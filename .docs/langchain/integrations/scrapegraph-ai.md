# ScrapeGraph AI

> [ScrapeGraph AI](https://scrapegraphai.com) is a service that provides AI-powered web scraping capabilities.
> It offers tools for extracting structured data, converting webpages to markdown, and processing local HTML content
> using natural language prompts.

## Installation and Setup

Install the required packages:

<CodeGroup>
  ```bash pip theme={null}
  pip install langchain-scrapegraph
  ```

  ```bash uv theme={null}
  uv add langchain-scrapegraph
  ```
</CodeGroup>

Set up your API key:

```bash  theme={null}
export SGAI_API_KEY="your-scrapegraph-api-key"
```

## Tools

See a [usage example](/oss/python/integrations/tools/scrapegraph).

There are four tools available:

```python  theme={null}
from langchain_scrapegraph.tools import (
    SmartScraperTool,    # Extract structured data from websites
    SmartCrawlerTool,    # Extract data from multiple pages with crawling
    MarkdownifyTool,     # Convert webpages to markdown
    AgenticScraperTool,  # Extract specifying steps
    GetCreditsTool,      # Check remaining API credits
)
```

Each tool serves a specific purpose:

* `SmartScraperTool`: Extract structured data from websites given a URL, prompt and optional output schema
* `SmartCrawlerTool`: Extract data from multiple pages with advanced crawling options like depth control, page limits, and domain restrictions
* `MarkdownifyTool`: Convert any webpage to clean markdown format
* `AgenticScraperTool`: Extract specifying steps
* `GetCreditsTool`: Check your remaining ScrapeGraph AI credits

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/scrapegraph.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt