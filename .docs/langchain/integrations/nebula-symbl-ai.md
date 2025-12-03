# Nebula (Symbl.ai)

This notebook covers how to get started with [Nebula](https://docs.symbl.ai/docs/nebula-llm) - Symbl.ai's chat model.

### Integration details

Head to the [API reference](https://docs.symbl.ai/reference/nebula-chat) for detailed documentation.

### Model features: TODO

## Setup

### Credentials

To get started, request a [Nebula API key](https://platform.symbl.ai/#/login) and set the `NEBULA_API_KEY` environment variable:

```python  theme={null}
import getpass
import os

os.environ["NEBULA_API_KEY"] = getpass.getpass()
```

### Installation

The integration is set up in the `langchain-community` package.

## Instantiation

```python  theme={null}
from langchain_community.chat_models.symblai_nebula import ChatNebula
from langchain.messages import AIMessage, HumanMessage, SystemMessage
```

```python  theme={null}
chat = ChatNebula(max_tokens=1024, temperature=0.5)
```

## Invocation

```python  theme={null}
messages = [
    SystemMessage(
        content="You are a helpful assistant that answers general knowledge questions."
    ),
    HumanMessage(content="What is the capital of France?"),
]
chat.invoke(messages)
```

```output  theme={null}
AIMessage(content=[{'role': 'human', 'text': 'What is the capital of France?'}, {'role': 'assistant', 'text': 'The capital of France is Paris.'}])
```

### Async

```python  theme={null}
await chat.ainvoke(messages)
```

```output  theme={null}
AIMessage(content=[{'role': 'human', 'text': 'What is the capital of France?'}, {'role': 'assistant', 'text': 'The capital of France is Paris.'}])
```

### Streaming

```python  theme={null}
for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)
```

```output  theme={null}
 The capital of France is Paris.
```

### Batch

```python  theme={null}
chat.batch([messages])
```

```output  theme={null}
[AIMessage(content=[{'role': 'human', 'text': 'What is the capital of France?'}, {'role': 'assistant', 'text': 'The capital of France is Paris.'}])]
```

## Chaining

```python  theme={null}
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | chat
```

```python  theme={null}
chain.invoke({"topic": "cows"})
```

```output  theme={null}
AIMessage(content=[{'role': 'human', 'text': 'Tell me a joke about cows'}, {'role': 'assistant', 'text': "Sure, here's a joke about cows:\n\nWhy did the cow cross the road?\n\nTo get to the udder side!"}])
```

***

## API reference

Check out the [API reference](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.symblai_nebula.ChatNebula.html) for more detail.

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/symblai_nebula.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt