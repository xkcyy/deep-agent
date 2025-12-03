# DuckDB

> [DuckDB](https://duckdb.org/) is an in-process SQL OLAP database management system.

## Installation and Setup

First, you need to install `duckdb` python package.

<CodeGroup>
  ```bash pip theme={null}
  pip install duckdb
  ```

  ```bash uv theme={null}
  uv add duckdb
  ```
</CodeGroup>

## Document Loader

```python  theme={null}
from langchain_community.document_loaders import DuckDBLoader
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/duckdb.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt