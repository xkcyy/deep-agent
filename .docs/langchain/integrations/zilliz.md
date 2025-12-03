# Zilliz

> [Zilliz Cloud](https://zilliz.com/doc/quick_start) is a fully managed service on cloud for `LF AI Milvus®`,

## Installation and Setup

Install the Python SDK:

<CodeGroup>
  ```bash pip theme={null}
  pip install pymilvus
  ```

  ```bash uv theme={null}
  uv add pymilvus
  ```
</CodeGroup>

## Vectorstore

A wrapper around Zilliz indexes allows you to use it as a vectorstore,
whether for semantic search or example selection.

```python  theme={null}
from langchain_community.vectorstores import Milvus
```

For a more detailed walkthrough of the Miluvs wrapper, see [this notebook](/oss/python/integrations/vectorstores/zilliz)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/zilliz.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt