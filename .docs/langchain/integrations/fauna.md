# Fauna

> [Fauna](https://fauna.com/) is a Document Database.

Query `Fauna` documents

```python  theme={null}
pip install -qU  fauna
```

## Query data example

```python  theme={null}
from langchain_community.document_loaders.fauna import FaunaLoader

secret = "<enter-valid-fauna-secret>"
query = "Item.all()"  # Fauna query. Assumes that the collection is called "Item"
field = "text"  # The field that contains the page content. Assumes that the field is called "text"

loader = FaunaLoader(query, field, secret)
docs = loader.lazy_load()

for value in docs:
    print(value)
```

### Query with Pagination

You get a `after` value if there are more data. You can get values after the curcor by passing in the `after` string in query.

To learn more following [this link](https://fqlx-beta--fauna-docs.netlify.app/fqlx/beta/reference/schema_entities/set/static-paginate)

```python  theme={null}
query = """
Item.paginate("hs+DzoPOg ... aY1hOohozrV7A")
Item.all()
"""
loader = FaunaLoader(query, field, secret)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/fauna.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt