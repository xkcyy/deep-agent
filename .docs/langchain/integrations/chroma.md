# Chroma

> [Chroma](https://docs.trychroma.com/getting-started) is a database for building AI applications with embeddings.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-chroma
  ```

  ```bash uv theme={null}
  uv add langchain-chroma
  ```
</CodeGroup>

## VectorStore

There exists a wrapper around Chroma vector databases, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

```python  theme={null}
from langchain_chroma import Chroma
```

For a more detailed walkthrough of the Chroma wrapper, see [this notebook](/oss/python/integrations/vectorstores/chroma)

## Retriever

```python  theme={null}
from langchain_classic.retrievers import SelfQueryRetriever
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/chroma.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt