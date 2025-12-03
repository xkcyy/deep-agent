# AnalyticDB

> [AnalyticDB for PostgreSQL](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/latest/product-introduction-overview)
> is a massively parallel processing (MPP) data warehousing service
> from [Alibaba Cloud](https://www.alibabacloud.com/)
> that is designed to analyze large volumes of data online.

> `AnalyticDB for PostgreSQL` is developed based on the open-source `Greenplum Database`
> project and is enhanced with in-depth extensions by `Alibaba Cloud`. AnalyticDB
> for PostgreSQL is compatible with the ANSI SQL 2003 syntax and the PostgreSQL and
> Oracle database ecosystems. AnalyticDB for PostgreSQL also supports row store and
> column store. AnalyticDB for PostgreSQL processes petabytes of data offline at a
> high performance level and supports highly concurrent.

This page covers how to use the AnalyticDB ecosystem within LangChain.

## Installation and Setup

You need to install the `sqlalchemy` python package.

<CodeGroup>
  ```bash pip theme={null}
  pip install sqlalchemy
  ```

  ```bash uv theme={null}
  uv add sqlalchemy
  ```
</CodeGroup>

## VectorStore

See a [usage example](/oss/python/integrations/vectorstores/analyticdb).

```python  theme={null}
from langchain_community.vectorstores import AnalyticDB
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/analyticdb.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt