# Deep Agents LangChain Backend

基于 LangChain 1.x（无 LangGraph、多 Agent）实现的 DeepAgent 能力后端。目标是保留原有 `deep-agents-backend` 的接口形态（`/assistants`、`/threads`、`/threads/{id}/runs/stream`、`/threads/{id}/state`），提供单 Agent 版本的对话、工具调用和文件系统能力，方便 `deep-agents-ui` 无需改动即可接入。

> 参考文档：`.docs/langchain/deep-agents/deep-agents-overview.md`、`.docs/langchain/deep-agents/backends.md`

## 特性

- ✅ LangChain 1.x 工具调用链（无 LangGraph 依赖）
- ✅ Tavily `internet_search` 工具
- ✅ 文件系统工具：`ls`、`read_file`、`write_file`、`edit_file`
- ✅ 待办规划工具：`write_todos`
- ✅ 与 `deep-agents-backend` 相同的 API 路径形态，便于前端复用
- ✅ 基于 `.env` 的模型与后端配置

## 快速开始

```bash
cd deep-agents-langchain
uv sync  # 或 pip install -e .
cp env.example .env
uvicorn deep_agents_langchain.server:app --reload --port 8123
```

## 配置

环境变量（见 `env.example`）：

- `OPENAI_API_KEY` / `OPENAI_API_BASE`
- `TAVILY_API_KEY`
- `DEFAULT_MODEL`（示例：`openai:gpt-4o-mini`）
- `FILESYSTEM_ROOT_DIR`（文件工具沙盒根目录，默认 `./workspace`）

## 代码结构

```
deep-agents-langchain/
├── src/deep_agents_langchain/
│   ├── agent.py          # 单 Agent 构建与消息历史
│   ├── prompts.py        # 系统提示词
│   ├── config.py         # 配置加载
│   ├── server.py         # FastAPI 兼容接口
│   └── tools/            # 工具实现（搜索、文件、待办）
└── tests/                # 单元测试（待补充）
```

## API 兼容层

- `GET /assistants`：返回单个 `deep_agent`
- `POST /threads`：创建线程并初始化状态
- `GET/PUT /threads/{id}/state`：获取/更新线程状态（消息、todos、文件映射）
- `POST /threads/{id}/runs/stream`：流式执行单次对话，事件格式对齐 LangGraph SSE（基础版）

## 已知差异

- 不提供多 Agent/子代理能力，主 Agent 通过工具完成搜索、文件与规划任务。
- SSE 仅覆盖前端现有使用的基础事件，后续若需完整 LangGraph 事件集，可再扩展。

## 许可证

MIT License

