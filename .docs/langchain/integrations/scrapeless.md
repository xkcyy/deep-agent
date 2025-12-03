# Scrapeless

[Scrapeless](https://scrapeless.com) offers flexible and feature-rich data acquisition services with extensive parameter customization and multi-format export support.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-scrapeless
  ```

  ```bash uv theme={null}
  uv add langchain-scrapeless
  ```
</CodeGroup>

You'll need to set up your Scrapeless API key:

```python  theme={null}
import os
os.environ["SCRAPELESS_API_KEY"] = "your-api-key"
```

## Tools

The Scrapeless integration provides several tools:

* [ScrapelessDeepSerpGoogleSearchTool](/oss/python/integrations/tools/scrapeless_scraping_api) - Enables comprehensive extraction of Google SERP data across all result types.
* [ScrapelessDeepSerpGoogleTrendsTool](/oss/python/integrations/tools/scrapeless_scraping_api) - Retrieves keyword trend data from Google, including popularity over time, regional interest, and related searches.
* [ScrapelessUniversalScrapingTool](/oss/python/integrations/tools/scrapeless_universal_scraping) - Access and extract data from JS-Render websites that typically block bots.
* [ScrapelessCrawlerCrawlTool](/oss/python/integrations/tools/scrapeless_crawl) - Crawl a website and its linked pages to extract comprehensive data.
* [ScrapelessCrawlerScrapeTool](/oss/python/integrations/tools/scrapeless_crawl) - Extract information from a single webpage.

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/scrapeless.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt