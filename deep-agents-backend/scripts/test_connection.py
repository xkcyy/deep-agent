#!/usr/bin/env python
"""Test connection to the LangGraph server."""

import asyncio
import os
import sys


async def test_connection():
    """Test basic connection and invocation."""
    try:
        from langgraph_sdk import get_client
    except ImportError:
        print("❌ langgraph-sdk not installed!")
        print("   Install with: pip install langgraph-sdk")
        return False

    deployment_url = os.getenv("DEPLOYMENT_URL", "http://127.0.0.1:2024")

    print(f"🔗 Connecting to LangGraph server at {deployment_url}...")

    client = get_client(url=deployment_url)

    # List assistants
    print("\n📋 Available assistants:")
    assistants = await client.assistants.search()
    for assistant in assistants:
        print(f"   - {assistant['assistant_id']}: {assistant.get('name', 'N/A')}")

    if not assistants:
        print("   No assistants found. Is the server running?")
        return False

    # Create a thread
    print("\n🧵 Creating test thread...")
    thread = await client.threads.create()
    print(f"   Thread ID: {thread['thread_id']}")

    # Test invocation
    print("\n💬 Sending test message...")
    assistant_id = assistants[0]["assistant_id"]

    async for chunk in client.runs.stream(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "human", "content": "Say hello!"}]},
        stream_mode="messages",
    ):
        if hasattr(chunk, "content"):
            print(f"   Response: {chunk.content[:100]}...")
            break

    print("\n✅ Connection test successful!")
    return True


def main():
    """Run the connection test."""
    print("=" * 50)
    print("Deep Agents Backend - Connection Test")
    print("=" * 50)

    try:
        success = asyncio.run(test_connection())
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure the LangGraph server is running:")
        print("   langgraph dev")
        sys.exit(1)


if __name__ == "__main__":
    main()

