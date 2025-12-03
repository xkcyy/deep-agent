# Elasticsearch

Walkthrough of how to generate embeddings using a hosted embedding model in Elasticsearch

The easiest way to instantiate the `ElasticsearchEmbeddings` class it either

* using the `from_credentials` constructor if you are using Elastic Cloud
* or using the `from_es_connection` constructor with any Elasticsearch cluster

```python  theme={null}
!pip -q install langchain-elasticsearch
```

```python  theme={null}
from langchain_elasticsearch import ElasticsearchEmbeddings
```

```python  theme={null}
# Define the model ID
model_id = "your_model_id"
```

## Testing with `from_credentials`

This required an Elastic Cloud `cloud_id`

```python  theme={null}
# Instantiate ElasticsearchEmbeddings using credentials
embeddings = ElasticsearchEmbeddings.from_credentials(
    model_id,
    es_cloud_id="your_cloud_id",
    es_user="your_user",
    es_password="your_password",
)
```

```python  theme={null}
# Create embeddings for multiple documents
documents = [
    "This is an example document.",
    "Another example document to generate embeddings for.",
]
document_embeddings = embeddings.embed_documents(documents)
```

```python  theme={null}
# Print document embeddings
for i, embedding in enumerate(document_embeddings):
    print(f"Embedding for document {i + 1}: {embedding}")
```

```python  theme={null}
# Create an embedding for a single query
query = "This is a single query."
query_embedding = embeddings.embed_query(query)
```

```python  theme={null}
# Print query embedding
print(f"Embedding for query: {query_embedding}")
```

## Testing with Existing Elasticsearch client connection

This can be used with any Elasticsearch deployment

```python  theme={null}
# Create Elasticsearch connection
from elasticsearch import Elasticsearch

es_connection = Elasticsearch(
    hosts=["https://es_cluster_url:port"], basic_auth=("user", "password")
)
```

```python  theme={null}
# Instantiate ElasticsearchEmbeddings using es_connection
embeddings = ElasticsearchEmbeddings.from_es_connection(
    model_id,
    es_connection,
)
```

```python  theme={null}
# Create embeddings for multiple documents
documents = [
    "This is an example document.",
    "Another example document to generate embeddings for.",
]
document_embeddings = embeddings.embed_documents(documents)
```

```python  theme={null}
# Print document embeddings
for i, embedding in enumerate(document_embeddings):
    print(f"Embedding for document {i + 1}: {embedding}")
```

```python  theme={null}
# Create an embedding for a single query
query = "This is a single query."
query_embedding = embeddings.embed_query(query)
```

```python  theme={null}
# Print query embedding
print(f"Embedding for query: {query_embedding}")
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/elasticsearch.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt