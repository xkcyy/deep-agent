# OpenLLM

[🦾 OpenLLM](https://github.com/bentoml/OpenLLM) lets developers run any **open-source LLMs** as **OpenAI-compatible API** endpoints with **a single command**.

* 🔬 Build for fast and production usages
* 🚂 Support llama3, qwen2, gemma, etc, and many **quantized** versions [full list](https://github.com/bentoml/openllm-models)
* ⛓️ OpenAI-compatible API
* 💬 Built-in ChatGPT like UI
* 🔥 Accelerated LLM decoding with state-of-the-art inference backends
* 🌥️ Ready for enterprise-grade cloud deployment (Kubernetes, Docker and BentoCloud)

## Installation

Install `openllm` through [PyPI](https://pypi.org/project/openllm/)

```python  theme={null}
pip install -qU  openllm
```

## Launch OpenLLM server locally

To start an LLM server, use `openllm hello` command:

```bash  theme={null}
openllm hello
```

## Wrapper

```python  theme={null}
from langchain_community.llms import OpenLLM

server_url = "http://localhost:3000"  # Replace with remote host if you are running on a remote server
llm = OpenLLM(base_url=server_url, api_key="na")
```

```python  theme={null}
llm("To build a LLM from scratch, the following are the steps:")
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/llms/openllm.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt