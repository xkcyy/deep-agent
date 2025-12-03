# DeepInfra

[DeepInfra](https://deepinfra.com/?utm_source=langchain) is a serverless inference as a service that provides access to a [variety of LLMs](https://deepinfra.com/models?utm_source=langchain) and [embeddings models](https://deepinfra.com/models?type=embeddings\&utm_source=langchain). This notebook goes over how to use LangChain with DeepInfra for text embeddings.

```python  theme={null}
# sign up for an account: https://deepinfra.com/login?utm_source=langchain

from getpass import getpass

DEEPINFRA_API_TOKEN = getpass()
```

```output  theme={null}
 ········
```

```python  theme={null}
import os

os.environ["DEEPINFRA_API_TOKEN"] = DEEPINFRA_API_TOKEN
```

```python  theme={null}
from langchain_community.embeddings import DeepInfraEmbeddings
```

```python  theme={null}
embeddings = DeepInfraEmbeddings(
    model_id="sentence-transformers/clip-ViT-B-32",
    query_instruction="",
    embed_instruction="",
)
```

```python  theme={null}
docs = ["Dog is not a cat", "Beta is the second letter of Greek alphabet"]
document_result = embeddings.embed_documents(docs)
```

```python  theme={null}
query = "What is the first letter of Greek alphabet"
query_result = embeddings.embed_query(query)
```

```python  theme={null}
import numpy as np

query_numpy = np.array(query_result)
for doc_res, doc in zip(document_result, docs):
    document_numpy = np.array(doc_res)
    similarity = np.dot(query_numpy, document_numpy) / (
        np.linalg.norm(query_numpy) * np.linalg.norm(document_numpy)
    )
    print(f'Cosine similarity between "{doc}" and query: {similarity}')
```

```output  theme={null}
Cosine similarity between "Dog is not a cat" and query: 0.7489097144129355
Cosine similarity between "Beta is the second letter of Greek alphabet" and query: 0.9519380640702013
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/deepinfra.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt