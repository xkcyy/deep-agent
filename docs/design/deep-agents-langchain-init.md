# deep-agents-langchain 初始化构建详细设计文档

> 参考来源：`deep-agents-backend/README.md`、`.docs/langchain/deep-agents/agent-harness-capabilities.md`、`.docs/langchain/deep-agents/backends.md`、`.docs/langchain/deep-agents/quickstart.md`、`.docs/langchain/deep-agents/deep-agents-overview.md`、`docs/requirements/13-tool-calls-and-display.md`。

## 0. 术语表（傻瓜工程师可直接理解）
- 线程 thread：一次持续会话/任务的容器，相当于“会话 ID”。同一个 thread_id 下保存全部消息、状态、待办、文件引用。
- 运行 run：在某个 thread 上的一次完整执行（用户提问触发的推理过程，含工具调用与最终回复）。
- 工具调用 tool_call：助手消息里发出的单个工具请求，包含 id/name/args/status。tool 结果需用相同 tool_call_id 写回。
- SSE 事件：服务端发送的流事件，格式 `event: <type>\ndata: <json字符串>\n\n`，type 可能是 message/tool/end/error。
- 沙盒根目录 WORKSPACE_ROOT：文件工具可访问的唯一根路径，禁止越权路径或符号链接逃逸。

## 1. 目标与范围
- 项目名：`deep-agents-langchain`。
- 单智能体后端服务，使用 LangChain 1.x 的 `create_deep_agent` 构建，不使用 `langgraph` CLI 启动，改用自定义 FastAPI+Uvicorn。
- 兼容 API 形态（/assistants、/threads、/threads/{id}/runs/stream、/threads/{id}/state），供前端直接复用。
- 存储：SQLite 持久化线程、消息、运行、工具调用、状态；文件存储落地本地沙盒目录。

## 2. 依赖与配置
- 版本策略：锁定到“交付当日可用的最新 1.x/兼容”版本；以下为初始 Pin，若交付时有更新，请在 `requirements.txt/constraints.txt` 中替换为当日最新。
- 核心依赖（示例 Pin）：
  - `python==3.11.*`（推荐）或 3.12.*
  - `langchain==1.3.0`（如有更新，改为最新 1.x）
  - `deepagents==0.1.11`（如有更新，改为最新）
  - `langgraph==0.2.42`（仅运行时依赖，不使用 CLI）
  - `fastapi==0.115.0`
  - `uvicorn[standard]==0.31.0`
  - `pydantic==2.9.2`
  - `sqlalchemy==2.0.35`
  - `aiosqlite==0.20.0`（如使用异步 SQLite）
  - `python-dotenv==1.0.1`
  - `httpx==0.27.2`（外部请求/回调）
  - `structlog==24.4.0`（可选日志）
  - `tavily-python==0.3.7`（可选，启用搜索）
- 环境变量/.env：
  - 必需：`OPENAI_API_KEY`
  - 可选：`OPENAI_API_BASE`、`DEFAULT_MODEL`（如 `openai:gpt-4o-mini`）、`TAVILY_API_KEY`、`SQLITE_PATH`、`WORKSPACE_ROOT`、`TIMEOUT_SECONDS`、`MAX_TOKENS_RESULT_TO_FILE`

## 3. 工程结构（唯一推荐：src 布局，只有一个包目录）
```
deep-agents-langchain/
├── pyproject.toml / requirements.txt        # 依赖声明（含版本）
├── .env.example                             # 环境变量示例
├── docs/
│   └── design/
│       └── deep-agents-langchain-init.md    # 本设计文档
├── src/
│   └── deep_agents_langchain/               # 唯一的包目录（不要再建重复目录）
│       ├── main.py                          # FastAPI 应用入口（uvicorn 启动）
│       ├── api/                             # 路由与 SSE 适配
│       │   ├── __init__.py
│       │   └── routes.py
│       ├── agent/                           # create_deep_agent 构建、prompt、工具封装
│       │   ├── __init__.py
│       │   ├── builder.py
│       │   └── prompts.py
│       ├── service/                         # 线程/运行/消息/工具结果协调
│       │   ├── __init__.py
│       │   ├── threads.py
│       │   └── runs.py
│       ├── storage/                         # SQLite + 文件元数据
│       │   ├── __init__.py
│       │   ├── db.py
│       │   ├── models.py
│       │   └── repositories.py
│       ├── config/                          # 配置与常量
│       │   ├── __init__.py
│       │   └── settings.py
│       └── utils/                           # 日志、校验、SSE 工具
│           ├── __init__.py
│           ├── logging.py
│           └── sse.py
└── tests/
    ├── test_api.py
    ├── test_agent.py
    └── test_storage.py
```

## 4. 架构概览
- 分层：
  - API 层：FastAPI 路由 + SSE 输出。
  - Service 层：线程/运行管理、消息与工具结果协调、状态读写。
  - Agent 层：使用 `create_deep_agent` 创建单一 agent。
  - 存储层：SQLite（WAL 模式）+ 本地沙盒文件系统。
- 启动：`uvicorn deep_agents_langchain.main:app --host 0.0.0.0 --port 8123`（禁止使用 langgraph 命令）。

## 5. Agent 构建（必须指明给后续 AI）
- 调用 `create_deep_agent` 时配置：
  - tools：`[ls, read_file, write_file, edit_file, glob, grep, write_todos, task, internet_search?]`
  - backend：`FilesystemBackend(root_dir=WORKSPACE_ROOT, virtual_mode=True)`（沙盒，禁止越权）
  - system_prompt：中文，说明工具用法、错误重试、大结果落盘策略。
  - model：由 `DEFAULT_MODEL` 指定，格式 `provider:model`。
  - store：可留空（如无跨线程持久 store）。
- 大结果驱逐：当工具结果超过阈值（默认 20k tokens），写入文件 `/workspace/outputs/<id>.txt`，返回结果中注明“内容已写入 <path>”。
- 子任务工具 `task`：单智能体模式下直接返回“未开启子代理，不创建新 agent”。
- 搜索工具 `internet_search`：无 `TAVILY_API_KEY` 时返回“搜索未启用”文本，不抛异常。
- 会话摘要/截断：可采用默认策略（超 170k tokens 自动插入系统摘要消息，保留最近 6 条原文）。

## 6. 工具行为要求（傻瓜化规则）
- 通用：不得抛异常，错误返回字符串。
- `ls`：列出目录，返回路径/是否目录/大小/修改时间（可用则填）。
- `read_file(file_path, offset=0, limit=2000)`：返回带行号字符串，越界返回错误文本。
- `write_file(file_path, content)`：create-only，存在则返回错误文本。
- `edit_file(file_path, old_string, new_string, replace_all=False)`：默认唯一匹配，否则报错；replace_all=True 才全量替换；不存在文件或匹配失败需返回错误文本。
- `glob(pattern, path="/")`：返回匹配文件列表（路径+基本元信息）；无匹配返回空列表。
- `grep(pattern, path=None, glob=None)`：返回匹配列表；非法正则返回错误文本；无匹配返回空列表。
- `write_todos`：维护 pending/in_progress/completed 状态，存 thread 状态。
- `task`：返回固定提示，不派生子代理。
- 大结果落盘：结果中需写明保存路径，避免长文本直接塞进消息。

## 7. API 详细设计（含示例）
### 7.1 GET /assistants
- 响应示例：
```
[
  {
    "assistant_id": "deep_agent",
    "name": "Deep Agent",
    "description": "单智能体，含文件/搜索/待办工具",
    "model": "openai:gpt-4o-mini",
    "tools": ["ls","read_file","write_file","edit_file","glob","grep","write_todos","task","internet_search"]
  }
]
```

### 7.2 POST /threads
- 入参（JSON，全部可选）：
  - `metadata: object?` 任意元数据
  - `initial_state: object?` 初始状态 KV
- 响应：`{ "thread_id": "<uuid>" }`
- 线程定义：会话 ID，容纳全部消息/状态/文件引用。

### 7.3 POST /threads/{id}/runs/stream
- 入参（JSON）：
  - `input`（必填）：`{ "messages": [ { "role": "user|assistant|system|tool", "content": <string|object|array> } ] }`
    - 常用最小输入：单条 user 消息。
  - `stream`（可选，默认 true，若 false 则可实现一次性 JSON 返回）
```
{
  "input": {
    "messages": [
      { "role": "user", "content": "帮我总结 README" }
    ]
  },
  "stream": true
}
```
- SSE 事件最小序列示例（data 是 JSON 字符串）：
```
event: message
data: {"message_id":"m1","thread_id":"t1","role":"assistant","tool_calls":[{"id":"tc1","name":"read_file","args":{"file_path":"/workspace/README.md","offset":0,"limit":2000},"status":"pending"}]}

event: tool
data: {"tool_call_id":"tc1","status":"completed","result":"L1:...带行号内容..."}

event: message
data: {"message_id":"m2","thread_id":"t1","role":"assistant","content":"总结结果...","tool_calls":[]}

event: end
data: {"run_id":"r1","status":"completed","error":null}
```
- 错误示例：`event: error` + `data: {"message":"thread not found","code":"THREAD_NOT_FOUND"}`。
- 要求：tool_call_id 必须匹配；如调用被中断需发 `status="interrupted"` 的 tool 事件或合成 ToolMessage。

### 7.4 GET /threads/{id}/state
- 入参：路径参数 `id`，无 body
- 响应示例：
```
{
  "thread_id": "t1",
  "state": {"todos":[...], "vars": {...}},
  "updated_at": "...",
  "messages_summary": [],
  "files": []
}
```

### 7.5 PUT /threads/{id}/state
- 入参（JSON）：
  - `state: object` 要写入的 KV
  - `replace: bool`（默认 false；true 则全量覆盖 state，false 则合并）
- 响应：同 GET，返回更新后的 state。

## 8. 数据模型（SQLite 表）
- `threads(id TEXT PK, metadata JSON, created_at, updated_at)`
- `messages(id TEXT PK, thread_id TEXT FK, role TEXT, content JSON, order_num INT, created_at)`
- `runs(id TEXT PK, thread_id TEXT FK, status TEXT, input JSON, output JSON, error TEXT, started_at, ended_at)`
- `tool_calls(id TEXT PK, run_id TEXT FK, name TEXT, args JSON, status TEXT, result JSON, error TEXT, created_at, updated_at)`
- `state(thread_id TEXT PK, kv JSON, updated_at)`
- 可选 `files_meta(path TEXT PK, size INT, modified_at, thread_id NULLABLE)`

## 9. 安全与校验
- 路径沙箱：所有文件操作必须在 WORKSPACE_ROOT 下，拒绝 `..` 和符号链接逃逸；违规返回错误文本。
- 正则/Glob 校验：非法模式返回错误文本。
- 模型/工具超时：返回 error 事件或在 end 事件中标记 status=error。
- 日志脱敏：不打印 API Key。

## 10. 状态管理与摘要
- 大结果落盘：见工具规则。
- 历史压缩：超阈值自动插入系统摘要消息，近期 6 条不压缩，可配置阈值。

## 11. 启动与运维
- 禁用 `langgraph dev/serve`，仅用自定义入口。
- 建议开启 SQLite WAL。
- Docker（可选）：python:3.11/3.12，安装依赖，暴露 8123。

## 12. 错误返回格式
- 统一示例：`{ "error": "说明" }` 或 `{ "code": "ERR_CODE", "message": "说明" }`。
- HTTP 码建议：400 入参错误；404 线程不存在；409 并发冲突（可选）；500 服务异常。

## 13. 测试要点
- 单元：文件工具、待办、task 限制、搜索禁用提示、DB CRUD。
- 集成：创建线程→流式运行→工具调用→状态读写→大结果落盘。
- 前端兼容：tool_call 字段完整，SSE 顺序符合示例，错误/中断能展示。 

