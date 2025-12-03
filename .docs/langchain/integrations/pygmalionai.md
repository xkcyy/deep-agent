# PygmalionAI

> [PygmalionAI](https://pygmalion.chat/) is a company supporting the
> open-source models by serving the inference endpoint
> for the [Aphrodite Engine](https://github.com/PygmalionAI/aphrodite-engine).

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install aphrodite-engine
  ```

  ```bash uv theme={null}
  uv add aphrodite-engine
  ```
</CodeGroup>

## LLMs

See a [usage example](/oss/python/integrations/llms/aphrodite).

```python  theme={null}
from langchain_community.llms import Aphrodite
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/pygmalionai.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt