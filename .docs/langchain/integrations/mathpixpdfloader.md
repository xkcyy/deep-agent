# MathPixPDFLoader

Inspired by Daniel Gross's snippet here: [https://gist.github.com/danielgross/3ab4104e14faccc12b49200843adab21](https://gist.github.com/danielgross/3ab4104e14faccc12b49200843adab21)

## Overview

### Integration details

| Class                                                                                                                                                    | Package                                                                                | Local | Serializable | JS support |
| :------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :---: | :----------: | :--------: |
| [MathPixPDFLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.MathpixPDFLoader.html) | [langchain-community](https://python.langchain.com/api_reference/community/index.html) |   ✅   |       ❌      |      ❌     |

### Loader features

|      Source      | Document Lazy Loading | Native Async Support |
| :--------------: | :-------------------: | :------------------: |
| MathPixPDFLoader |           ✅           |           ❌          |

## Setup

### Credentials

Sign up for Mathpix and [create an API key](https://mathpix.com/docs/ocr/creating-an-api-key) to set the `MATHPIX_API_KEY` variables in your environment

```python  theme={null}
import getpass
import os

if "MATHPIX_API_KEY" not in os.environ:
    os.environ["MATHPIX_API_KEY"] = getpass.getpass("Enter your Mathpix API key: ")
```

To enable automated tracing of your model calls, set your [LangSmith](https://docs.smith.langchain.com/) API key:

```python  theme={null}
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"
```

### Installation

Install **langchain-community**.

```python  theme={null}
pip install -qU langchain-community
```

## Initialization

Now we are ready to initialize our loader:

```python  theme={null}
from langchain_community.document_loaders import MathpixPDFLoader

file_path = "./example_data/layout-parser-paper.pdf"
loader = MathpixPDFLoader(file_path)
```

## Load

```python  theme={null}
docs = loader.load()
docs[0]
```

```python  theme={null}
print(docs[0].metadata)
```

## Lazy Load

```python  theme={null}
page = []
for doc in loader.lazy_load():
    page.append(doc)
    if len(page) >= 10:
        # do some paged operation, e.g.
        # index.upsert(page)

        page = []
```

***

## API reference

For detailed documentation of all MathpixPDFLoader features and configurations head to the API reference: [python.langchain.com/api\_reference/community/document\_loaders/langchain\_community.document\_loaders.pdf.MathpixPDFLoader.html](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.MathpixPDFLoader.html)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/mathpix.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt