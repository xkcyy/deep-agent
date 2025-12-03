# Arize

[Arize](https://arize.com) is an AI observability and LLM evaluation platform that offers
support for LangChain applications, providing detailed traces of input, embeddings, retrieval,
functions, and output messages.

## Installation and Setup

First, you need to install `arize` python package.

<CodeGroup>
  ```bash pip theme={null}
  pip install arize
  ```

  ```bash uv theme={null}
  uv add arize
  ```
</CodeGroup>

Second, you need to set up your [Arize account](https://app.arize.com/auth/join)
and get your  `API_KEY` or `SPACE_KEY`.

## Callback handler

```python  theme={null}
from langchain_community.callbacks import ArizeCallbackHandler
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/arize.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt