# TensorFlow Hub

> [TensorFlow Hub](https://www.tensorflow.org/hub) is a repository of trained machine learning models ready for fine-tuning and deployable anywhere. Reuse trained models like `BERT` and `Faster R-CNN` with just a few lines of code.

Let's load the TensorflowHub Embedding class.

```python  theme={null}
from langchain_community.embeddings import TensorflowHubEmbeddings
```

```python  theme={null}
embeddings = TensorflowHubEmbeddings()
```

```output  theme={null}
2023-01-30 23:53:01.652176: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-01-30 23:53:34.362802: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = embeddings.embed_query(text)
```

```python  theme={null}
doc_results = embeddings.embed_documents(["foo"])
```

```python  theme={null}
doc_results
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/tensorflowhub.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt