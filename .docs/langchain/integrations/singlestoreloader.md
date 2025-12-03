# SingleStoreLoader

The `SingleStoreLoader` allows you to load documents directly from a SingleStore database table. It is part of the `langchain-singlestore` integration package.

## Overview

### Integration Details

| Class               | Package                 | JS Support |
| :------------------ | :---------------------- | :--------: |
| `SingleStoreLoader` | `langchain_singlestore` |      ❌     |

### Features

* Load documents lazily to handle large datasets efficiently.
* Supports native asynchronous operations.
* Easily configurable to work with different database schemas.

## Setup

To use the `SingleStoreLoader`, you need to install the `langchain-singlestore` package. Follow the installation instructions below.

### Installation

Install **langchain\_singlestore**.

```python  theme={null}
pip install -qU langchain_singlestore
```

## Initialization

To initialize `SingleStoreLoader`, you need to provide connection parameters for the SingleStore database and specify the table and fields to load documents from.

### Required Parameters

* **host** (`str`): Hostname, IP address, or URL for the database.
* **table\_name** (`str`): Name of the table to query. Defaults to `embeddings`.
* **content\_field** (`str`): Field containing document content. Defaults to `content`.
* **metadata\_field** (`str`): Field containing document metadata. Defaults to `metadata`.

### Optional Parameters

* **id\_field** (`str`): Field containing document IDs. Defaults to `id`.

### Connection Pool Parameters

* **pool\_size** (`int`): Number of active connections in the pool. Defaults to `5`.
* **max\_overflow** (`int`): Maximum connections beyond `pool_size`. Defaults to `10`.
* **timeout** (`float`): Connection timeout in seconds. Defaults to `30`.

### Additional Options

* **pure\_python** (`bool`): Enables pure Python mode.
* **local\_infile** (`bool`): Allows local file uploads.
* **charset** (`str`): Character set for string values.
* **ssl\_key**, **ssl\_cert**, **ssl\_ca** (`str`): Paths to SSL files.
* **ssl\_disabled** (`bool`): Disables SSL.
* **ssl\_verify\_cert** (`bool`): Verifies server's certificate.
* **ssl\_verify\_identity** (`bool`): Verifies server's identity.
* **autocommit** (`bool`): Enables autocommits.
* **results\_type** (`str`): Structure of query results (e.g., `tuples`, `dicts`).

```python  theme={null}
from langchain_singlestore.document_loaders import SingleStoreLoader

loader = SingleStoreLoader(
    host="127.0.0.1:3306/db",
    table_name="documents",
    content_field="content",
    metadata_field="metadata",
    id_field="id",
)
```

## Load

```python  theme={null}
docs = loader.load()
docs[0]
```

```python  theme={null}
print(docs[0].metadata)
```

## Lazy Load

```python  theme={null}
page = []
for doc in loader.lazy_load():
    page.append(doc)
    if len(page) >= 10:
        # do some paged operation, e.g.
        # index.upsert(page)

        page = []
```

***

## API reference

For detailed documentation of all SingleStore Document Loader features and configurations head to the github page: [https://github.com/singlestore-labs/langchain-singlestore/](https://github.com/singlestore-labs/langchain-singlestore/)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/singlestore.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt