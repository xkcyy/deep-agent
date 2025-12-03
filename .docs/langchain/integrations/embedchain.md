# Embedchain

> [Embedchain](https://github.com/embedchain/embedchain) is a RAG framework to create
> data pipelines. It loads, indexes, retrieves and syncs all the data.
>
> It is available as an [open source package](https://github.com/embedchain/embedchain)
> and as a [hosted platform solution](https://app.embedchain.ai/).

## Installation and Setup

Install the package using pip:

<CodeGroup>
  ```bash pip theme={null}
  pip install embedchain
  ```

  ```bash uv theme={null}
  uv add embedchain
  ```
</CodeGroup>

## Retriever

See a [usage example](/oss/python/integrations/retrievers/embedchain).

```python  theme={null}
from langchain_community.retrievers import EmbedchainRetriever
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/embedchain.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt