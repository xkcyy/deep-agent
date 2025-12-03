# Annoy

> [Annoy](https://github.com/spotify/annoy) (`Approximate Nearest Neighbors Oh Yeah`)
> is a C++ library with Python bindings to search for points in space that are
> close to a given query point. It also creates large read-only file-based data
> structures that are mapped into memory so that many processes may share the same data.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install annoy
  ```

  ```bash uv theme={null}
  uv add annoy
  ```
</CodeGroup>

## Vectorstore

See a [usage example](/oss/python/integrations/vectorstores/annoy).

```python  theme={null}
from langchain_community.vectorstores import Annoy
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/annoy.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt