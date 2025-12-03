# Yellowbrick

> [Yellowbrick](https://yellowbrick.com/) is a provider of
> Enterprise Data Warehousing, Ad-hoc and Streaming Analytics,
> BI and AI workloads.

## Vector store

We have to install a python package:

<CodeGroup>
  ```bash pip theme={null}
  pip install psycopg2
  ```

  ```bash uv theme={null}
  uv add psycopg2
  ```
</CodeGroup>

```python  theme={null}
from langchain_community.vectorstores import Yellowbrick
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/yellowbrick.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt