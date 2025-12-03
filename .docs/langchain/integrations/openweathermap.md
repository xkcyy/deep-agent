# OpenWeatherMap

This notebook goes over how to use the `OpenWeatherMap` component to fetch weather information.

First, you need to sign up for an `OpenWeatherMap API` key:

1. Go to OpenWeatherMap and sign up for an API key [here](https://openweathermap.org/api/)
2. pip install pyowm

Then we will need to set some environment variables:

1. Save your API KEY into OPENWEATHERMAP\_API\_KEY env variable

## Use the wrapper

```python  theme={null}
pip install -qU pyowm
```

```python  theme={null}
import os

from langchain_community.utilities import OpenWeatherMapAPIWrapper

os.environ["OPENWEATHERMAP_API_KEY"] = ""

weather = OpenWeatherMapAPIWrapper()
```

```python  theme={null}
weather_data = weather.run("London,GB")
print(weather_data)
```

```output  theme={null}
In London,GB, the current weather is as follows:
Detailed status: overcast clouds
Wind speed: 4.12 m/s, direction: 10°
Humidity: 51%
Temperature:
  - Current: 12.82°C
  - High: 13.98°C
  - Low: 12.01°C
  - Feels like: 11.49°C
Rain: {}
Heat index: None
Cloud cover: 100%
```

## Use the tool

```python  theme={null}
import os

from langchain.agents import create_agent


os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENWEATHERMAP_API_KEY"] = ""

tools = [weather.run]
agent = create_agent("gpt-4.1-mini", tools)
```

```python  theme={null}
input_message = {
    "role": "user",
    "content": "What's the weather like in London?",
}

for step in agent.stream(
    {"messages": [input_message]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
```

```output  theme={null}
================================ Human Message =================================

What's the weather like in London?
================================== Ai Message ==================================
Tool Calls:
  run (call_6vPq9neyy7oOnht29ExidE2g)
 Call ID: call_6vPq9neyy7oOnht29ExidE2g
  Args:
    location: London
================================= Tool Message =================================
Name: run

In London, the current weather is as follows:
Detailed status: overcast clouds
Wind speed: 4.12 m/s, direction: 10°
Humidity: 51%
Temperature:
  - Current: 12.82°C
  - High: 13.98°C
  - Low: 12.01°C
  - Feels like: 11.49°C
Rain: {}
Heat index: None
Cloud cover: 100%
================================== Ai Message ==================================

The weather in London is currently overcast with 100% cloud cover. The temperature is around 12.82°C, feeling like 11.49°C. The wind is blowing at 4.12 m/s from the direction of 10°. Humidity is at 51%. The high for the day is 13.98°C, and the low is 12.01°C.
```

```python  theme={null}
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/openweathermap.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt