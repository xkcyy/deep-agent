# vlite

This page covers how to use [vlite](https://github.com/sdan/vlite) within LangChain. vlite is a simple and fast vector database for storing and retrieving embeddings.

## Installation and Setup

To install vlite, run the following command:

<CodeGroup>
  ```bash pip theme={null}
  pip install vlite
  ```

  ```bash uv theme={null}
  uv add vlite
  ```
</CodeGroup>

For PDF OCR support, install the `vlite[ocr]` extra:

<CodeGroup>
  ```bash pip theme={null}
  pip install vlite[ocr]
  ```

  ```bash uv theme={null}
  uv add vlite[ocr]
  ```
</CodeGroup>

## VectorStore

vlite provides a wrapper around its vector database, allowing you to use it as a vectorstore for semantic search and example selection.

To import the vlite vectorstore:

```python  theme={null}
from langchain_community.vectorstores import vlite
```

### Usage

For a more detailed walkthrough of the vlite wrapper, see [this notebook](/oss/python/integrations/vectorstores/vlite).

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/vlite.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt