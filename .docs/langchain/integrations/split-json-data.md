# Split JSON data

This json splitter [splits](/oss/python/integrations/splitters/) json data while allowing control over chunk sizes. It traverses json data depth first and builds smaller json chunks. It attempts to keep nested json objects whole but will split them if needed to keep chunks between a min\_chunk\_size and the max\_chunk\_size.

If the value is not a nested json, but rather a very large string the string will not be split. If you need a hard cap on the chunk size consider composing this with a Recursive Text splitter on those chunks. There is an optional pre-processing step to split lists, by first converting them to json (dict) and then splitting them as such.

1. How the text is split: json value.
2. How the chunk size is measured: by number of characters.

```python  theme={null}
pip install -qU langchain-text-splitters
```

First we load some json data:

```python  theme={null}
import json

import requests

# This is a large nested json object and will be loaded as a python dict
json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
```

## Basic usage

Specify `max_chunk_size` to constrain chunk sizes:

```python  theme={null}
from langchain_text_splitters import RecursiveJsonSplitter

splitter = RecursiveJsonSplitter(max_chunk_size=300)
```

To obtain json chunks, use the `.split_json` method:

```python  theme={null}
# Recursively split json data - If you need to access/manipulate the smaller json chunks
json_chunks = splitter.split_json(json_data=json_data)

for chunk in json_chunks[:3]:
    print(chunk)
```

```output  theme={null}
{'openapi': '3.1.0', 'info': {'title': 'LangSmith', 'version': '0.1.0'}, 'servers': [{'url': 'https://api.smith.langchain.com', 'description': 'LangSmith API endpoint.'}]}
{'paths': {'/api/v1/sessions/{session_id}': {'get': {'tags': ['tracer-sessions'], 'summary': 'Read Tracer Session', 'description': 'Get a specific session.', 'operationId': 'read_tracer_session_api_v1_sessions__session_id__get'}}}}
{'paths': {'/api/v1/sessions/{session_id}': {'get': {'security': [{'API Key': []}, {'Tenant ID': []}, {'Bearer Auth': []}]}}}}
```

To obtain LangChain [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) objects, use the `.create_documents` method:

```python  theme={null}
# The splitter can also output documents
docs = splitter.create_documents(texts=[json_data])

for doc in docs[:3]:
    print(doc)
```

```output  theme={null}
page_content='{"openapi": "3.1.0", "info": {"title": "LangSmith", "version": "0.1.0"}, "servers": [{"url": "https://api.smith.langchain.com", "description": "LangSmith API endpoint."}]}'
page_content='{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}'
page_content='{"paths": {"/api/v1/sessions/{session_id}": {"get": {"security": [{"API Key": []}, {"Tenant ID": []}, {"Bearer Auth": []}]}}}}'
```

Or use `.split_text` to obtain string content directly:

```python  theme={null}
texts = splitter.split_text(json_data=json_data)

print(texts[0])
print(texts[1])
```

```output  theme={null}
{"openapi": "3.1.0", "info": {"title": "LangSmith", "version": "0.1.0"}, "servers": [{"url": "https://api.smith.langchain.com", "description": "LangSmith API endpoint."}]}
{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}
```

## How to manage chunk sizes from list content

Note that one of the chunks in this example is larger than the specified `max_chunk_size` of 300. Reviewing one of these chunks that was bigger we see there is a list object there:

```python  theme={null}
print([len(text) for text in texts][:10])
print()
print(texts[3])
```

```output  theme={null}
[171, 231, 126, 469, 210, 213, 237, 271, 191, 232]

{"paths": {"/api/v1/sessions/{session_id}": {"get": {"parameters": [{"name": "session_id", "in": "path", "required": true, "schema": {"type": "string", "format": "uuid", "title": "Session Id"}}, {"name": "include_stats", "in": "query", "required": false, "schema": {"type": "boolean", "default": false, "title": "Include Stats"}}, {"name": "accept", "in": "header", "required": false, "schema": {"anyOf": [{"type": "string"}, {"type": "null"}], "title": "Accept"}}]}}}}
```

The json splitter by default does not split lists.

Specify `convert_lists=True` to preprocess the json, converting list content to dicts with `index:item` as `key:val` pairs:

```python  theme={null}
texts = splitter.split_text(json_data=json_data, convert_lists=True)
```

Let's look at the size of the chunks. Now they are all under the max

```python  theme={null}
print([len(text) for text in texts][:10])
```

```output  theme={null}
[176, 236, 141, 203, 212, 221, 210, 213, 242, 291]
```

The list has been converted to a dict, but retains all the needed contextual information even if split into many chunks:

```python  theme={null}
print(texts[1])
```

```output  theme={null}
{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": {"0": "tracer-sessions"}, "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}
```

```python  theme={null}
# We can also look at the documents
docs[1]
```

```output  theme={null}
Document(page_content='{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}')
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/splitters/recursive_json_splitter.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt