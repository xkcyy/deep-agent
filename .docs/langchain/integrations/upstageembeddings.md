# UpstageEmbeddings

This notebook covers how to get started with Upstage embedding models.

## Installation

Install `langchain-upstage` package.

```bash  theme={null}
pip install -U langchain-upstage
```

## Environment Setup

Make sure to set the following environment variables:

* `UPSTAGE_API_KEY`: Your Upstage API key from [Upstage console](https://console.upstage.ai/).

```python  theme={null}
import os

os.environ["UPSTAGE_API_KEY"] = "YOUR_API_KEY"
```

## Usage

Initialize `UpstageEmbeddings` class.

```python  theme={null}
from langchain_upstage import UpstageEmbeddings

embeddings = UpstageEmbeddings(model="solar-embedding-1-large")
```

Use `embed_documents` to embed list of texts or documents.

```python  theme={null}
doc_result = embeddings.embed_documents(
    ["Sung is a professor.", "This is another document"]
)
print(doc_result)
```

Use `embed_query` to embed query string.

```python  theme={null}
query_result = embeddings.embed_query("What does Sung do?")
print(query_result)
```

Use `aembed_documents` and `aembed_query` for async operations.

```python  theme={null}
# async embed query
await embeddings.aembed_query("My query to look up")
```

```python  theme={null}
# async embed documents
await embeddings.aembed_documents(
    ["This is a content of the document", "This is another document"]
)
```

## Using with vector store

You can use `UpstageEmbeddings` with vector store component. The following demonstrates a simple example.

```python  theme={null}
from langchain_community.vectorstores import DocArrayInMemorySearch

vectorstore = DocArrayInMemorySearch.from_texts(
    ["harrison worked at kensho", "bears like to eat honey"],
    embedding=UpstageEmbeddings(model="solar-embedding-1-large"),
)
retriever = vectorstore.as_retriever()
docs = retriever.invoke("Where did Harrison work?")
print(docs)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/upstage.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt