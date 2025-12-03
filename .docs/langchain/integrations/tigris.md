# Tigris

> [Tigris](https://tigrisdata.com) is an open-source Serverless NoSQL Database and Search Platform designed to simplify building high-performance vector search applications.
> `Tigris` eliminates the infrastructure complexity of managing, operating, and synchronizing multiple tools, allowing you to focus on building great applications instead.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install tigrisdb openapi-schema-pydantic
  ```

  ```bash uv theme={null}
  uv add tigrisdb openapi-schema-pydantic
  ```
</CodeGroup>

## Vector Store

See a [usage example](/oss/python/integrations/vectorstores/tigris).

```python  theme={null}
from langchain_community.vectorstores import Tigris
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/tigris.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt