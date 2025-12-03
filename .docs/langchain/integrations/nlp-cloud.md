# NLP Cloud

> [NLP Cloud](https://docs.nlpcloud.com/#introduction) is an artificial intelligence platform that allows you to use the most advanced AI engines, and even train your own engines with your own data.

The [embeddings](https://docs.nlpcloud.com/#embeddings) endpoint offers the following model:

* `paraphrase-multilingual-mpnet-base-v2`: Paraphrase Multilingual MPNet Base V2 is a very fast model based on Sentence Transformers that is perfectly suited for embeddings extraction in more than 50 languages (see the full list here).

```python  theme={null}
pip install -qU  nlpcloud
```

```python  theme={null}
from langchain_community.embeddings import NLPCloudEmbeddings
```

```python  theme={null}
import os

os.environ["NLPCLOUD_API_KEY"] = "xxx"
nlpcloud_embd = NLPCloudEmbeddings()
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = nlpcloud_embd.embed_query(text)
```

```python  theme={null}
doc_result = nlpcloud_embd.embed_documents([text])
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/nlp_cloud.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt