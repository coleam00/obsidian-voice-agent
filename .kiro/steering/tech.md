# Technical Architecture

## Technology Stack
- **Backend**: Python 3.11+
- **Voice Agent**: LiveKit Agents SDK
- **Text Agent**: Pydantic AI
- **Search Tools**: Whoosh (full-text), glob/pathlib (file discovery), regex (pattern matching)
- **Frontend**: React + Vite + TypeScript
- **Voice UI**: LiveKit React SDK
- **Package Management**: uv (Python), pnpm (Node.js)

## Architecture Overview
```
┌─────────────────────────────────────────────────┐
│                 React Frontend                   │
│         (Voice UI + Text Chat Interface)         │
└──────────────┬─────────────────────┬────────────┘
               │                     │
       LiveKit Room            REST/WebSocket
               │                     │
┌──────────────▼──────┐  ┌──────────▼──────────────┐
│   LiveKit Agent     │  │   Pydantic AI Agent     │
│   (Voice)           │  │   (Text)                │
└──────────┬──────────┘  └──────────┬──────────────┘
           │                        │
           └──────────┬─────────────┘
                      │
           ┌──────────▼──────────┐
           │   Shared Tools      │
           │  (Cursor/Jex/Blob)  │
           └──────────┬──────────┘
                      │
           ┌──────────▼──────────┐
           │  Obsidian Vault     │
           │  (Markdown Files)   │
           └─────────────────────┘
```

## Development Environment
- Python 3.11+ with uv for dependency management
- Node.js 20+ with pnpm
- LiveKit server (local or cloud for development)
- Obsidian vault path configured via environment variable

## Code Standards
- Python: Ruff for linting/formatting, type hints required
- TypeScript: ESLint + Prettier, strict mode
- Pydantic models for all data structures
- Async/await patterns throughout

## Testing Strategy
- **E2E Testing**: Agent Browser for full workflow testing via text interface
- **Unit Tests**: pytest for Python tools and agent logic
- **Integration**: Test shared tools independently of agent framework

## Deployment Process
- Local development only (no cloud deployment)
- Docker Compose for local LiveKit server (optional)
- Environment variables for Obsidian vault path configuration

## Performance Requirements
- Search response: < 1 second for typical queries
- Voice latency: Real-time conversation flow
- Support vaults with 1000+ documents

## Security Considerations
- Local-only access (no authentication required)
- No external data transmission beyond LLM API calls
- Obsidian vault accessed read-only

## Current Scope Constraints
- **Read-only tools only**: Search, read, summarize - no write operations
- **No MCP servers**: Custom tools built directly in Python
- **No hooks or custom agents**: Keeping architecture simple
