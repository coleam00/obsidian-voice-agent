# Obsidian Voice Agent - Development Log

## Project Overview
Building a voice and text interface for querying Obsidian knowledge bases using LiveKit (voice) and Pydantic AI (text) with shared search tools.

---

## Timeline

### Day 1 - Project Setup & Full Implementation
**Date**: 2026-01-17

#### Phase 1: Project Setup
- [x] Initialized project with Kiro CLI Quick Start Wizard
- [x] Created steering documents (product.md, tech.md, structure.md)
- [x] Defined architecture: shared tools between LiveKit and Pydantic AI agents

#### Phase 2: Read-Only Tools Layer
- [x] Implemented Whoosh full-text search index
- [x] Created `search_documents()` - full-text search across vault
- [x] Created `find_files()` - glob pattern file discovery
- [x] Created `search_content()` - regex search within files
- [x] Created `read_document()` - read markdown with frontmatter
- [x] Created `get_document_metadata()` - metadata without full content

#### Phase 3: Text Agent & React Frontend
- [x] Built Pydantic AI text agent with all tools
- [x] Created FastAPI routes (`/chat`, `/health`, `/index/rebuild`)
- [x] Built React frontend with chat interface
- [x] Configured Vite proxy for API calls

#### Phase 4: LiveKit Voice Agent
- [x] Added LiveKit dependencies (livekit-agents, livekit-api)
- [x] Created voice agent with OpenAI Realtime API (`gpt-realtime-mini`)
- [x] Implemented `@function_tool` wrappers for shared tools
- [x] Added RPC for sending file references to frontend
- [x] Built React voice UI (connect/mute/disconnect, audio visualizer)
- [x] Added `/livekit-token` endpoint for JWT generation

#### Phase 5: Testing & Validation
- [x] Unit tests for all tools (pytest)
- [x] E2E tests with Agent Browser
- [x] Verified voice/text mode switching
- [x] Confirmed LiveKit connection flow works

#### Decisions Made
- **OpenAI Realtime API**: Chose `gpt-realtime-mini` for lowest latency (~300ms vs 2-3s with separate STT/LLM/TTS)
- **Dual agent approach**: LiveKit for voice, Pydantic AI for text - enables E2E testing via Agent Browser
- **Shared tools layer**: Framework-agnostic Python functions wrapped by each agent
- **Local-only deployment**: No auth needed, simplifies development

---

## Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| LiveKit API version conflict | Updated `livekit-api>=1.0.7,<2` to match livekit-agents requirements |
| AgentServer import location | Moved from `livekit.agents.voice` to `livekit.agents` |
| Slow voice response | Switched from separate STT/LLM/TTS to OpenAI Realtime API |
| Port conflicts during E2E testing | Added cleanup step to execute prompt |
| `server.run()` coroutine warning | Changed to `run_app(server)` from CLI module |

---

## Time Tracking

| Task | Hours |
|------|-------|
| Project setup & planning | 0.5 |
| Read-only tools implementation | 1.0 |
| Text agent & React frontend | 1.5 |
| LiveKit voice agent integration | 2.0 |
| Testing & debugging | 1.0 |
| **Total** | **6.0** |

---

## Key Learnings
- OpenAI Realtime API dramatically reduces voice latency vs traditional STT→LLM→TTS pipeline
- LiveKit Agents SDK has evolved - always check latest docs for import paths
- Agent Browser is excellent for E2E testing voice UIs (can verify state transitions)
- Always clean up test processes to avoid port conflicts

---

## Kiro CLI Features Used
- [x] Quick Start Wizard
- [x] Steering documents
- [x] @plan-feature (structured implementation plans)
- [x] @execute (plan execution with validation)
- [x] Agent Browser skill (E2E testing)
- [x] Custom prompts (execute.md updated with cleanup step)

---

## Tech Stack
- **Backend**: Python 3.11+, FastAPI, Pydantic AI, LiveKit Agents SDK
- **Voice**: OpenAI Realtime API (gpt-realtime-mini)
- **Search**: Whoosh full-text index
- **Frontend**: React, Vite, TypeScript, LiveKit React SDK
- **Testing**: pytest, Agent Browser
