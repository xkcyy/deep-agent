# Transwarp

> [Transwarp](https://www.transwarp.cn/en/introduction) aims to build
> enterprise-level big data and AI infrastructure software,
> to shape the future of data world. It provides enterprises with
> infrastructure software and services around the whole data lifecycle,
> including integration, storage, governance, modeling, analysis,
> mining and circulation.
>
> `Transwarp` focuses on technology research and
> development and has accumulated core technologies in these aspects:
> distributed computing, SQL compilations, database technology,
> unification for multi-model data management, container-based cloud computing,
> and big data analytics and intelligence.

## Installation

You have to install several python packages:

<CodeGroup>
  ```bash pip theme={null}
  pip install -U tiktoken hippo-api
  ```

  ```bash uv theme={null}
  uv add tiktoken hippo-api
  ```
</CodeGroup>

and get the connection configuration.

## Vector stores

### Hippo

See [a usage example and installation instructions](/oss/python/integrations/vectorstores/hippo).

```python  theme={null}
from langchain_community.vectorstores.hippo import Hippo
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/transwarp.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt