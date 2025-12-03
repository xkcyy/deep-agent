# Outline Document Loader

> [Outline](https://www.getoutline.com/) is an open-source collaborative knowledge base platform designed for team information sharing.

This notebook shows how to obtain langchain Documents from your Outline collections.

## Overview

The [Outline Document Loader](https://github.com/10Pines/langchain-outline) can be used to load Outline collections as LangChain Documents for integration into Retrieval-Augmented Generation (RAG) workflows.

This example demonstrates:

* Setting up a Document Loader to load all documents from an Outline instance.

### Setup

Before starting, ensure you have the following environment variables set:

* OUTLINE\_API\_KEY: Your API key for authenticating with your Outline instance ([www.getoutline.com/developers#section/Authentication](https://www.getoutline.com/developers#section/Authentication)).
* OUTLINE\_INSTANCE\_URL: The URL (including protocol) of your Outline instance.

```python  theme={null}
import os

os.environ["OUTLINE_API_KEY"] = "ol_api_xyz123"
os.environ["OUTLINE_INSTANCE_URL"] = "https://app.getoutline.com"
```

## Initialization

To initialize the OutlineLoader, you need the following parameters:

* outline\_base\_url: The URL of your outline instance (or it will be taken from the environment variable).
* outline\_api\_key: Your API key for authenticating with your Outline instance (or it will be taken from the environment variable).
* outline\_collection\_id\_list: List of collection ids to be retrieved. If None all will be retrieved.
* page\_size: Because the Outline API uses paginated results you can configure how many results (documents) per page will be retrieved per API request.  If this is not specified a default will be used.

## Instantiation

```python  theme={null}
# Option 1: Using environment variables (ensure they are set)
from langchain_outline.document_loaders.outline import OutlineLoader

loader = OutlineLoader()

# Option 2: Passing parameters directly
loader = OutlineLoader(
    outline_base_url="YOUR_OUTLINE_URL", outline_api_key="YOUR_API_KEY"
)
```

## Load

To load and return all documents available in the Outline instance

```python  theme={null}
loader.load()
```

## Lazy Load

The lazy\_load method allows you to iteratively load documents from the Outline collection, yielding each document as it is fetched:

```python  theme={null}
loader.lazy_load()
```

***

## API reference

For detailed documentation of all `Outline` features and configurations head to the API reference: [www.getoutline.com/developers](https://www.getoutline.com/developers)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/outline.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt