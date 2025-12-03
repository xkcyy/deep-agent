# LocalAI Embeddings

<Info>
  **`langchain-localai` is a 3rd party integration package for LocalAI. It provides a simple way to use LocalAI services in LangChain.**

  The source code is available on [Github](https://github.com/mkhludnev/langchain-localai)
</Info>

Let's load the LocalAI Embedding class. In order to use the LocalAI Embedding class, you need to have the LocalAI service hosted somewhere and configure the embedding models. See the documentation at [localai.io/basics/getting\_started/index.html](https://localai.io/basics/getting_started/index.html) and [localai.io/features/embeddings/index.html](https://localai.io/features/embeddings/index.html).

```python  theme={null}
pip install -U langchain-localai
```

```python  theme={null}
from langchain_localai import LocalAIEmbeddings
```

```python  theme={null}
embeddings = LocalAIEmbeddings(
    openai_api_base="http://localhost:8080", model="embedding-model-name"
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

Let's load the LocalAI Embedding class with first generation models (e.g. text-search-ada-doc-001/text-search-ada-query-001). Note: These are not recommended models - see [here](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

```python  theme={null}
from langchain_community.embeddings import LocalAIEmbeddings
```

```python  theme={null}
embeddings = LocalAIEmbeddings(
    openai_api_base="http://localhost:8080", model="embedding-model-name"
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

```python  theme={null}
import os

# if you are behind an explicit proxy, you can use the OPENAI_PROXY environment variable to pass through
os.environ["OPENAI_PROXY"] = "http://proxy.yourcompany.com:8080"
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/localai.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt