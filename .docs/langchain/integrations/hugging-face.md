# Hugging Face

Let's load the Hugging Face Embedding class.

```python  theme={null}
pip install -qU  langchain langchain-huggingface sentence_transformers
```

```python  theme={null}
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
```

```python  theme={null}
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = embeddings.embed_query(text)
```

```python  theme={null}
query_result[:3]
```

```output  theme={null}
[-0.04895168915390968, -0.03986193612217903, -0.021562768146395683]
```

```python  theme={null}
doc_result = embeddings.embed_documents([text])
```

## Hugging Face Inference Providers

We can also access embedding models via the [Inference Providers](https://huggingface.co/docs/inference-providers), which let's us use open source models on scalable serverless infrastructure.

First, we need to get a read-only API key from [Hugging Face](https://huggingface.co/settings/tokens).

```python  theme={null}
from getpass import getpass

huggingfacehub_api_token = getpass()
```

Now we can use the `HuggingFaceInferenceAPIEmbeddings` class to run open source embedding models via [Inference Providers](https://huggingface.co/docs/inference-providers).

```python  theme={null}
from langchain_huggingface import HuggingFaceInferenceAPIEmbeddings

embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=huggingfacehub_api_token,
    model_name="sentence-transformers/all-MiniLM-l6-v2",
)

query_result = embeddings.embed_query(text)
query_result[:3]
```

```output  theme={null}
[-0.038338541984558105, 0.1234646737575531, -0.028642963618040085]
```

## Hugging Face Hub

We can also generate embeddings locally via the Hugging Face Hub package, which requires us to install `huggingface_hub`

```python  theme={null}
!pip install huggingface_hub
```

```python  theme={null}
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
```

```python  theme={null}
embeddings = HuggingFaceEndpointEmbeddings()
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = embeddings.embed_query(text)
```

```python  theme={null}
query_result[:3]
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/huggingfacehub.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt