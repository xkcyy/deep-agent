# FakeEmbeddings

LangChain also provides a fake embedding class. You can use this to test your pipelines.

```python  theme={null}
from langchain_community.embeddings import FakeEmbeddings
```

```python  theme={null}
embeddings = FakeEmbeddings(size=1352)
```

```python  theme={null}
query_result = embeddings.embed_query("foo")
```

```python  theme={null}
doc_results = embeddings.embed_documents(["foo"])
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/fake.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt