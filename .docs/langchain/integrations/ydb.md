# YDB

All functionality related to YDB.

> [YDB](https://ydb.tech/) is a versatile open source Distributed SQL Database that combines
> high availability and scalability with strong consistency and ACID transactions.
> It accommodates transactional (OLTP), analytical (OLAP), and streaming workloads simultaneously.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-ydb
  ```

  ```bash uv theme={null}
  uv add langchain-ydb
  ```
</CodeGroup>

## Vector Store

To import YDB vector store:

```python  theme={null}
from langchain_ydb.vectorstores import YDB
```

For a more detailed walkthrough of the YDB vector store, see [this notebook](/oss/python/integrations/vectorstores/ydb).

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/ydb.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt