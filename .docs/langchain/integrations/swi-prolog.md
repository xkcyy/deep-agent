# SWI-Prolog

SWI-Prolog offers a comprehensive free Prolog environment.

## Installation and Setup

Once SWI-Prolog has been installed, install lanchain-prolog using pip:

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-prolog
  ```

  ```bash uv theme={null}
  uv add langchain-prolog
  ```
</CodeGroup>

## Tools

The `PrologTool` class allows the generation of langchain tools that use Prolog rules to generate answers.

```python  theme={null}
from langchain_prolog import PrologConfig, PrologTool
```

See a [usage example](/oss/python/integrations/tools/prolog_tool).

See the same guide for usage examples of `PrologRunnable`, which allows the generation
of LangChain runnables that use Prolog rules to generate answers.

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/prolog.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt