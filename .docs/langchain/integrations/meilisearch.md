# Meilisearch

> [Meilisearch](https://meilisearch.com) is an open-source, lightning-fast, and hyper
> relevant search engine.
> It comes with great defaults to help developers build snappy search experiences.
>
> You can [self-host Meilisearch](https://www.meilisearch.com/docs/learn/getting_started/installation#local-installation)
> or run on [Meilisearch Cloud](https://www.meilisearch.com/pricing).
>
> `Meilisearch v1.3` supports vector search.

## Installation and Setup

See a [usage example](/oss/python/integrations/vectorstores/meilisearch) for detail configuration instructions.

We need to install `meilisearch` python package.

<CodeGroup>
  ```bash pip theme={null}
  pip install meilisearch
  ```

  ```bash uv theme={null}
  uv add meilisearch
  ```
</CodeGroup>

## Vector Store

See a [usage example](/oss/python/integrations/vectorstores/meilisearch).

```python  theme={null}
from langchain_community.vectorstores import Meilisearch
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/meilisearch.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt