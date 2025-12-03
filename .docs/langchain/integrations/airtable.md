# Airtable

```python  theme={null}
pip install -qU  pyairtable
```

```python  theme={null}
from langchain_community.document_loaders import AirtableLoader
```

* Get your API key [here](https://support.airtable.com/docs/creating-and-using-api-keys-and-access-tokens).
* Get ID of your base [here](https://airtable.com/developers/web/api/introduction).
* Get your table ID from the table url as shown [here](https://www.highviewapps.com/kb/where-can-i-find-the-airtable-base-id-and-table-id/#:~:text=Both%20the%20Airtable%20Base%20ID,URL%20that%20begins%20with%20tbl).

```python  theme={null}
api_key = "xxx"
base_id = "xxx"
table_id = "xxx"
view = "xxx"  # optional
```

```python  theme={null}
loader = AirtableLoader(api_key, table_id, base_id, view=view)
docs = loader.load()
```

Returns each table row as `dict`.

```python  theme={null}
len(docs)
```

```output  theme={null}
3
```

```python  theme={null}
eval(docs[0].page_content)
```

```output  theme={null}
{'id': 'recF3GbGZCuh9sXIQ',
 'createdTime': '2023-06-09T04:47:21.000Z',
 'fields': {'Priority': 'High',
  'Status': 'In progress',
  'Name': 'Document Splitters'}}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/airtable.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt