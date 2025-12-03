# ChatUpstage

This notebook covers how to get started with Upstage chat models.

## Installation

Install `langchain-upstage` package.

```bash  theme={null}
pip install -U langchain-upstage
```

## Environment Setup

Make sure to set the following environment variables:

* `UPSTAGE_API_KEY`: Your Upstage API key from [Upstage console](https://console.upstage.ai/).

## Usage

```python  theme={null}
import os

os.environ["UPSTAGE_API_KEY"] = "YOUR_API_KEY"
```

```python  theme={null}
from langchain_core.prompts import ChatPromptTemplate
from langchain_upstage import ChatUpstage

chat = ChatUpstage()
```

```python  theme={null}
# using chat invoke
chat.invoke("Hello, how are you?")
```

```python  theme={null}
# using chat stream
for m in chat.stream("Hello, how are you?"):
    print(m)
```

## Chaining

```python  theme={null}
# using chain
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to French."),
        ("human", "Translate this sentence from English to French. {english_text}."),
    ]
)
chain = prompt | chat

chain.invoke({"english_text": "Hello, how are you?"})
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/upstage.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt