# Nuclia

> [Nuclia](https://nuclia.com) automatically indexes your unstructured data from any internal and external source, providing optimized search results and generative answers. It can handle video and audio transcription, image content extraction, and document parsing.

`Nuclia Understanding API` document transformer splits text into paragraphs and sentences, identifies entities, provides a summary of the text and generates embeddings for all the sentences.

To use the Nuclia Understanding API, you need to have a Nuclia account. You can create one for free at [https://nuclia.cloud](https://nuclia.cloud), and then [create a NUA key](https://docs.nuclia.dev/docs/docs/using/understanding/intro).

from langchain\_community.document\_transformers.nuclia\_text\_transform import NucliaTextTransformer

```python  theme={null}
pip install -qU  protobuf
pip install -qU  nucliadb-protos
```

```python  theme={null}
import os

os.environ["NUCLIA_ZONE"] = "<YOUR_ZONE>"  # e.g. europe-1
os.environ["NUCLIA_NUA_KEY"] = "<YOUR_API_KEY>"
```

To use the Nuclia document transformer, you need to instantiate a `NucliaUnderstandingAPI` tool with `enable_ml` set to `True`:

```python  theme={null}
from langchain_community.tools.nuclia import NucliaUnderstandingAPI

nua = NucliaUnderstandingAPI(enable_ml=True)
```

The Nuclia document transformer must be called in async mode, so you need to use the `atransform_documents` method:

```python  theme={null}
import asyncio

from langchain_community.document_transformers.nuclia_text_transform import (
    NucliaTextTransformer,
)
from langchain_core.documents import Document


async def process():
    documents = [
        Document(page_content="<TEXT 1>", metadata={}),
        Document(page_content="<TEXT 2>", metadata={}),
        Document(page_content="<TEXT 3>", metadata={}),
    ]
    nuclia_transformer = NucliaTextTransformer(nua)
    transformed_documents = await nuclia_transformer.atransform_documents(documents)
    print(transformed_documents)


asyncio.run(process())
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_transformers/nuclia_transformer.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt