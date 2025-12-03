# NucliaDB

You can use a local NucliaDB instance or use [Nuclia Cloud](https://nuclia.cloud).

When using a local instance, you need a Nuclia Understanding API key, so your texts are properly vectorized and indexed. You can get a key by creating a free account at [https://nuclia.cloud](https://nuclia.cloud), and then [create a NUA key](https://docs.nuclia.dev/docs/docs/using/understanding/intro).

```python  theme={null}
pip install -qU  langchain langchain-community nuclia
```

## Usage with nuclia.cloud

```python  theme={null}
from langchain_community.vectorstores.nucliadb import NucliaDB

API_KEY = "YOUR_API_KEY"

ndb = NucliaDB(knowledge_box="YOUR_KB_ID", local=False, api_key=API_KEY)
```

## Usage with a local instance

Note: By default `backend` is set to `http://localhost:8080`.

```python  theme={null}
from langchain_community.vectorstores.nucliadb import NucliaDB

ndb = NucliaDB(knowledge_box="YOUR_KB_ID", local=True, backend="http://my-local-server")
```

## Add and delete texts to your Knowledge Box

```python  theme={null}
ids = ndb.add_texts(["This is a new test", "This is a second test"])
```

```python  theme={null}
ndb.delete(ids=ids)
```

## Search in your Knowledge Box

```python  theme={null}
results = ndb.similarity_search("Who was inspired by Ada Lovelace?")
print(results[0].page_content)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/vectorstores/nucliadb.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt