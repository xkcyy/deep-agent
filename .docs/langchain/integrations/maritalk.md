# MariTalk

> [MariTalk](https://www.maritaca.ai/en) is an LLM-based chatbot trained to meet the needs of Brazil.

## Installation and Setup

You have to get the MariTalk API key.

You also need to install the `httpx` Python package.

<CodeGroup>
  ```bash pip theme={null}
  pip install httpx
  ```

  ```bash uv theme={null}
  uv add httpx
  ```
</CodeGroup>

## Chat models

See a [usage example](/oss/python/integrations/chat/maritalk).

```python  theme={null}
from langchain_community.chat_models import ChatMaritalk
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/maritalk.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt