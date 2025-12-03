# YouTube

> [YouTube](https://www.youtube.com/) is an online video sharing and social media platform by Google.
> We download the `YouTube` transcripts and video information.

## Installation and Setup

<CodeGroup>
  ```bash pip theme={null}
  pip install youtube-transcript-api
  pip install pytube
  ```

  ```bash uv theme={null}
  uv add youtube-transcript-api
  uv add pytube
  ```
</CodeGroup>

See a [usage example](/oss/python/integrations/document_loaders/youtube_transcript).

## Document Loader

See a [usage example](/oss/python/integrations/document_loaders/youtube_transcript).

```python  theme={null}
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import GoogleApiYoutubeLoader
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/youtube.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt