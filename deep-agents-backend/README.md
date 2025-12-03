# Deep Agents Backend

基于 LangGraph 的 Deep Agent 后端服务，为 `deep-agents-ui` 前端提供 API 支持。

## 特性

- 🤖 **Deep Agent 架构**: 支持计划、文件系统、子代理
- 🔍 **内置工具**: `internet_search` (Tavily)，可扩展更多工具
- 👥 **子代理系统**: 研究代理、代码代理
- 💾 **文件系统后端**: 默认使用沙盒文件系统，可切换为纯内存

## 快速开始

### 1. 安装依赖

```bash
# 使用 uv (推荐)
uv sync

# 或使用 pip
pip install -e .
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
cp env.example .env

# 编辑 .env 文件，填入 API Keys
```

必需的环境变量：
- `OPENAI_API_KEY`: OpenAI 兼容接口的 API Key
- `OPENAI_API_BASE`: 可选，自定义 OpenAI 兼容 API Base（默认 `https://api.openai.com/v1`）
- `TAVILY_API_KEY`: 网络搜索工具 (可选，启用 `internet_search` 时必填)

### 3. 启动开发服务器

```bash
# 使用 LangGraph CLI
langgraph dev

# 服务将在 http://localhost:8123 启动
```

### 4. 连接前端

在 `deep-agents-ui` 前端配置中设置：
- **Deployment URL**: `http://localhost:8123`
- **Assistant ID**: `deep_agent`

## 项目结构

```
deep-agents-backend/
├── src/
│   ├── agent/           # 主 Agent 实现
│   │   ├── deep_agent.py
│   │   └── prompts.py
│   ├── tools/           # 自定义工具
│   │   └── search.py
│   ├── subagents/       # 子代理配置
│   │   ├── research.py
│   │   └── code.py
│   └── config/          # 配置管理
│       └── settings.py
├── tests/               # 测试文件
├── langgraph.json       # LangGraph 配置
├── pyproject.toml       # 项目依赖
└── env.example          # 环境变量模板
```

## 配置选项

### 模型配置

支持的模型格式: `provider:model-name`

```env
# 默认使用 OpenAI 兼容模型
DEFAULT_MODEL=openai:gpt-4o-mini

# 如需其他模型，可更改 provider:model
DEFAULT_MODEL=openai:gpt-4o
```

### 后端存储

```env
# 后端类型: state 或 filesystem
BACKEND_TYPE=filesystem

# 文件系统根目录 (仅在 filesystem 时生效)
FILESYSTEM_ROOT_DIR=./workspace
```

## 扩展指南

### 添加新工具

```python
# src/tools/my_tool.py
from langchain_core.tools import tool

@tool
def my_custom_tool(param: str) -> str:
    """Tool description."""
    return f"Result: {param}"
```

### 添加新子代理

```python
# src/subagents/my_subagent.py
my_subagent = {
    "name": "my-subagent",
    "description": "What this subagent does",
    "system_prompt": "Detailed instructions...",
    "tools": [my_tool],
}
```

## API 端点

LangGraph Server 提供以下 API：

| 端点 | 方法 | 描述 |
|------|------|------|
| `/assistants` | GET | 获取可用 assistants |
| `/threads` | POST | 创建新会话 |
| `/threads/{id}/runs/stream` | POST | 流式执行 |
| `/threads/{id}/state` | GET/PUT | 获取/更新状态 |

详细 API 文档请参考 [LangGraph SDK 文档](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/)

## 开发

```bash
# 运行测试
pytest

# 代码格式化
ruff format .

# 类型检查
mypy src/
```

## 许可证

MIT License

