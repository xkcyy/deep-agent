# Dria

> [Dria](https://dria.co/) is a hub of public RAG models for developers to
> both contribute and utilize a shared embedding lake.

See more details about the LangChain integration with Dria
at [this page](https://dria.co/docs/integrations/langchain).

## Installation and Setup

You have to install a python package:

<CodeGroup>
  ```bash pip theme={null}
  pip install dria
  ```

  ```bash uv theme={null}
  uv add dria
  ```
</CodeGroup>

You have to get an API key from Dria. You can get it by signing up at [Dria](https://dria.co/).

## Retrievers

See a [usage example](/oss/python/integrations/retrievers/dria_index).

```python  theme={null}
from langchain_community.retrievers import DriaRetriever
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/dria.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt