# Feature: LiveKit Voice Agent Integration

The following plan should be complete, but validate documentation and codebase patterns before implementing.

Pay special attention to naming of existing utils, types, and models. Import from the right files.

## Feature Description

Add real-time voice conversation capabilities to the Obsidian Voice Agent using LiveKit. Users can press a button to start talking to the agent, which will search their knowledge base and respond via voice. A panel shows referenced files in real-time as the agent mentions them.

## User Story

As a knowledge worker using Obsidian
I want to have voice conversations with an AI agent about my notes
So that I can query my knowledge base hands-free while multitasking

## Problem Statement

The current text-only interface requires typing, which isn't ideal for hands-free use cases. Users want to speak naturally and hear responses while seeing which documents the agent references.

## Solution Statement

Implement a LiveKit voice agent that:
1. Shares the existing search tools with the text agent
2. Sends file references to the frontend via RPC when tools are called
3. Provides a React UI with connect/mute buttons, audio visualizer, and referenced files panel

## Feature Metadata

**Feature Type**: New Capability
**Estimated Complexity**: High
**Primary Systems Affected**: Backend (new voice agent), Frontend (new components), API (token endpoint)
**Dependencies**: livekit-agents, livekit-api, @livekit/components-react, livekit-client

---

## CONTEXT REFERENCES

### Relevant Codebase Files - MUST READ BEFORE IMPLEMENTING

- `backend/src/tools/__init__.py` - Why: Shows how tools are exported, pattern to follow for voice agent imports
- `backend/src/tools/search.py` (full file) - Why: Contains search_documents, find_files, search_content - will wrap these as @function_tool
- `backend/src/tools/documents.py` (full file) - Why: Contains read_document, get_document_metadata - will wrap these
- `backend/src/agents/text_agent.py` (full file) - Why: Shows system prompt pattern and tool registration approach
- `backend/src/config.py` (full file) - Why: Settings pattern to extend for LiveKit credentials
- `backend/src/api/routes.py` (full file) - Why: FastAPI patterns, will add token endpoint here
- `backend/pyproject.toml` - Why: Dependency management pattern
- `frontend/src/App.tsx` (full file) - Why: Current React patterns, state management approach
- `frontend/src/App.css` (full file) - Why: Styling patterns (dark theme, #3b82f6 accent)
- `frontend/package.json` - Why: Dependency management
- `frontend/vite.config.ts` - Why: Proxy configuration pattern
- `backend/tests/conftest.py` - Why: Fixture patterns for testing

### New Files to Create

**Backend:**
- `backend/src/agents/voice_agent.py` - LiveKit voice agent with @function_tool wrappers
- `backend/src/api/livekit_token.py` - Token generation endpoint (or add to routes.py)

**Frontend:**
- `frontend/src/components/VoiceAgent.tsx` - Main voice agent component with LiveKitRoom
- `frontend/src/components/VoiceControls.tsx` - Connect/disconnect/mute buttons
- `frontend/src/components/ReferencedFiles.tsx` - Panel showing files agent references
- `frontend/src/components/AudioVisualizer.tsx` - Wrapper around BarVisualizer
- `frontend/src/hooks/useReferencedFiles.ts` - Hook for managing RPC-received file references

**Tests:**
- `backend/tests/test_voice_agent.py` - Voice agent tool tests

### Relevant Documentation - READ BEFORE IMPLEMENTING

- [LiveKit Agents Quickstart](https://docs.livekit.io/agents/start/voice-ai-quickstart/)
  - Section: Agent code, AgentSession setup
  - Why: Shows exact pattern for Agent class and session initialization

- [LiveKit Tool Definition](https://docs.livekit.io/agents/logic/tools/)
  - Section: Function tool definition, @function_tool decorator
  - Why: Shows how to define tools with proper signatures

- [LiveKit RPC](https://docs.livekit.io/transport/data/rpc/)
  - Section: Method registration, Calling a method
  - Why: Shows how to send data from agent to frontend

- [LiveKit React Components](https://docs.livekit.io/frontends/start/frontends/)
  - Section: Audio visualizer, useVoiceAssistant
  - Why: Shows React component patterns

- [LiveKit Token Generation](https://docs.livekit.io/frontends/authentication/tokens/)
  - Section: Python token creation
  - Why: Shows exact API for generating access tokens

### Patterns to Follow

**Naming Conventions:**
- Python files: snake_case (`voice_agent.py`)
- Python functions: snake_case (`search_documents`)
- Python classes: PascalCase (`ObsidianVoiceAgent`)
- TypeScript components: PascalCase (`VoiceAgent.tsx`)
- TypeScript hooks: camelCase with `use` prefix (`useReferencedFiles`)
- CSS classes: kebab-case (`voice-controls`)

**Error Handling (from existing tools):**
```python
# Return error dict pattern from documents.py
if not full_path.exists():
    return {"error": "File not found", "path": path}
```

**Async Pattern (from existing tools):**
```python
# All tools are async, use asyncio.to_thread for blocking ops
async def search_documents(query: str, limit: int = 10) -> list[dict]:
    return await asyncio.to_thread(search_index, query, limit)
```

**Settings Pattern (from config.py):**
```python
class Settings(BaseSettings):
    obsidian_vault_path: Path
    model_config = {"env_file": ".env", "extra": "ignore"}
```

**React State Pattern (from App.tsx):**
```typescript
const [messages, setMessages] = useState<Message[]>([])
const [loading, setLoading] = useState(false)
```

**CSS Variables (from App.css):**
- Background: `#1a1a1a`
- Accent: `#3b82f6`
- Text: `#ffffff`

---

## IMPLEMENTATION PLAN

### Phase 1: Backend Foundation

Set up LiveKit dependencies, configuration, and token generation.

**Tasks:**
- Add LiveKit dependencies to pyproject.toml
- Extend Settings class with LiveKit credentials
- Create token generation endpoint

### Phase 2: Voice Agent Implementation

Create the LiveKit voice agent that wraps existing tools.

**Tasks:**
- Create voice_agent.py with Agent class
- Wrap existing tools as @function_tool methods
- Add RPC calls to send file references to frontend
- Set up AgentServer and entrypoint

### Phase 3: Frontend Components

Build React components for voice interaction.

**Tasks:**
- Add LiveKit React dependencies
- Create VoiceAgent component with LiveKitRoom
- Create control buttons (connect/mute)
- Create referenced files panel
- Add RPC handler for receiving file data
- Integrate into App.tsx

### Phase 4: Testing & Validation

Test the integration end-to-end.

**Tasks:**
- Test token generation endpoint
- Test voice agent tools
- Manual testing of voice flow

---

## STEP-BY-STEP TASKS

### Task 1: UPDATE `backend/pyproject.toml`

- **IMPLEMENT**: Add LiveKit dependencies
- **PATTERN**: Follow existing dependency format
- **ADD** to dependencies array:
```toml
"livekit-agents[silero,turn-detector,openai]~=1.3",
"livekit-api~=0.7",
```
- **VALIDATE**: `cd backend && uv sync`

### Task 2: UPDATE `backend/src/config.py`

- **IMPLEMENT**: Add LiveKit configuration fields
- **PATTERN**: Mirror existing Settings class pattern
- **ADD** fields:
```python
livekit_api_key: str = ""
livekit_api_secret: str = ""
livekit_url: str = ""
```
- **VALIDATE**: `cd backend && python -c "from src.config import settings; print('OK')"`

### Task 3: UPDATE `backend/src/api/routes.py`

- **IMPLEMENT**: Add token generation endpoint
- **PATTERN**: Follow existing route patterns (ChatRequest/ChatResponse)
- **IMPORTS**: `from livekit import api`
- **ADD** endpoint `/livekit-token` that:
  - Accepts room_name and participant_name
  - Returns JWT token with VideoGrants(room_join=True, room=room_name)
- **GOTCHA**: Token must include `can_publish=True` for microphone
- **VALIDATE**: `cd backend && python -c "from src.api.routes import app; print('OK')"`

### Task 4: CREATE `backend/src/agents/voice_agent.py`

- **IMPLEMENT**: LiveKit voice agent with tool wrappers
- **PATTERN**: Follow text_agent.py system prompt style
- **IMPORTS**:
```python
import json
from livekit.agents import Agent, AgentSession, AgentServer, function_tool, RunContext
from livekit.plugins import silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from src.tools import search_documents, find_files, search_content, read_document, get_document_metadata
from src.config import settings
```
- **IMPLEMENT** class `ObsidianVoiceAgent(Agent)` with:
  - System prompt similar to text_agent.py
  - `@function_tool` methods that wrap existing tools
  - RPC call to frontend after each tool returns results
- **IMPLEMENT** AgentServer with `@server.rtc_session()` entrypoint
- **GOTCHA**: Use `context.session` to access room for RPC
- **GOTCHA**: RPC payload must be JSON string, max 15KB
- **VALIDATE**: `cd backend && python -c "from src.agents.voice_agent import server; print('OK')"`

### Task 5: UPDATE `backend/src/agents/__init__.py`

- **IMPLEMENT**: Export voice agent server
- **ADD**: `from src.agents.voice_agent import server as voice_server`
- **UPDATE** `__all__` to include `voice_server`
- **VALIDATE**: `cd backend && python -c "from src.agents import voice_server; print('OK')"`

### Task 6: UPDATE `frontend/package.json`

- **IMPLEMENT**: Add LiveKit React dependencies
- **ADD** to dependencies:
```json
"@livekit/components-react": "^2.9",
"@livekit/components-styles": "^1.1",
"livekit-client": "^2.9"
```
- **VALIDATE**: `cd frontend && pnpm install`

### Task 7: CREATE `frontend/src/hooks/useReferencedFiles.ts`

- **IMPLEMENT**: Hook to manage file references received via RPC
- **PATTERN**: Follow React hooks conventions
- **IMPLEMENT**:
  - State for `referencedFiles: FileReference[]`
  - Function to add new references
  - Function to clear references
  - Return `{ referencedFiles, addReference, clearReferences }`
- **VALIDATE**: TypeScript compilation via `cd frontend && pnpm build`

### Task 8: CREATE `frontend/src/components/ReferencedFiles.tsx`

- **IMPLEMENT**: Panel showing files the agent references
- **PATTERN**: Follow App.tsx component style
- **PROPS**: `files: FileReference[]`
- **RENDER**: List of file paths with titles, scrollable container
- **STYLE**: Dark theme matching App.css
- **VALIDATE**: TypeScript compilation

### Task 9: CREATE `frontend/src/components/VoiceControls.tsx`

- **IMPLEMENT**: Connect/disconnect and mute buttons
- **PATTERN**: Follow App.tsx button styling
- **PROPS**: `isConnected`, `isMuted`, `onConnect`, `onDisconnect`, `onToggleMute`
- **RENDER**: Two buttons with appropriate icons/text
- **STYLE**: Use #3b82f6 accent for active states
- **VALIDATE**: TypeScript compilation

### Task 10: CREATE `frontend/src/components/AudioVisualizer.tsx`

- **IMPLEMENT**: Wrapper around LiveKit BarVisualizer
- **IMPORTS**: `import { BarVisualizer, useVoiceAssistant } from '@livekit/components-react'`
- **RENDER**: BarVisualizer with state indicator text
- **STYLE**: Centered, appropriate sizing
- **VALIDATE**: TypeScript compilation

### Task 11: CREATE `frontend/src/components/VoiceAgent.tsx`

- **IMPLEMENT**: Main voice agent component
- **IMPORTS**:
```typescript
import { LiveKitRoom, RoomAudioRenderer } from '@livekit/components-react'
import '@livekit/components-styles'
```
- **IMPLEMENT**:
  - State for connection, token, room name
  - Fetch token from `/api/livekit-token` on connect
  - LiveKitRoom wrapper with child components
  - RPC handler registration for `showReferencedFiles`
  - Compose VoiceControls, AudioVisualizer, ReferencedFiles
- **GOTCHA**: Must render RoomAudioRenderer for agent audio playback
- **GOTCHA**: Register RPC handler after room connection
- **VALIDATE**: TypeScript compilation

### Task 12: UPDATE `frontend/src/App.tsx`

- **IMPLEMENT**: Add voice agent tab/toggle alongside text chat
- **PATTERN**: Follow existing state management
- **ADD**: Import VoiceAgent component
- **ADD**: State for `mode: 'text' | 'voice'`
- **ADD**: Toggle buttons to switch modes
- **RENDER**: Conditionally show chat or VoiceAgent based on mode
- **VALIDATE**: `cd frontend && pnpm build`

### Task 13: UPDATE `frontend/src/App.css`

- **IMPLEMENT**: Styles for voice components
- **PATTERN**: Follow existing dark theme
- **ADD** styles for:
  - `.voice-container` - main voice UI wrapper
  - `.voice-controls` - button container
  - `.referenced-files` - file panel
  - `.audio-visualizer` - visualizer container
  - `.mode-toggle` - text/voice mode switcher
- **VALIDATE**: Visual inspection

### Task 14: CREATE `backend/tests/test_voice_agent.py`

- **IMPLEMENT**: Tests for voice agent tools
- **PATTERN**: Follow test_tools.py class-based structure
- **IMPORTS**: Use existing conftest fixtures
- **TEST**: Tool wrapper functions return expected data
- **VALIDATE**: `cd backend && uv run pytest tests/test_voice_agent.py -v`

### Task 15: CREATE `README.md`

- **IMPLEMENT**: Project documentation at repository root
- **SECTIONS**:
  - **Title & Description**: Obsidian Voice Agent - voice and text interface for Obsidian knowledge bases
  - **Features**: Voice conversations, text chat, knowledge base search, real-time file references
  - **Prerequisites**: Python 3.11+, Node.js 20+, LiveKit Cloud account, OpenAI API key
  - **Installation**:
    ```bash
    # Backend
    cd backend
    uv sync
    
    # Frontend
    cd frontend
    pnpm install
    ```
  - **Configuration**: Copy `.env.example` to `.env`, fill in credentials (OBSIDIAN_VAULT_PATH, OPENAI_API_KEY, LIVEKIT_*)
  - **Running**:
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
  - **Usage**: Open http://localhost:5173, toggle between Text/Voice modes
  - **Architecture**: Brief diagram or description of components (text agent, voice agent, shared tools, React frontend)
  - **Development**: How to run tests (`uv run pytest`, `pnpm build`)
  - **License**: (if applicable)
- **PATTERN**: Clear, scannable markdown with code blocks
- **VALIDATE**: `cat README.md` - verify renders correctly

### Task 16: E2E TEST with Agent Browser

- **IMPLEMENT**: End-to-end test of voice UI connectivity
- **PREREQUISITE**: All services running (backend API on 8000, voice agent, frontend on 5173)
- **TEST FLOW**:

```bash
# 1. Open the app
agent-browser open http://localhost:5173

# 2. Get initial snapshot to find mode toggle
agent-browser snapshot -i

# 3. Click voice mode toggle (find button with "Voice" text or appropriate ref)
agent-browser find text "Voice" click
# OR: agent-browser click @eN  (use ref from snapshot)

# 4. Re-snapshot to get voice UI elements
agent-browser snapshot -i

# 5. Verify voice UI loaded - should see Connect button
agent-browser wait --text "Connect"

# 6. Click Connect button to initiate LiveKit connection
agent-browser find text "Connect" click
# OR: agent-browser click @eN

# 7. Wait for connection (button should change to Disconnect or show connected state)
agent-browser wait 3000
agent-browser snapshot -i

# 8. Check for errors in console
agent-browser errors

# 9. Verify no critical errors - should see connected state
agent-browser get text @eN  # Check status indicator

# 10. Test mute button exists and is clickable
agent-browser find text "Mute" click
# OR: agent-browser click @eN

# 11. Re-snapshot to verify mute state changed
agent-browser snapshot -i

# 12. Unmute
agent-browser find text "Unmute" click

# 13. Test disconnect
agent-browser find text "Disconnect" click

# 14. Verify returned to disconnected state
agent-browser wait 1000
agent-browser snapshot -i

# 15. Check backend logs/errors
agent-browser errors

# 16. Close browser
agent-browser close
```

- **VALIDATE**: No JavaScript errors, UI state transitions work, LiveKit connection established
- **GOTCHA**: Voice agent must be running (`uv run python -m src.agents.voice_agent dev`) for full test

---

## TESTING STRATEGY

### Unit Tests

Based on existing pytest patterns in `backend/tests/`:

- Test each @function_tool wrapper returns correct data structure
- Test token generation endpoint returns valid JWT
- Use `configured_settings` fixture for vault path

### Integration Tests

- Test voice agent can be instantiated
- Test RPC payload serialization

### E2E Tests (Agent Browser)

Automated browser tests to verify frontend-backend connectivity:

1. **Voice UI Loads**: Mode toggle works, voice interface renders
2. **LiveKit Connection**: Connect button initiates connection without errors
3. **Mute/Unmute**: Button toggles state correctly
4. **Disconnect**: Clean disconnection, UI returns to initial state
5. **No Console Errors**: No JavaScript errors during flow
6. **Backend Health**: Token endpoint responds, no 500 errors

### Edge Cases

- Empty search results
- Invalid file paths
- Missing LiveKit credentials (should fail gracefully)
- Network disconnection during voice session

---

## VALIDATION COMMANDS

### Level 1: Syntax & Style

```bash
cd backend && uv run ruff check src/
cd backend && uv run ruff format --check src/
cd frontend && pnpm build  # TypeScript compilation
```

### Level 2: Unit Tests

```bash
cd backend && uv run pytest tests/ -v
```

### Level 3: Integration Tests

```bash
# Start backend
cd backend && uv run uvicorn src.api.routes:app --reload &

# Test token endpoint
curl -X POST http://localhost:8000/livekit-token \
  -H "Content-Type: application/json" \
  -d '{"room_name": "test", "participant_name": "user"}'
```

### Level 4: E2E Tests (Agent Browser)

**Prerequisites**: Start all services first:
```bash
# Terminal 1: Backend API
cd backend && uv run uvicorn src.api.routes:app --port 8000

# Terminal 2: Voice Agent
cd backend && uv run python -m src.agents.voice_agent dev

# Terminal 3: Frontend
cd frontend && pnpm dev
```

**Run E2E test sequence**:
```bash
# Open app and verify initial load
agent-browser open http://localhost:5173
agent-browser wait --load networkidle
agent-browser snapshot -i

# Switch to voice mode
agent-browser find text "Voice" click
agent-browser wait 500
agent-browser snapshot -i

# Verify Connect button present
agent-browser wait --text "Connect"

# Test connection flow
agent-browser find text "Connect" click
agent-browser wait 3000

# Check for errors
agent-browser errors

# Verify connected state (Disconnect button should appear)
agent-browser snapshot -i
agent-browser wait --text "Disconnect"

# Test mute toggle
agent-browser find text "Mute" click
agent-browser wait 500
agent-browser snapshot -i

# Unmute
agent-browser find text "Unmute" click

# Disconnect
agent-browser find text "Disconnect" click
agent-browser wait 1000

# Verify clean disconnect
agent-browser snapshot -i
agent-browser wait --text "Connect"

# Final error check
agent-browser errors

# Cleanup
agent-browser close
```

**Success criteria**:
- No JavaScript errors in `agent-browser errors` output
- UI transitions: Connect → Disconnect, Mute → Unmute
- No 500 errors from backend (check terminal output)

### Level 5: Manual Validation

1. Set environment variables:
   - `LIVEKIT_API_KEY`
   - `LIVEKIT_API_SECRET`
   - `LIVEKIT_URL`
   - `OBSIDIAN_VAULT_PATH`

2. Start voice agent:
   ```bash
   cd backend && uv run python -m src.agents.voice_agent dev
   ```

3. Start backend API:
   ```bash
   cd backend && uv run uvicorn src.api.routes:app --port 8000
   ```

4. Start frontend:
   ```bash
   cd frontend && pnpm dev
   ```

5. Open http://localhost:5173
6. Switch to voice mode
7. Click connect button
8. Speak a query like "search for notes about Python"
9. Verify:
   - Agent responds via voice
   - Referenced files appear in panel
   - Mute button works
   - Disconnect button works

---

## ACCEPTANCE CRITERIA

- [ ] Voice agent starts and connects to LiveKit
- [ ] User can connect/disconnect via button
- [ ] User can mute/unmute microphone
- [ ] Agent responds to voice queries
- [ ] Agent searches Obsidian vault using existing tools
- [ ] Referenced files appear in UI panel in real-time
- [ ] Audio visualizer shows agent state (listening/thinking/speaking)
- [ ] Text chat still works (no regression)
- [ ] All validation commands pass
- [ ] Token endpoint returns valid JWT
- [ ] E2E tests pass (Agent Browser): no JS errors, UI state transitions work

---

## COMPLETION CHECKLIST

- [ ] All tasks completed in order
- [ ] Each task validation passed
- [ ] All validation commands executed successfully
- [ ] Full test suite passes (unit + E2E)
- [ ] No linting or type errors
- [ ] E2E Agent Browser tests pass
- [ ] Manual voice testing confirms feature works
- [ ] Acceptance criteria all met

---

## NOTES

### Design Decisions

1. **Shared tools via wrapper**: Rather than duplicating tool logic, voice agent wraps existing async functions with @function_tool decorator. This ensures consistency.

2. **RPC for file references**: Using RPC instead of text streams because file references are structured data that needs reliable delivery, not streaming text.

3. **Mode toggle vs tabs**: Simple toggle between text/voice modes keeps UI clean. Could evolve to tabs later.

4. **LiveKit Cloud vs self-hosted**: Plan assumes LiveKit Cloud for simplicity. Self-hosted would require additional Docker setup.

### Trade-offs

- **Complexity**: LiveKit adds significant complexity but provides production-grade voice infrastructure
- **Cost**: LiveKit Cloud has usage-based pricing; self-hosting requires infrastructure
- **Latency**: Voice round-trip depends on STT/LLM/TTS providers chosen

### Risks

1. **LiveKit credentials**: User must have LiveKit Cloud account or self-hosted server
2. **Browser permissions**: Microphone access requires HTTPS in production
3. **Model costs**: Voice agents use more API calls (STT + LLM + TTS per turn)

### Future Enhancements

- Conversation history persistence
- Voice activity visualization
- Transcript display alongside voice
- Multiple voice/persona options
