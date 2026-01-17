# Obsidian Voice Agent

Voice and text interface for querying your Obsidian knowledge base using AI.

## Features

- **Voice Conversations**: Real-time voice chat via LiveKit
- **Text Chat**: Traditional chat interface for typed queries
- **Knowledge Base Search**: Full-text search across your Obsidian vault
- **Real-time File References**: See which documents the agent references

## Prerequisites

- Python 3.11+
- Node.js 20+
- [LiveKit Cloud](https://cloud.livekit.io/) account (or self-hosted LiveKit server)
- OpenAI API key

## Installation

```bash
# Backend
cd backend
uv sync

# Frontend
cd frontend
pnpm install
```

## Configuration

Copy `.env.example` to `.env` in the backend directory and fill in:

```env
OBSIDIAN_VAULT_PATH=/path/to/your/vault
OPENAI_API_KEY=sk-...
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
LIVEKIT_URL=wss://your-project.livekit.cloud
```

## Running

```bash
# Terminal 1: Build search index & start API
cd backend
uv run uvicorn src.api.routes:app --port 8000

# Terminal 2: Start voice agent
cd backend
uv run python -m src.agents.voice_agent dev

# Terminal 3: Start frontend
cd frontend
pnpm dev
```

Open http://localhost:5173 and toggle between Text/Voice modes.

## Architecture

```
┌─────────────────────────────────────────────┐
│              React Frontend                  │
│        (Text Chat + Voice UI)               │
└──────────────┬─────────────────┬────────────┘
               │                 │
         REST API          LiveKit Room
               │                 │
┌──────────────▼──────┐  ┌──────▼──────────────┐
│   Text Agent        │  │   Voice Agent       │
│   (Pydantic AI)     │  │   (LiveKit Agents)  │
└──────────┬──────────┘  └──────────┬──────────┘
           └──────────┬─────────────┘
                      │
           ┌──────────▼──────────┐
           │    Shared Tools     │
           │  (Search, Read)     │
           └──────────┬──────────┘
                      │
           ┌──────────▼──────────┐
           │   Obsidian Vault    │
           └─────────────────────┘
```

## Development

```bash
# Run tests
cd backend && uv run pytest

# Type check frontend
cd frontend && pnpm build

# Lint backend
cd backend && uv run ruff check src/
```

## License

MIT
