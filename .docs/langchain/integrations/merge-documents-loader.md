# Merge Documents Loader

Merge the documents returned from a set of specified data loaders.

```python  theme={null}
from langchain_community.document_loaders import WebBaseLoader

loader_web = WebBaseLoader(
    "https://github.com/basecamp/handbook/blob/master/37signals-is-you.md"
)
```

```python  theme={null}
from langchain_community.document_loaders import PyPDFLoader

loader_pdf = PyPDFLoader("../MachineLearning-Lecture01.pdf")
```

```python  theme={null}
from langchain_community.document_loaders.merge import MergedDataLoader

loader_all = MergedDataLoader(loaders=[loader_web, loader_pdf])
```

```python  theme={null}
docs_all = loader_all.load()
```

```python  theme={null}
len(docs_all)
```

```output  theme={null}
23
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/merge_doc.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt