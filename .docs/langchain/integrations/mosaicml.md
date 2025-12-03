# MosaicML

> [MosaicML](https://docs.mosaicml.com/en/latest/inference.html) offers a managed inference service. You can either use a variety of open-source models, or deploy your own.

This example goes over how to use LangChain to interact with `MosaicML` Inference for text embedding.

```python  theme={null}
# sign up for an account: https://forms.mosaicml.com/demo?utm_source=langchain

from getpass import getpass

MOSAICML_API_TOKEN = getpass()
```

```python  theme={null}
import os

os.environ["MOSAICML_API_TOKEN"] = MOSAICML_API_TOKEN
```

```python  theme={null}
from langchain_community.embeddings import MosaicMLInstructorEmbeddings
```

```python  theme={null}
embeddings = MosaicMLInstructorEmbeddings(
    query_instruction="Represent the query for retrieval: "
)
```

```python  theme={null}
query_text = "This is a test query."
query_result = embeddings.embed_query(query_text)
```

```python  theme={null}
document_text = "This is a test document."
document_result = embeddings.embed_documents([document_text])
```

```python  theme={null}
import numpy as np

query_numpy = np.array(query_result)
document_numpy = np.array(document_result[0])
similarity = np.dot(query_numpy, document_numpy) / (
    np.linalg.norm(query_numpy) * np.linalg.norm(document_numpy)
)
print(f"Cosine similarity between document and query: {similarity}")
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/mosaicml.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt