# AWS S3 File

> [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) is an object storage service.

> [AWS S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)

This covers how to load document objects from an `AWS S3 File` object.

```python  theme={null}
from langchain_community.document_loaders import S3FileLoader
```

```python  theme={null}
pip install -qU  boto3
```

```python  theme={null}
loader = S3FileLoader("testing-hwc", "fake.docx")
```

```python  theme={null}
loader.load()
```

```output  theme={null}
[Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': 's3://testing-hwc/fake.docx'}, lookup_index=0)]
```

## Configuring the AWS Boto3 client

You can configure the AWS [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) client by passing
named arguments when creating the S3DirectoryLoader.
This is useful for instance when AWS credentials can't be set as environment variables.
See the [list of parameters](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session) that can be configured.

```python  theme={null}
loader = S3FileLoader(
    "testing-hwc", "fake.docx", aws_access_key_id="xxxx", aws_secret_access_key="yyyy"
)
```

```python  theme={null}
loader.load()
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_loaders/aws_s3_file.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.langchain.com/llms.txt