# Postgres Embedding

> [pg\_embedding](https://github.com/neondatabase/pg_embedding) is an open-source package for
> vector similarity search using `Postgres` and the `Hierarchical Navigable Small Worlds`
> algorithm for approximate nearest neighbor search.

## Installation and Setup

We need to install several python packages.

<CodeGroup>
  ```bash pip theme={null}
  pip install psycopg2-binary
  ```

  ```bash uv theme={null}
  uv add psycopg2-binary
  ```
</CodeGroup>

## Vector Store

See a [usage example](/oss/python/integrations/vectorstores/pgembedding).

```python  theme={null}
from langchain_community.vectorstores import PGEmbedding
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/pg_embedding.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt