# Model2Vec

Model2Vec is a technique to turn any sentence transformer into a really small static model
[model2vec](https://github.com/MinishLab/model2vec) can be used to generate embeddings.

## Setup

```bash  theme={null}
pip install -U langchain-community
```

## Instantiation

Ensure that `model2vec` is installed

```bash  theme={null}
pip install -U model2vec
```

## Indexing and Retrieval

```python  theme={null}
from langchain_community.embeddings import Model2vecEmbeddings
```

```python  theme={null}
embeddings = Model2vecEmbeddings("minishlab/potion-base-8M")
```

```python  theme={null}
query_text = "This is a test query."
query_result = embeddings.embed_query(query_text)
```

```python  theme={null}
document_text = "This is a test document."
document_result = embeddings.embed_documents([document_text])
```

## Direct Usage

Here's how you would directly make use of `model2vec`

```python  theme={null}
from model2vec import StaticModel

# Load a model from the HuggingFace hub (in this case the potion-base-8M model)
model = StaticModel.from_pretrained("minishlab/potion-base-8M")

# Make embeddings
embeddings = model.encode(["It's dangerous to go alone!", "It's a secret to everybody."])

# Make sequences of token embeddings
token_embeddings = model.encode_as_sequence(["It's dangerous to go alone!", "It's a secret to everybody."])
```

***

## API reference

For more information check out the model2vec github [repo](https://github.com/MinishLab/model2vec)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/model2vec.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt