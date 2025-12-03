# Snowflake

This notebooks goes over how to load documents from Snowflake

```python  theme={null}
pip install -qU  snowflake-connector-python
```

```python  theme={null}
import settings as s
from langchain_community.document_loaders import SnowflakeLoader
```

```python  theme={null}
QUERY = "select text, survey_id from CLOUD_DATA_SOLUTIONS.HAPPY_OR_NOT.OPEN_FEEDBACK limit 10"
snowflake_loader = SnowflakeLoader(
    query=QUERY,
    user=s.SNOWFLAKE_USER,
    password=s.SNOWFLAKE_PASS,
    account=s.SNOWFLAKE_ACCOUNT,
    warehouse=s.SNOWFLAKE_WAREHOUSE,
    role=s.SNOWFLAKE_ROLE,
    database=s.SNOWFLAKE_DATABASE,
    schema=s.SNOWFLAKE_SCHEMA,
)
snowflake_documents = snowflake_loader.load()
print(snowflake_documents)
```

```python  theme={null}
import settings as s
from snowflakeLoader import SnowflakeLoader

QUERY = "select text, survey_id as source from CLOUD_DATA_SOLUTIONS.HAPPY_OR_NOT.OPEN_FEEDBACK limit 10"
snowflake_loader = SnowflakeLoader(
    query=QUERY,
    user=s.SNOWFLAKE_USER,
    password=s.SNOWFLAKE_PASS,
    account=s.SNOWFLAKE_ACCOUNT,
    warehouse=s.SNOWFLAKE_WAREHOUSE,
    role=s.SNOWFLAKE_ROLE,
    database=s.SNOWFLAKE_DATABASE,
    schema=s.SNOWFLAKE_SCHEMA,
    metadata_columns=["source"],
)
snowflake_documents = snowflake_loader.load()
print(snowflake_documents)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/snowflake.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt