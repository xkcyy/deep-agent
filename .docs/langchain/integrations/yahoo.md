# Yahoo

> [Yahoo (Wikipedia)](https://en.wikipedia.org/wiki/Yahoo) is an American web services provider.
>
> It provides a web portal, search engine Yahoo Search, and related
> services, including `My Yahoo`, `Yahoo Mail`, `Yahoo News`,
> `Yahoo Finance`, `Yahoo Sports` and its advertising platform, `Yahoo Native`.

## Tools

### Yahoo Finance News

We have to install a python package:

<CodeGroup>
  ```bash pip theme={null}
  pip install yfinance
  ```

  ```bash uv theme={null}
  uv add yfinance
  ```
</CodeGroup>

See a [usage example](/oss/python/integrations/tools/yahoo_finance_news).

```python  theme={null}
from langchain_community.tools import YahooFinanceNewsTool
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/yahoo.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt