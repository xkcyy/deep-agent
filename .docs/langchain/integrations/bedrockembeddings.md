# BedrockEmbeddings

> [Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service that offers a choice of
> high-performing foundation models (FMs) from leading AI companies like `AI21 Labs`, `Anthropic`, `Cohere`,
> `Meta`, `Stability AI`, and `Amazon` via a single API, along with a broad set of capabilities you need to
> build generative AI applications with security, privacy, and responsible AI. Using `Amazon Bedrock`,
> you can easily experiment with and evaluate top FMs for your use case, privately customize them with
> your data using techniques such as fine-tuning and `Retrieval Augmented Generation` (`RAG`), and build
> agents that execute tasks using your enterprise systems and data sources. Since `Amazon Bedrock` is
> serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy
> generative AI capabilities into your applications using the AWS services you are already familiar with.

```python  theme={null}
pip install -qU  boto3
```

```python  theme={null}
from langchain_aws import BedrockEmbeddings

embeddings = BedrockEmbeddings(
    credentials_profile_name="bedrock-admin", region_name="us-east-1"
)
```

```python  theme={null}
embeddings.embed_query("This is a content of the document")
```

```python  theme={null}
embeddings.embed_documents(
    ["This is a content of the document", "This is another document"]
)
```

```python  theme={null}
# async embed query
await embeddings.aembed_query("This is a content of the document")
```

```python  theme={null}
# async embed documents
await embeddings.aembed_documents(
    ["This is a content of the document", "This is another document"]
)
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/text_embedding/bedrock.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt