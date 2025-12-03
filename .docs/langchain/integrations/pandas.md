# Pandas

> [pandas](https://pandas.pydata.org) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
> built on top of the `Python` programming language.

## Installation and Setup

Install the `pandas` package using `pip`:

<CodeGroup>
  ```bash pip theme={null}
  pip install pandas
  ```

  ```bash uv theme={null}
  uv add pandas
  ```
</CodeGroup>

## Document loader

See a [usage example](/oss/python/integrations/document_loaders/pandas_dataframe).

```python  theme={null}
from langchain_community.document_loaders import DataFrameLoader
```

## Toolkit

See a [usage example](/oss/python/integrations/tools/pandas).

```python  theme={null}
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/pandas.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt