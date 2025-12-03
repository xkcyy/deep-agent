# BGE on Hugging Face

> [BGE models on the HuggingFace](https://huggingface.co/BAAI/bge-large-en-v1.5) are one of [the best open-source embedding models](https://huggingface.co/spaces/mteb/leaderboard).
> BGE model is created by the [Beijing Academy of Artificial Intelligence (BAAI)](https://en.wikipedia.org/wiki/Beijing_Academy_of_Artificial_Intelligence). `BAAI` is a private non-profit organization engaged in AI research and development.

This notebook shows how to use `BGE Embeddings` through `Hugging Face`

```python  theme={null}
pip install -qU  sentence_transformers
```

```python  theme={null}
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

model_name = "BAAI/bge-small-en"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
hf = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)
```

Note that you need to pass `query_instruction=""` for `model_name="BAAI/bge-m3"` see [FAQ BGE M3](https://huggingface.co/BAAI/bge-m3#faq).

```python  theme={null}
embedding = hf.embed_query("hi this is harrison")
len(embedding)
```

```output  theme={null}
384
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/bge_huggingface.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt