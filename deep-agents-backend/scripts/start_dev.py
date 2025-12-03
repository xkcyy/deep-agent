#!/usr/bin/env python
"""Development server startup script."""

import subprocess
import sys
from pathlib import Path


def main():
    """Start the LangGraph development server."""
    # Ensure we're in the right directory
    project_root = Path(__file__).parent.parent
    
    print("🚀 Starting Deep Agents Backend...")
    print(f"📁 Project root: {project_root}")
    
    # Check for .env file
    env_file = project_root / ".env"
    if not env_file.exists():
        print("⚠️  Warning: .env file not found!")
        print("   Copy env.example to .env and configure your API keys.")
        print()
    
    # Start LangGraph dev server
    try:
        subprocess.run(
            ["langgraph", "dev"],
            cwd=project_root,
            check=True,
        )
    except FileNotFoundError:
        print("❌ Error: langgraph CLI not found!")
        print("   Install it with: pip install langgraph-cli")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Server stopped.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

