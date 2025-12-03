# Outline

> [Outline](https://www.getoutline.com/) is an open-source collaborative knowledge base platform designed for team information sharing.

## Setup

You first need to [create an api key](https://www.getoutline.com/developers#section/Authentication) for your Outline instance. Then you need to set the following environment variables:

```python  theme={null}
import os

os.environ["OUTLINE_API_KEY"] = "xxx"
os.environ["OUTLINE_INSTANCE_URL"] = "https://app.getoutline.com"
```

## Retriever

See a [usage example](/oss/python/integrations/retrievers/outline).

```python  theme={null}
from langchain_classic.retrievers import OutlineRetriever
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/outline.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt