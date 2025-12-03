# Jina

You can check the list of available models from [here](https://jina.ai/embeddings/).

## Installation and setup

Install requirements

```python  theme={null}
pip install -U langchain-community
```

Import libraries

```python  theme={null}
import requests
from langchain_community.embeddings import JinaEmbeddings
from numpy import dot
from numpy.linalg import norm
from PIL import Image
```

## Embed text and queries with Jina embedding models through JinaAI API

```python  theme={null}
text_embeddings = JinaEmbeddings(
    jina_api_key="jina_*", model_name="jina-embeddings-v2-base-en"
)
```

```python  theme={null}
text = "This is a test document."
```

```python  theme={null}
query_result = text_embeddings.embed_query(text)
```

```python  theme={null}
print(query_result)
```

```python  theme={null}
doc_result = text_embeddings.embed_documents([text])
```

```python  theme={null}
print(doc_result)
```

## Embed images and queries with Jina CLIP through JinaAI API

```python  theme={null}
multimodal_embeddings = JinaEmbeddings(jina_api_key="jina_*", model_name="jina-clip-v1")
```

```python  theme={null}
image = "https://avatars.githubusercontent.com/u/126733545?v=4"

description = "Logo of a parrot and a chain on green background"

im = Image.open(requests.get(image, stream=True).raw)
print("Image:")
display(im)
```

```python  theme={null}
image_result = multimodal_embeddings.embed_images([image])
```

```python  theme={null}
print(image_result)
```

```python  theme={null}
description_result = multimodal_embeddings.embed_documents([description])
```

```python  theme={null}
print(description_result)
```

```python  theme={null}
cosine_similarity = dot(image_result[0], description_result[0]) / (
    norm(image_result[0]) * norm(description_result[0])
)
```

```python  theme={null}
print(cosine_similarity)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/jina.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt