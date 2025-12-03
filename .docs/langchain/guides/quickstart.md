# LangGraph 快速开始

> 本文档介绍如何使用 LangGraph 创建基础 Agent。

## 安装

```bash
pip install langgraph langchain-openai
```

## 创建基础 Agent

```python
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")
agent = create_react_agent(model, tools=[])
```

## 运行 Agent

```python
result = agent.invoke({"messages": [("user", "Hello!")]})
print(result["messages"][-1].content)
```

## 更多资源

- [官方文档](https://langchain-ai.github.io/langgraph/)
- [Memory 机制](memory.md)

