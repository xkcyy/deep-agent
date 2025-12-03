# Agent API Reference

> LangGraph Agent 相关 API 参考。

## create_react_agent

创建 ReAct 模式的 Agent。

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model,                    # 语言模型
    tools=[],                 # 工具列表
    checkpointer=None,        # 状态持久化
    state_schema=None,        # 自定义状态 Schema
    prompt=None,              # 系统提示词
)
```

## 运行方法

### invoke (同步)

```python
result = agent.invoke({"messages": [("user", "Hello")]})
```

### ainvoke (异步)

```python
result = await agent.ainvoke({"messages": [("user", "Hello")]})
```

### stream (流式)

```python
for chunk in agent.stream({"messages": [("user", "Hello")]}):
    print(chunk)
```

