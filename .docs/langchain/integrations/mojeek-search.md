# Mojeek Search

The following notebook will explain how to get results using Mojeek Search. Please visit [Mojeek Website](https://www.mojeek.com/services/search/web-search-api/) to obtain an API key.

```python  theme={null}
from langchain_community.tools import MojeekSearch
```

```python  theme={null}
api_key = "KEY"  # obtained from Mojeek Website
```

```python  theme={null}
search = MojeekSearch.config(api_key=api_key, search_kwargs={"t": 10})
```

In `search_kwargs` you can add any search parameter that you can find on [Mojeek Documentation](https://www.mojeek.com/support/api/search/request_parameters.html)

```python  theme={null}
search.run("mojeek")
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/mojeek_search.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt