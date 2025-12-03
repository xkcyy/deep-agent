# Vespa

> [Vespa](https://vespa.ai/) is a fully featured search engine and vector database.
> It supports vector search (ANN), lexical search, and search in structured data, all in the same query.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install pyvespa
  ```

  ```bash uv theme={null}
  uv add pyvespa
  ```
</CodeGroup>

## Retriever

See a [usage example](/oss/python/integrations/retrievers/vespa).

```python  theme={null}
from langchain_classic.retrievers import VespaRetriever
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/vespa.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt