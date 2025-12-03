# LangGraph Memory 机制

> 本文档介绍 LangGraph 的状态持久化与 Checkpoint 机制。

## 短期记忆 (Short-term Memory)

短期记忆通过 Checkpointer 实现，用于保存对话历史：

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
agent = create_react_agent(model, tools=[], checkpointer=checkpointer)
```

## 长期记忆 (Long-term Memory)

长期记忆用于跨会话持久化信息，需要配置 Store：

```python
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
```

## Thread 配置

使用 `thread_id` 区分不同对话：

```python
config = {"configurable": {"thread_id": "user-123"}}
result = agent.invoke({"messages": [...]}, config=config)
```

