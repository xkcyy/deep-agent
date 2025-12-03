# MistralAI

> [Mistral AI](https://docs.mistral.ai/api/) is a platform that offers hosting for their powerful open source models.

## Installation and Setup

A valid [API key](https://console.mistral.ai/users/api-keys/) is needed to communicate with the API.

You will also need the `langchain-mistralai` package:

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-mistralai
  ```

  ```bash uv theme={null}
  uv add langchain-mistralai
  ```
</CodeGroup>

## Chat models

### ChatMistralAI

See a [usage example](/oss/python/integrations/chat/mistralai).

```python  theme={null}
from langchain_mistralai.chat_models import ChatMistralAI
```

## Embedding models

### MistralAIEmbeddings

See a [usage example](/oss/python/integrations/text_embedding/mistralai).

```python  theme={null}
from langchain_mistralai import MistralAIEmbeddings
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/mistralai.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt