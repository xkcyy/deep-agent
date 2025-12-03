# Linkup

> [Linkup](https://www.linkup.so/) provides an API to connect LLMs to the web and the Linkup Premium Partner sources.

## Installation and Setup

To use the Linkup provider, you first need a valid API key, which you can find by signing-up [here](https://app.linkup.so/sign-up).
You will also need the `langchain-linkup` package, which you can install using pip:

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-linkup
  ```

  ```bash uv theme={null}
  uv add langchain-linkup
  ```
</CodeGroup>

## Retriever

See a [usage example](/oss/python/integrations/retrievers/linkup_search).

```python  theme={null}
from langchain_linkup import LinkupSearchRetriever

retriever = LinkupSearchRetriever(
    depth="deep",  # "standard" or "deep"
    linkup_api_key=None,  # API key can be passed here or set as the LINKUP_API_KEY environment variable
)
```

## Tools

See a [usage example](/oss/python/integrations/tools/linkup_search).

```python  theme={null}
from langchain_linkup import LinkupSearchTool

tool = LinkupSearchTool(
    depth="deep",  # "standard" or "deep"
    output_type="searchResults",  # "searchResults", "sourcedAnswer" or "structured"
    linkup_api_key=None,  # API key can be passed here or set as the LINKUP_API_KEY environment variable
)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/linkup.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt