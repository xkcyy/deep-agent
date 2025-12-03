# Google Places

This notebook goes through how to use Google Places API

```python  theme={null}
pip install -qU  googlemaps langchain-community
```

```python  theme={null}
import os

os.environ["GPLACES_API_KEY"] = ""
```

```python  theme={null}
from langchain_community.tools import GooglePlacesTool
```

```python  theme={null}
places = GooglePlacesTool()
```

```python  theme={null}
places.run("al fornos")
```

```output  theme={null}
"1. Delfina Restaurant\nAddress: 3621 18th St, San Francisco, CA 94110, USA\nPhone: (415) 552-4055\nWebsite: https://www.delfinasf.com/\n\n\n2. Piccolo Forno\nAddress: 725 Columbus Ave, San Francisco, CA 94133, USA\nPhone: (415) 757-0087\nWebsite: https://piccolo-forno-sf.com/\n\n\n3. L'Osteria del Forno\nAddress: 519 Columbus Ave, San Francisco, CA 94133, USA\nPhone: (415) 982-1124\nWebsite: Unknown\n\n\n4. Il Fornaio\nAddress: 1265 Battery St, San Francisco, CA 94111, USA\nPhone: (415) 986-0100\nWebsite: https://www.ilfornaio.com/\n\n"
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/google_places.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt