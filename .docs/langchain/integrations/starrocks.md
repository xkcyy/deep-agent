# StarRocks

> [StarRocks](https://www.starrocks.io/) is a High-Performance Analytical Database.
> `StarRocks` is a next-gen sub-second MPP database for full analytics scenarios, including multi-dimensional analytics, real-time analytics and ad-hoc query.

> Usually `StarRocks` is categorized into OLAP, and it has showed excellent performance in [ClickBench — a Benchmark For Analytical DBMS](https://benchmark.clickhouse.com/). Since it has a super-fast vectorized execution engine, it could also be used as a fast vectordb.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install pymysql
  ```

  ```bash uv theme={null}
  uv add pymysql
  ```
</CodeGroup>

## Vector Store

See a [usage example](/oss/python/integrations/vectorstores/starrocks).

```python  theme={null}
from langchain_community.vectorstores import StarRocks
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/starrocks.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt