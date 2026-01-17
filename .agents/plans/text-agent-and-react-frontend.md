# Feature: Pydantic AI Text Agent + React Chat Frontend

The following plan should be complete, but validate documentation and codebase patterns before implementing.

Pay special attention to naming of existing utils, types, and models. Import from the right files.

## Feature Description

Build a Pydantic AI text agent that wraps the existing search tools, and a minimal React frontend with a chat interface. This enables conversational access to the Obsidian knowledge base via text, and allows E2E testing with Agent Browser before adding voice capabilities.

## User Story

As a knowledge worker with an Obsidian vault
I want to chat with an AI agent about my notes
So that I can quickly find and understand information without manual searching

## Problem Statement

The backend has search tools implemented but no agent to orchestrate them. There's no frontend for users to interact with the system. The API routes reference a non-existent `text_agent` module.

## Solution Statement

1. Create a Pydantic AI agent that registers the existing tools and provides a system prompt for knowledge base assistance
2. Build a minimal React + Vite frontend with a chat interface that calls the `/chat` endpoint
3. Enable E2E testing via Agent Browser

## Feature Metadata

**Feature Type**: New Capability
**Estimated Complexity**: Medium
**Primary Systems Affected**: `backend/src/agents/`, `frontend/`
**Dependencies**: pydantic-ai (already in pyproject.toml), React, Vite, TypeScript

---

## CONTEXT REFERENCES

### Relevant Codebase Files - READ BEFORE IMPLEMENTING

- `backend/src/api/routes.py` (lines 1-38) - Why: Shows expected agent interface (`agent.run()` returning `result.output`)
- `backend/src/tools/__init__.py` (lines 1-11) - Why: Exports all tools to register with agent
- `backend/src/tools/search.py` (lines 1-65) - Why: Tool implementations to understand signatures
- `backend/src/tools/documents.py` (lines 1-50) - Why: Document tools to register
- `backend/src/config.py` (lines 1-12) - Why: Settings pattern for any agent config
- `backend/tests/conftest.py` (lines 1-25) - Why: Test fixture pattern for agent tests

### New Files to Create

- `backend/src/agents/__init__.py` - Package init
- `backend/src/agents/text_agent.py` - Pydantic AI agent with tools
- `backend/tests/test_text_agent.py` - Agent integration tests
- `frontend/package.json` - Node dependencies
- `frontend/tsconfig.json` - TypeScript config
- `frontend/vite.config.ts` - Vite configuration
- `frontend/index.html` - Entry HTML
- `frontend/src/main.tsx` - React entry point
- `frontend/src/App.tsx` - Chat interface component
- `frontend/src/App.css` - Minimal styling

### Relevant Documentation - READ BEFORE IMPLEMENTING

- [Pydantic AI Agents](https://ai.pydantic.dev/agents/)
  - Agent creation with `Agent()`, system_prompt, tools registration
  - Why: Core pattern for creating the text agent
- [Pydantic AI Tools](https://ai.pydantic.dev/tools/)
  - `@agent.tool_plain` decorator for tools without context
  - `tools=[]` argument for registering existing functions
  - Why: How to register our existing tool functions

### Patterns to Follow

**Agent Creation (from Pydantic AI docs):**
```python
from pydantic_ai import Agent

agent = Agent(
    'openai:gpt-4o',  # or other model
    system_prompt='You are a helpful assistant...',
    tools=[tool_func1, tool_func2],  # plain functions
)

# Run async
result = await agent.run('user message')
print(result.output)
```

**Tool Registration (existing tools are async functions):**
```python
# Our tools have signatures like:
async def search_documents(query: str, limit: int = 10) -> list[dict]: ...
async def read_document(path: str) -> dict: ...

# Register via tools= argument since they're already defined
agent = Agent(..., tools=[search_documents, read_document, ...])
```

**Test Pattern (from conftest.py):**
```python
@pytest.fixture
def configured_settings(sample_vault, monkeypatch):
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(sample_vault))
    # reload config after env change
```

**React Chat Pattern:**
```tsx
const [messages, setMessages] = useState<Message[]>([]);
const [input, setInput] = useState('');

const sendMessage = async () => {
  const response = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: input }),
  });
  const data = await response.json();
  // update messages
};
```

---

## IMPLEMENTATION PLAN

### Phase 1: Text Agent

Create the Pydantic AI agent that wraps existing tools.

**Tasks:**
- Create agents package with `__init__.py`
- Implement `text_agent.py` with Agent, system prompt, and tool registration
- Add OPENAI_API_KEY to .env.example

### Phase 2: React Frontend

Create minimal chat interface.

**Tasks:**
- Initialize Vite + React + TypeScript project
- Create chat component with message state
- Style with minimal CSS
- Configure proxy to backend

### Phase 3: Integration & Testing

Connect frontend to backend and add tests.

**Tasks:**
- Add agent tests
- Test full flow with Agent Browser

---

## STEP-BY-STEP TASKS

### Task 1: CREATE `backend/src/agents/__init__.py`

- **IMPLEMENT**: Empty package init, export agent
- **PATTERN**: Standard Python package
- **VALIDATE**: `python -c "from src.agents import agent"`

```python
from src.agents.text_agent import agent

__all__ = ["agent"]
```

### Task 2: CREATE `backend/src/agents/text_agent.py`

- **IMPLEMENT**: Pydantic AI agent with system prompt and tools
- **PATTERN**: Follow Pydantic AI docs - use `tools=[]` argument
- **IMPORTS**: `from pydantic_ai import Agent`, tools from `src.tools`
- **GOTCHA**: Tools are async - Pydantic AI handles this automatically
- **GOTCHA**: Need to set model via environment or explicit string
- **VALIDATE**: `cd backend && uv run python -c "from src.agents.text_agent import agent; print(agent)"`

```python
from pydantic_ai import Agent

from src.tools import (
    search_documents,
    find_files,
    search_content,
    read_document,
    get_document_metadata,
)

SYSTEM_PROMPT = """You are a helpful assistant for searching and retrieving information from an Obsidian knowledge base.

You have access to these tools:
- search_documents: Full-text search across all documents
- find_files: Find files matching glob patterns (e.g., '**/daily/*.md')
- search_content: Search for regex patterns within files
- read_document: Read the full content of a specific document
- get_document_metadata: Get metadata (tags, dates) without full content

When answering questions:
1. Use search_documents for general queries
2. Use read_document to get full content when needed
3. Summarize relevant information clearly
4. Cite document paths when referencing specific notes
"""

agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt=SYSTEM_PROMPT,
    tools=[
        search_documents,
        find_files,
        search_content,
        read_document,
        get_document_metadata,
    ],
)
```

### Task 3: UPDATE `backend/.env.example`

- **IMPLEMENT**: Add OPENAI_API_KEY placeholder
- **VALIDATE**: `cat backend/.env.example`

```
OBSIDIAN_VAULT_PATH=/path/to/your/obsidian/vault
INDEX_PATH=.vault_index
OPENAI_API_KEY=sk-your-api-key-here
```

### Task 4: CREATE `frontend/package.json`

- **IMPLEMENT**: Minimal Vite + React + TypeScript setup
- **PATTERN**: Standard Vite React template
- **VALIDATE**: `cd frontend && pnpm install`

```json
{
  "name": "obsidian-voice-agent-frontend",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5",
    "@vitejs/plugin-react": "^4.3.4",
    "typescript": "~5.6.2",
    "vite": "^6.0.5"
  }
}
```

### Task 5: CREATE `frontend/tsconfig.json`

- **IMPLEMENT**: TypeScript config for React
- **VALIDATE**: File exists and is valid JSON

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}
```

### Task 6: CREATE `frontend/vite.config.ts`

- **IMPLEMENT**: Vite config with proxy to backend
- **PATTERN**: Proxy /api to localhost:8000
- **VALIDATE**: `cd frontend && pnpm run build` (after deps installed)

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
```

### Task 7: CREATE `frontend/index.html`

- **IMPLEMENT**: Entry HTML file
- **VALIDATE**: File exists

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Obsidian Voice Agent</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

### Task 8: CREATE `frontend/src/main.tsx`

- **IMPLEMENT**: React entry point
- **VALIDATE**: `cd frontend && pnpm run build`

```tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import './App.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

### Task 9: CREATE `frontend/src/App.tsx`

- **IMPLEMENT**: Chat interface with message state, input, send button
- **PATTERN**: Controlled input, fetch to /api/chat
- **GOTCHA**: Handle loading state, errors
- **VALIDATE**: Visual inspection after `pnpm run dev`

```tsx
import { useState, FormEvent } from 'react'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

export default function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const sendMessage = async (e: FormEvent) => {
    e.preventDefault()
    if (!input.trim() || loading) return

    const userMessage = input.trim()
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }])
    setLoading(true)

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
      })
      const data = await response.json()
      setMessages((prev) => [...prev, { role: 'assistant', content: data.response }])
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', content: 'Error: Failed to get response' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="chat-container">
      <h1>Obsidian Voice Agent</h1>
      <div className="messages">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <strong>{msg.role === 'user' ? 'You' : 'Agent'}:</strong> {msg.content}
          </div>
        ))}
        {loading && <div className="message assistant loading">Thinking...</div>}
      </div>
      <form onSubmit={sendMessage} className="input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about your notes..."
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>
          Send
        </button>
      </form>
    </div>
  )
}
```

### Task 10: CREATE `frontend/src/App.css`

- **IMPLEMENT**: Minimal chat styling
- **VALIDATE**: Visual inspection

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: #1a1a1a;
  color: #fff;
  min-height: 100vh;
}

.chat-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #3b82f6;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  background: #2a2a2a;
  border-radius: 8px;
  margin-bottom: 20px;
}

.message {
  padding: 12px;
  margin-bottom: 10px;
  border-radius: 8px;
  white-space: pre-wrap;
}

.message.user {
  background: #3b82f6;
  margin-left: 20%;
}

.message.assistant {
  background: #374151;
  margin-right: 20%;
}

.message.loading {
  opacity: 0.7;
  font-style: italic;
}

.input-form {
  display: flex;
  gap: 10px;
}

.input-form input {
  flex: 1;
  padding: 12px;
  border: none;
  border-radius: 8px;
  background: #2a2a2a;
  color: #fff;
  font-size: 16px;
}

.input-form input:focus {
  outline: 2px solid #3b82f6;
}

.input-form button {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  background: #3b82f6;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.input-form button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.input-form button:hover:not(:disabled) {
  background: #2563eb;
}
```

