# Copy Paste

This notebook covers how to load a document object from something you just want to copy and paste. In this case, you don't even need to use a DocumentLoader, but rather can just construct the Document directly.

```python  theme={null}
from langchain_core.documents import Document
```

```python  theme={null}
text = "..... put the text you copy pasted here......"
```

```python  theme={null}
doc = Document(page_content=text)
```

## Metadata

If you want to add metadata about the where you got this piece of text, you easily can with the metadata key.

```python  theme={null}
metadata = {"source": "internet", "date": "Friday"}
```

```python  theme={null}
doc = Document(page_content=text, metadata=metadata)
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/copypaste.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt