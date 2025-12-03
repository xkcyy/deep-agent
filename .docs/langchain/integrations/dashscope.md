# DashScope

Let's load the DashScope Embedding class.

```python  theme={null}
from langchain_community.embeddings import DashScopeEmbeddings
```

```python  theme={null}
embeddings = DashScopeEmbeddings(
    model="text-embedding-v1", dashscope_api_key="your-dashscope-api-key"
)
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = embeddings.embed_query(text)
print(query_result)
```

```python  theme={null}
doc_results = embeddings.embed_documents(["foo"])
print(doc_results)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/dashscope.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt