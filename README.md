# Obsidian Voice Agent

Voice and text interface for querying your Obsidian knowledge base using AI.

## Features

- **Voice Conversations**: Real-time voice chat powered by OpenAI Realtime API (~300ms latency)
- **Text Chat**: Traditional chat interface for typed queries
- **Knowledge Base Search**: Full-text search across your Obsidian vault
- **Real-time File References**: See which documents the agent references as it speaks

## Prerequisites

- Python 3.11+
- Node.js 20+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [pnpm](https://pnpm.io/) (Node package manager)
- [LiveKit Cloud](https://cloud.livekit.io/) account (free tier available)
- OpenAI API key (with Realtime API access)

## Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/coleam00/obsidian-voice-agent.git
cd obsidian-voice-agent

# Backend
cd backend
uv sync

# Frontend
cd ../frontend
pnpm install
```

### 2. Configure Environment

Create `backend/.env`:

```env
OBSIDIAN_VAULT_PATH=/path/to/your/vault
OPENAI_API_KEY=sk-...
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
LIVEKIT_URL=wss://your-project.livekit.cloud
```

Create `frontend/.env`:

```env
VITE_LIVEKIT_URL=wss://your-project.livekit.cloud
```

### 3. Run

```bash
# Terminal 1: Start API server
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
│   (Pydantic AI)     │  │   (OpenAI Realtime) │
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

## Available Tools

Both agents share these tools for querying your vault:

| Tool | Description |
|------|-------------|
| `search_documents` | Full-text search across all markdown files |
| `find_files` | Find files matching glob patterns (e.g., `**/daily/*.md`) |
| `search_content` | Regex search within file contents |
| `read_document` | Read full document with frontmatter parsing |
| `get_document_metadata` | Get tags, dates without full content |

## Development

```bash
# Run tests
cd backend && uv run pytest

# Type check frontend
cd frontend && pnpm build

# Lint backend
cd backend && uv run ruff check src/
```

## Tech Stack

- **Backend**: Python 3.11+, FastAPI, Pydantic AI, LiveKit Agents SDK
- **Voice**: OpenAI Realtime API (gpt-realtime-mini)
- **Search**: Whoosh full-text index
- **Frontend**: React 18, Vite, TypeScript, LiveKit React SDK

## License

MIT