### Task 11: CREATE `backend/tests/test_text_agent.py`

- **IMPLEMENT**: Basic agent test using TestModel
- **PATTERN**: Mirror existing test structure from test_tools.py
- **IMPORTS**: Agent from src.agents, TestModel from pydantic_ai
- **VALIDATE**: `cd backend && uv run pytest tests/test_text_agent.py -v`

```python
import pytest
from pydantic_ai.models.test import TestModel


class TestTextAgent:
    async def test_agent_responds(self, configured_settings):
        from src.tools.index import build_index
        from src.agents import agent

        build_index()

        # Use TestModel to avoid real API calls
        test_model = TestModel()
        result = await agent.run("What notes do I have?", model=test_model)

        assert result.output is not None

    async def test_agent_has_tools(self):
        from src.agents import agent

        # Verify tools are registered
        tool_names = [t.name for t in agent._function_tools.values()]
        assert "search_documents" in tool_names
        assert "read_document" in tool_names
```

---

## TESTING STRATEGY

### Unit Tests

- Test agent creation and tool registration
- Use `TestModel` from pydantic_ai to avoid real API calls
- Follow existing pytest-asyncio patterns

### Integration Tests

- Test `/chat` endpoint with mocked agent
- Test frontend build succeeds

### E2E Tests (Agent Browser)

After implementation, use Agent Browser to:
1. Open frontend at `http://localhost:5173`
2. Type a message in the input
3. Click Send
4. Verify response appears

---

## VALIDATION COMMANDS

### Level 1: Syntax & Style

```bash
cd backend && uv run ruff check src/agents/
cd backend && uv run ruff format --check src/agents/
cd frontend && pnpm run build
```

### Level 2: Unit Tests

```bash
cd backend && uv run pytest tests/test_text_agent.py -v
```

### Level 3: Integration Tests

```bash
# Start backend
cd backend && uv run uvicorn src.api.routes:app --reload &

# Test health endpoint
curl http://localhost:8000/health

# Test chat endpoint (requires OPENAI_API_KEY)
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

### Level 4: Manual Validation

```bash
# Terminal 1: Start backend
cd backend && uv run uvicorn src.api.routes:app --reload

# Terminal 2: Start frontend
cd frontend && pnpm run dev

# Open http://localhost:5173 in browser
# Type a message and verify response
```

### Level 5: Agent Browser E2E

```bash
agent-browser open http://localhost:5173
agent-browser snapshot -i
agent-browser fill @input "What notes do I have about Python?"
agent-browser click @send-button
agent-browser wait --text "Agent:"
agent-browser snapshot
```

---

## ACCEPTANCE CRITERIA

- [ ] `backend/src/agents/text_agent.py` exists with Agent configured
- [ ] Agent has all 5 tools registered (search_documents, find_files, search_content, read_document, get_document_metadata)
- [ ] `/chat` endpoint returns responses (with valid OPENAI_API_KEY)
- [ ] Frontend builds without errors (`pnpm run build`)
- [ ] Frontend displays chat interface with input and messages
- [ ] Messages sent from frontend appear in UI
- [ ] Agent responses appear in UI
- [ ] All existing tests still pass
- [ ] New agent tests pass with TestModel

---

## COMPLETION CHECKLIST

- [ ] All tasks completed in order
- [ ] Backend agent imports work: `from src.agents import agent`
- [ ] Frontend builds: `cd frontend && pnpm run build`
- [ ] Backend tests pass: `cd backend && uv run pytest`
- [ ] Ruff passes: `cd backend && uv run ruff check`
- [ ] Manual testing confirms chat works
- [ ] Agent Browser E2E validates full flow

---

## NOTES

### Design Decisions

1. **Model choice**: Using `openai:gpt-4o-mini` for cost efficiency during development. Can be changed via environment variable later.

2. **Tool registration**: Using `tools=[]` argument rather than decorators since tools already exist as standalone functions.

3. **Frontend simplicity**: Minimal React without additional libraries (no Tailwind, no component library) to keep bundle small and setup simple.

4. **Proxy configuration**: Frontend proxies `/api/*` to backend to avoid CORS issues during development.

### Risks

1. **API Key requirement**: Agent won't work without valid OPENAI_API_KEY. Tests use TestModel to avoid this.

2. **Index must exist**: Agent tools require Whoosh index. May need to call `/index/rebuild` first.

### Future Enhancements

- Add streaming responses
- Add conversation history persistence
- Add model selection UI
- Add error boundary in React
