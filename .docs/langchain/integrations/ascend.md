# Ascend

```python  theme={null}
from langchain_community.embeddings import AscendEmbeddings

model = AscendEmbeddings(
    model_path="/root/.cache/modelscope/hub/yangjhchs/acge_text_embedding",
    device_id=0,
    query_instruction="Represend this sentence for searching relevant passages: ",
)
emb = model.embed_query("hellow")
print(emb)
```

```output  theme={null}
[-0.04053403 -0.05560051 -0.04385472 ...  0.09371872  0.02846981
 -0.00576814]
```

```python  theme={null}
doc_embs = model.embed_documents(
    ["This is a content of the document", "This is another document"]
)
print(doc_embs)
```

```output  theme={null}
We strongly recommend passing in an `attention_mask` since your input_ids may be padded. See https://huggingface.co/docs/transformers/troubleshooting#incorrect-output-when-padding-tokens-arent-masked.
```

```output  theme={null}
[[-0.00348254  0.03098977 -0.00203087 ...  0.08492374  0.03970494
  -0.03372753]
 [-0.02198593 -0.01601127  0.00215684 ...  0.06065163  0.00126425
  -0.03634358]]
```

```python  theme={null}
model.aembed_query("hellow")
```

```output  theme={null}
<coroutine object Embeddings.aembed_query at 0x7f9fac699cb0>
```

```python  theme={null}
await model.aembed_query("hellow")
```

```output  theme={null}
array([-0.04053403, -0.05560051, -0.04385472, ...,  0.09371872,
                0.02846981, -0.00576814], dtype=float32)
```

```python  theme={null}
model.aembed_documents(
    ["This is a content of the document", "This is another document"]
)
```

```output  theme={null}
<coroutine object Embeddings.aembed_documents at 0x7fa093ff1a80>
```

```python  theme={null}
await model.aembed_documents(
    ["This is a content of the document", "This is another document"]
)
```

```output  theme={null}
array([[-0.00348254,  0.03098977, -0.00203087, ...,  0.08492374,
         0.03970494, -0.03372753],
       [-0.02198593, -0.01601127,  0.00215684, ...,  0.06065163,
         0.00126425, -0.03634358]], dtype=float32)
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/ascend.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt