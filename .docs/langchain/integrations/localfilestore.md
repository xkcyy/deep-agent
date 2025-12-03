# LocalFileStore

This will help you get started with local filesystem [key-value stores](/oss/python/integrations/stores). For detailed documentation of all LocalFileStore features and configurations head to the [API reference](https://python.langchain.com/api_reference/langchain/storage/langchain.storage.file_system.LocalFileStore.html).

## Overview

The `LocalFileStore` is a persistent implementation of `ByteStore` that stores everything in a folder of your choosing. It's useful if you're using a single machine and are tolerant of files being added or deleted.

### Integration details

| Class                                                                                                                            | Package                                                                      | Local | [JS support](https://js.langchain.com/docs/integrations/stores/file_system) |                                          Downloads                                         |                                         Version                                         |
| :------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- | :---: | :-------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------: |
| [LocalFileStore](https://python.langchain.com/api_reference/langchain/storage/langchain.storage.file_system.LocalFileStore.html) | [langchain](https://python.langchain.com/api_reference/langchain/index.html) |   ✅   |                                      ✅                                      | ![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain?style=flat-square\&label=%20) | ![PyPI - Version](https://img.shields.io/pypi/v/langchain?style=flat-square\&label=%20) |

### Installation

The LangChain `LocalFileStore` integration lives in the `langchain` package:

```python  theme={null}
pip install -qU langchain-classic
```

## Instantiation

Now we can instantiate our byte store:

```python  theme={null}
from pathlib import Path

from langchain_classic.storage import LocalFileStore

root_path = Path.cwd() / "data"  # can also be a path set by a string

kv_store = LocalFileStore(root_path)
```

## Usage

You can set data under keys like this using the `mset` method:

```python  theme={null}
kv_store.mset(
    [
        ["key1", b"value1"],
        ["key2", b"value2"],
    ]
)

kv_store.mget(
    [
        "key1",
        "key2",
    ]
)
```

```output  theme={null}
[b'value1', b'value2']
```

You can see the created files in your `data` folder:

```python  theme={null}
!ls {root_path}
```

```output  theme={null}
key1 key2
```

And you can delete data using the `mdelete` method:

```python  theme={null}
kv_store.mdelete(
    [
        "key1",
        "key2",
    ]
)

kv_store.mget(
    [
        "key1",
        "key2",
    ]
)
```

```output  theme={null}
[None, None]
```

***

## API reference

For detailed documentation of all `LocalFileStore` features and configurations, head to the API reference: [python.langchain.com/api\_reference/langchain/storage/langchain.storage.file\_system.LocalFileStore.html](https://python.langchain.com/api_reference/langchain/storage/langchain.storage.file_system.LocalFileStore.html)

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/stores/file_system.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt