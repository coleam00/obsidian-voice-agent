# Project Structure

## Directory Layout
```
obsidian-voice-agent/
├── backend/
│   ├── src/
│   │   ├── agents/
│   │   │   ├── voice_agent.py      # LiveKit voice agent
│   │   │   └── text_agent.py       # Pydantic AI text agent
│   │   ├── tools/
│   │   │   ├── __init__.py         # Shared tool exports
│   │   │   ├── search.py           # Cursor/Jex/BlobSearch
│   │   │   └── summarize.py        # Document summarization
│   │   ├── api/
│   │   │   └── routes.py           # FastAPI routes for text agent
│   │   └── config.py               # Configuration management
│   ├── tests/
│   ├── pyproject.toml
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
├── docs/
├── .kiro/
└── README.md
```

## File Naming Conventions
- Python: snake_case for files and functions
- TypeScript: PascalCase for components, camelCase for utilities
- Configuration: lowercase with hyphens (e.g., `docker-compose.yml`)

## Module Organization
- `tools/`: Shared agent tools (framework-agnostic)
- `agents/`: Framework-specific agent implementations
- `api/`: HTTP endpoints for text agent access

## Configuration Files
- `backend/.env`: Obsidian vault path, LLM API keys, LiveKit credentials
- `frontend/.env`: API endpoint URLs
- `pyproject.toml`: Python dependencies and tool config
- `package.json`: Frontend dependencies

## Documentation Structure
- `README.md`: Setup and usage instructions
- `DEVLOG.md`: Development timeline and decisions
- `docs/`: Additional documentation as needed

## Build Artifacts
- `backend/.venv/`: Python virtual environment
- `frontend/dist/`: Vite build output
- `frontend/node_modules/`: Node dependencies

## Environment-Specific Files
- `.env.example`: Template for required environment variables
- `.env`: Local configuration (gitignored)
