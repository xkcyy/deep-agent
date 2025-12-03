# Tools API Reference

> LangGraph 工具绑定与自定义工具参考。

## 定义工具

使用 `@tool` 装饰器定义工具：

```python
from langchain_core.tools import tool

@tool
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"
```

## 工具绑定

将工具绑定到 Agent：

```python
tools = [search, calculator]
agent = create_react_agent(model, tools=tools)
```

## 预构建工具

LangChain 提供多种预构建工具：

- `TavilySearchResults` - 网络搜索
- `WikipediaQueryRun` - Wikipedia 查询
- `PythonREPLTool` - Python 代码执行

## MCP 集成

使用 MCP 协议集成外部工具：

```python
from langchain_mcp_adapters import MCPToolkit

toolkit = MCPToolkit(server_params=...)
tools = toolkit.get_tools()
```

