# AimlapiEmbeddings

This guide helps you get started with AI/ML API embedding models using LangChain. For detailed documentation on `AimlapiEmbeddings` features and configuration options, please refer to the [API reference](https://python.langchain.com/api_reference/aimlapi/embeddings/langchain_aimlapi.embeddings.AimlapiEmbeddings.html).

## Overview

### Integration details

| Class                                                                                                                                  | Package                                                                            | Local | JS support |                                              Downloads                                             |                                             Version                                             |
| :------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- | :---: | :--------: | :------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: |
| [AimlapiEmbeddings](https://python.langchain.com/api_reference/aimlapi/embeddings/langchain_aimlapi.embeddings.AimlapiEmbeddings.html) | [langchain-aimlapi](https://python.langchain.com/api_reference/aimlapi/index.html) |   ❌   |      ❌     | ![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain-aimlapi?style=flat-square\&label=%20) | ![PyPI - Version](https://img.shields.io/pypi/v/langchain-aimlapi?style=flat-square\&label=%20) |

## Setup

To access AI/ML API embedding models you'll need to create an account, get an API key, and install the `langchain-aimlapi` integration package.

### Credentials

Head to [aimlapi.com](https://aimlapi.com/app/?utm_source=langchain\&utm_medium=github\&utm_campaign=integration) to sign up and generate an API key. Once you've done this set the `AIMLAPI_API_KEY` environment variable:

```python  theme={null}
import getpass
import os

if not os.getenv("AIMLAPI_API_KEY"):
    os.environ["AIMLAPI_API_KEY"] = getpass.getpass("Enter your AI/ML API key: ")
```

To enable automated tracing of your model calls, set your [LangSmith](https://docs.smith.langchain.com/) API key:

```python  theme={null}
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"
```

### Installation

The LangChain AI/ML API integration lives in the `langchain-aimlapi` package:

```python  theme={null}
pip install -qU langchain-aimlapi
```

## Instantiation

Now we can instantiate our embeddings model and perform embedding operations:

```python  theme={null}
from langchain_aimlapi import AimlapiEmbeddings

embeddings = AimlapiEmbeddings(
    model="text-embedding-ada-002",
)
```

## Indexing and Retrieval

Embedding models are often used in retrieval-augmented generation (RAG) flows. Below is how to index and retrieve data using the `embeddings` object we initialized above with `InMemoryVectorStore`.

```python  theme={null}
from langchain_core.vectorstores import InMemoryVectorStore

text = "LangChain is the framework for building context-aware reasoning applications"

vectorstore = InMemoryVectorStore.from_texts(
    [text],
    embedding=embeddings,
)

retriever = vectorstore.as_retriever()

retrieved_documents = retriever.invoke("What is LangChain?")
retrieved_documents[0].page_content
```

```output  theme={null}
'LangChain is the framework for building context-aware reasoning applications'
```

## Direct usage

You can directly call `embed_query` and `embed_documents` for custom embedding scenarios.

### Embed single text

```python  theme={null}
single_vector = embeddings.embed_query(text)
print(str(single_vector)[:100])
```

### Embed multiple texts

```python  theme={null}
text2 = "LangGraph is a library for building stateful, multi-actor applications with LLMs"

vectors = embeddings.embed_documents([text, text2])
for vector in vectors:
    print(str(vector)[:100])
```

***

## API reference

For detailed documentation on `AimlapiEmbeddings` features and configuration options, please refer to the [API reference](https://python.langchain.com/api_reference/aimlapi/embeddings/langchain_aimlapi.embeddings.AimlapiEmbeddings.html).

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/aimlapi.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt