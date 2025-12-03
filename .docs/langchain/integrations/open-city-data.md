# Open City Data

[Socrata](https://dev.socrata.com/foundry/data.sfgov.org/vw6y-z8j6) provides an API for city open data.

For a dataset such as [SF crime](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry), see the `API` tab on top right.

That provides you with the `dataset identifier`.

Use the dataset identifier to grab specific tables for a given city\_id (`data.sfgov.org`) -

E.g., `vw6y-z8j6` for [SF 311 data](https://dev.socrata.com/foundry/data.sfgov.org/vw6y-z8j6).

E.g., `tmnf-yvry` for [SF Police data](https://dev.socrata.com/foundry/data.sfgov.org/tmnf-yvry).

```python  theme={null}
pip install -qU  sodapy
```

```python  theme={null}
from langchain_community.document_loaders import OpenCityDataLoader
```

```python  theme={null}
dataset = "vw6y-z8j6"  # 311 data
dataset = "tmnf-yvry"  # crime data
loader = OpenCityDataLoader(city_id="data.sfgov.org", dataset_id=dataset, limit=2000)
```

```python  theme={null}
docs = loader.load()
```

```output  theme={null}
WARNING:root:Requests made without an app_token will be subject to strict throttling limits.
```

```python  theme={null}
eval(docs[0].page_content)
```

```output  theme={null}
{'pdid': '4133422003074',
 'incidntnum': '041334220',
 'incident_code': '03074',
 'category': 'ROBBERY',
 'descript': 'ROBBERY, BODILY FORCE',
 'dayofweek': 'Monday',
 'date': '2004-11-22T00:00:00.000',
 'time': '17:50',
 'pddistrict': 'INGLESIDE',
 'resolution': 'NONE',
 'address': 'GENEVA AV / SANTOS ST',
 'x': '-122.420084075249',
 'y': '37.7083109744362',
 'location': {'type': 'Point',
  'coordinates': [-122.420084075249, 37.7083109744362]},
 ':@computed_region_26cr_cadq': '9',
 ':@computed_region_rxqg_mtj9': '8',
 ':@computed_region_bh8s_q3mv': '309'}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/open_city_data.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt