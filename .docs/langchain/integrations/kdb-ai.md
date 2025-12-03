# KDB.AI

> [KDB.AI](https://kdb.ai) is a powerful knowledge-based vector database and search engine that allows you to build scalable, reliable AI applications, using real-time data, by providing advanced search, recommendation and personalization.

## Installation and Setup

Install the Python SDK:

<CodeGroup>
  ```bash pip theme={null}
  pip install kdbai-client
  ```

  ```bash uv theme={null}
  uv add kdbai-client
  ```
</CodeGroup>

## Vector store

There exists a wrapper around KDB.AI indexes, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

```python  theme={null}
from langchain_community.vectorstores import KDBAI
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/kdbai.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt