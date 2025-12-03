# Gutenberg

> [Project Gutenberg](https://www.gutenberg.org/about/) is an online library of free eBooks.

This notebook covers how to load links to `Gutenberg` e-books into a document format that we can use downstream.

```python  theme={null}
from langchain_community.document_loaders import GutenbergLoader
```

```python  theme={null}
loader = GutenbergLoader("https://www.gutenberg.org/cache/epub/69972/pg69972.txt")
```

```python  theme={null}
data = loader.load()
```

```python  theme={null}
data[0].page_content[:300]
```

```output  theme={null}
'The Project Gutenberg eBook of The changed brides, by Emma Dorothy\r\n\n\nEliza Nevitte Southworth\r\n\n\n\r\n\n\nThis eBook is for the use of anyone anywhere in the United States and\r\n\n\nmost other parts of the world at no cost and with almost no restrictions\r\n\n\nwhatsoever. You may copy it, give it away or re-u'
```

```python  theme={null}
data[0].metadata
```

```output  theme={null}
{'source': 'https://www.gutenberg.org/cache/epub/69972/pg69972.txt'}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/gutenberg.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt