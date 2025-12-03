# Tair

> [Alibaba Cloud Tair](https://www.alibabacloud.com/help/en/tair/latest/what-is-tair) is a cloud native in-memory database service
> developed by `Alibaba Cloud`. It provides rich data models and enterprise-grade capabilities to
> support your real-time online scenarios while maintaining full compatibility with open-source `Redis`.
> `Tair` also introduces persistent memory-optimized instances that are based on
> new non-volatile memory (NVM) storage medium.

## Installation and Setup

Install Tair Python SDK:

<CodeGroup>
  ```bash pip theme={null}
  pip install tair
  ```

  ```bash uv theme={null}
  uv add tair
  ```
</CodeGroup>

## Vector Store

```python  theme={null}
from langchain_community.vectorstores import Tair
```

See a [usage example](/oss/python/integrations/vectorstores/tair).

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/tair.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt