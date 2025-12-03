# BSHTMLLoader

This guide provides a quick overview for getting started with BeautifulSoup4 [document loader](https://python.langchain.com/docs/concepts/document_loaders). For detailed documentation of all \_\_ModuleName\_\_Loader features and configurations head to the [API reference](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html).

## Overview

### Integration details

| Class                                                                                                                                                | Package                                                                                | Local | Serializable | JS support |
| :--------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :---: | :----------: | :--------: |
| [BSHTMLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html) | [langchain-community](https://python.langchain.com/api_reference/community/index.html) |   ✅   |       ❌      |      ❌     |

### Loader features

|    Source    | Document Lazy Loading | Native Async Support |
| :----------: | :-------------------: | :------------------: |
| BSHTMLLoader |           ✅           |           ❌          |

## Setup

To access BSHTMLLoader document loader you'll need to install the `langchain-community` integration package and the `bs4` python package.

### Credentials

No credentials are needed to use the `BSHTMLLoader` class.

To enable automated tracing of your model calls, set your [LangSmith](https://docs.smith.langchain.com/) API key:

```python  theme={null}
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"
```

### Installation

Install **langchain-community** and **bs4**.

```python  theme={null}
pip install -qU langchain-community bs4
```

## Initialization

Now we can instantiate our model object and load documents:

* TODO: Update model instantiation with relevant params.

```python  theme={null}
from langchain_community.document_loaders import BSHTMLLoader

loader = BSHTMLLoader(
    file_path="./example_data/fake-content.html",
)
```

## Load

```python  theme={null}
docs = loader.load()
docs[0]
```

```output  theme={null}
Document(metadata={'source': './example_data/fake-content.html', 'title': 'Test Title'}, page_content='\nTest Title\n\n\nMy First Heading\nMy first paragraph.\n\n\n')
```

```python  theme={null}
print(docs[0].metadata)
```

```output  theme={null}
{'source': './example_data/fake-content.html', 'title': 'Test Title'}
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
page[0]
```

```output  theme={null}
Document(metadata={'source': './example_data/fake-content.html', 'title': 'Test Title'}, page_content='\nTest Title\n\n\nMy First Heading\nMy first paragraph.\n\n\n')
```

## Adding separator to BS4

We can also pass a separator to use when calling get\_text on the soup

```python  theme={null}
loader = BSHTMLLoader(
    file_path="./example_data/fake-content.html", get_text_separator=", "
)

docs = loader.load()
print(docs[0])
```

```output  theme={null}
page_content='
, Test Title,
,
,
, My First Heading,
, My first paragraph.,
,
,
' metadata={'source': './example_data/fake-content.html', 'title': 'Test Title'}
```

***

## API reference

For detailed documentation of all BSHTMLLoader features and configurations head to the API reference: [python.langchain.com/api\_reference/community/document\_loaders/langchain\_community.document\_loaders.html\_bs.BSHTMLLoader.html](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/bshtml.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt