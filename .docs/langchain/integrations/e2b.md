# E2B

> [E2B](https://e2b.dev/) provides open-source secure sandboxes
> for AI-generated code execution. See more [here](https://github.com/e2b-dev).

## Installation and Setup

You have to install a python package:

<CodeGroup>
  ```bash pip theme={null}
  pip install e2b_code_interpreter
  ```

  ```bash uv theme={null}
  uv add e2b_code_interpreter
  ```
</CodeGroup>

## Tool

See a [usage example](/oss/python/integrations/tools/e2b_data_analysis).

```python  theme={null}
from langchain_community.tools import E2BDataAnalysisTool
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/e2b.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt