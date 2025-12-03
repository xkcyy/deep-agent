# Graph RAG

## Overview

[Graph RAG](https://datastax.github.io/graph-rag/) provides a retriever interface
that combines **unstructured** similarity search on vectors with **structured**
traversal of metadata properties. This enables graph-based retrieval over **existing**
vector stores.

## Installation and setup

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-graph-retriever
  ```

  ```bash uv theme={null}
  uv add langchain-graph-retriever
  ```
</CodeGroup>

## Retrievers

```python  theme={null}
from langchain_graph_retriever import GraphRetriever
```

For more information, see the [Graph RAG Integration Guide](/oss/python/integrations/retrievers/graph_rag).

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/graph_rag.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt