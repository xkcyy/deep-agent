# Bookend AI

Let's load the Bookend AI Embeddings class.

```python  theme={null}
from langchain_community.embeddings import BookendEmbeddings
```

```python  theme={null}
embeddings = BookendEmbeddings(
    domain="your_domain",
    api_token="your_api_token",
    model_id="your_embeddings_model_id",
)
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = embeddings.embed_query(text)
```

```python  theme={null}
doc_result = embeddings.embed_documents([text])
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/bookend.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt