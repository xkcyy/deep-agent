# Concurrent Loader

Works just like the GenericLoader but concurrently for those who choose to optimize their workflow.

```python  theme={null}
from langchain_community.document_loaders import ConcurrentLoader
```

```python  theme={null}
loader = ConcurrentLoader.from_filesystem("example_data/", glob="**/*.txt")
```

```python  theme={null}
files = loader.load()
```

```python  theme={null}
len(files)
```

```output  theme={null}
2
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/concurrent.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt