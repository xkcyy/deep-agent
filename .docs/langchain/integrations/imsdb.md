# IMSDb

> [IMSDb](https://imsdb.com/) is the `Internet Movie Script Database`.

This covers how to load `IMSDb` webpages into a document format that we can use downstream.

```python  theme={null}
from langchain_community.document_loaders import IMSDbLoader
```

```python  theme={null}
loader = IMSDbLoader("https://imsdb.com/scripts/BlacKkKlansman.html")
```

```python  theme={null}
data = loader.load()
```

```python  theme={null}
data[0].page_content[:500]
```

```output  theme={null}
'\n\r\n\r\n\r\n\r\n                                    BLACKKKLANSMAN\r\n                         \r\n                         \r\n                         \r\n                         \r\n                                      Written by\r\n\r\n                          Charlie Wachtel & David Rabinowitz\r\n\r\n                                         and\r\n\r\n                              Kevin Willmott & Spike Lee\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n                         FADE IN:\r\n                         \r\n          SCENE FROM "GONE WITH'
```

```python  theme={null}
data[0].metadata
```

```output  theme={null}
{'source': 'https://imsdb.com/scripts/BlacKkKlansman.html'}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/imsdb.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt