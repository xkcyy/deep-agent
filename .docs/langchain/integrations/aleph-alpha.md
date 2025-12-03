# Aleph Alpha

There are two possible ways to use Aleph Alpha's semantic embeddings. If you have texts with a dissimilar structure (e.g. a Document and a Query) you would want to use asymmetric embeddings. Conversely, for texts with comparable structures, symmetric embeddings are the suggested approach.

## Asymmetric

```python  theme={null}
from langchain_community.embeddings import AlephAlphaAsymmetricSemanticEmbedding
```

```python  theme={null}
document = "This is a content of the document"
query = "What is the content of the document?"
```

```python  theme={null}
embeddings = AlephAlphaAsymmetricSemanticEmbedding(normalize=True, compress_to_size=128)
```

```python  theme={null}
doc_result = embeddings.embed_documents([document])
```

```python  theme={null}
query_result = embeddings.embed_query(query)
```

## Symmetric

```python  theme={null}
from langchain_community.embeddings import AlephAlphaSymmetricSemanticEmbedding
```

```python  theme={null}
text = "This is a test text"
```

```python  theme={null}
embeddings = AlephAlphaSymmetricSemanticEmbedding(normalize=True, compress_to_size=128)
```

```python  theme={null}
doc_result = embeddings.embed_documents([text])
```

```python  theme={null}
query_result = embeddings.embed_query(text)
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/aleph_alpha.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt