# Feature: Read-Only Tools Layer for Obsidian Search

The following plan should be complete, but validate documentation and codebase patterns before implementing.

## Feature Description

Create a shared, framework-agnostic tools layer that enables both LiveKit (voice) and Pydantic AI (text) agents to search, read, and summarize documents from an Obsidian vault. Tools are pure async Python functions that can be wrapped by either agent framework.

## User Story

As a knowledge worker with an Obsidian vault
I want to ask questions about my notes via voice or text
So that I can quickly find and understand information without manual searching

## Problem Statement

Both the voice agent (LiveKit) and text agent (Pydantic AI) need to search through Obsidian markdown files. Without a shared tools layer, we'd duplicate search logic across frameworks, making maintenance difficult and behavior inconsistent.

## Solution Statement

Build framework-agnostic async Python functions for:
1. **Full-text search** - Whoosh-indexed search across all markdown content
2. **File discovery** - Glob patterns to find files by name/path
3. **Content search** - Regex pattern matching within files
4. **Document reading** - Retrieve full content of specific files
5. **Summarization** - LLM-powered document summaries

These functions return simple data structures (dicts, lists, strings) that both LiveKit's `@function_tool` and Pydantic AI's `@agent.tool` can wrap.

## Feature Metadata

**Feature Type**: New Capability
**Estimated Complexity**: Medium
**Primary Systems Affected**: backend/src/tools/
**Dependencies**: whoosh, pathlib, re (stdlib), pydantic

---

## CONTEXT REFERENCES

### Relevant Documentation - READ BEFORE IMPLEMENTING

- [Whoosh Documentation](https://whoosh.readthedocs.io/en/latest/quickstart.html)
  - Schema definition, indexing, and searching
  - Why: Core full-text search implementation

- [LiveKit Function Tools](https://docs.livekit.io/agents/voice-agent/function-calling/)
  - `@function_tool` decorator pattern
  - Why: Shows how to wrap tools for voice agent

- [Pydantic AI Tools](https://ai.pydantic.dev/tools/)
  - `@agent.tool` and `@agent.tool_plain` decorators
  - Why: Shows how to wrap tools for text agent

### New Files to Create

- `backend/src/tools/__init__.py` - Tool exports
- `backend/src/tools/search.py` - Search tools (full-text, glob, regex)
- `backend/src/tools/documents.py` - Document reading tools
- `backend/src/tools/index.py` - Whoosh index management
- `backend/src/config.py` - Configuration (vault path, index path)
- `backend/pyproject.toml` - Dependencies
- `backend/.env.example` - Environment template
- `backend/tests/test_tools.py` - Tool unit tests

### Patterns to Follow

**Tool Function Pattern:**
```python
async def tool_name(param: str) -> dict[str, Any]:
    """Tool description for LLM.
    
    Args:
        param: Description of parameter
        
    Returns:
        Dictionary with result data
    """
    # Implementation
    return {"key": "value"}
```

**Pydantic Models for Results:**
```python
class SearchResult(BaseModel):
    path: str
    title: str
    snippet: str
    score: float
```

**Error Handling:**
```python
# Return error info in result, don't raise exceptions
# This lets the LLM understand what went wrong
return {"error": "File not found", "path": requested_path}
```

---

## IMPLEMENTATION PLAN

### Phase 1: Project Setup

Set up Python project structure with dependencies.

**Tasks:**
- Create directory structure
- Initialize pyproject.toml with dependencies
- Create configuration module
- Set up environment variables

### Phase 2: Index Management

Build Whoosh index for full-text search.

**Tasks:**
- Define Whoosh schema for markdown documents
- Create index builder that scans vault
- Add incremental update capability

### Phase 3: Search Tools

Implement the three search strategies.

**Tasks:**
- Full-text search via Whoosh
- File discovery via glob patterns
- Content search via regex

### Phase 4: Document Tools

Implement document reading and summarization.

**Tasks:**
- Read document by path
- Get document metadata (frontmatter)
- List recent/related documents

### Phase 5: Testing

Validate tools work correctly.

**Tasks:**
- Unit tests for each tool
- Integration test with sample vault

---

## STEP-BY-STEP TASKS

### CREATE backend/pyproject.toml

- **IMPLEMENT**: Project configuration with dependencies
- **DEPENDENCIES**: whoosh, pydantic, pydantic-settings, python-frontmatter, pytest, pytest-asyncio, ruff
- **VALIDATE**: `cd backend && uv sync`

```toml
[project]
name = "obsidian-voice-agent"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "whoosh>=2.7.4",
    "pydantic>=2.0",
    "pydantic-settings>=2.0",
    "python-frontmatter>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "ruff>=0.4",
]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.pytest.ini_options]
asyncio_mode = "auto"
```

### CREATE backend/src/config.py

- **IMPLEMENT**: Configuration using pydantic-settings
- **PATTERN**: Load from environment variables with sensible defaults
- **VALIDATE**: `cd backend && uv run python -c "from src.config import settings; print(settings)"`

```python
from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    obsidian_vault_path: Path
    index_path: Path = Path(".vault_index")
    
    model_config = {"env_file": ".env"}

settings = Settings()
```

### CREATE backend/.env.example

- **IMPLEMENT**: Environment variable template
- **VALIDATE**: File exists with documented variables

```
OBSIDIAN_VAULT_PATH=/path/to/your/obsidian/vault
INDEX_PATH=.vault_index
```

### CREATE backend/src/__init__.py

- **IMPLEMENT**: Empty init file for package
- **VALIDATE**: `cd backend && uv run python -c "import src"`

### CREATE backend/src/tools/__init__.py

- **IMPLEMENT**: Export all tool functions
- **VALIDATE**: `cd backend && uv run python -c "from src.tools import search_documents, find_files, read_document"`

```python
from src.tools.search import search_documents, find_files, search_content
from src.tools.documents import read_document, get_document_metadata

__all__ = [
    "search_documents",
    "find_files",
    "search_content",
    "read_document",
    "get_document_metadata",
]
```

### CREATE backend/src/tools/index.py

- **IMPLEMENT**: Whoosh index management
- **PATTERN**: Schema with path, title, content, modified date
- **GOTCHA**: Index creation is sync, wrap for async if needed
- **VALIDATE**: `cd backend && uv run python -c "from src.tools.index import build_index; build_index()"`

Key implementation points:
- Schema: path (ID), title (TEXT), content (TEXT), modified (DATETIME)
- build_index() scans vault and creates/updates index
- get_index() returns existing index for searching
- Handle frontmatter extraction for title

### CREATE backend/src/tools/search.py

- **IMPLEMENT**: Three search functions
- **PATTERN**: Return list of dicts with path, title, snippet, score
- **GOTCHA**: Whoosh search is sync, use asyncio.to_thread()
- **VALIDATE**: `cd backend && uv run pytest tests/test_tools.py::test_search -v`

Functions to implement:

1. `search_documents(query: str, limit: int = 10) -> list[dict]`
   - Full-text search using Whoosh
   - Returns matches with snippets and relevance scores

2. `find_files(pattern: str) -> list[dict]`
   - Glob pattern matching on file paths
   - Example: `**/daily/*.md`, `*recipe*`

3. `search_content(pattern: str, file_pattern: str = "**/*.md") -> list[dict]`
   - Regex search within file contents
   - Returns matches with line numbers and context

### CREATE backend/src/tools/documents.py

- **IMPLEMENT**: Document reading functions
- **PATTERN**: Return dict with content, metadata, error handling
- **GOTCHA**: Handle missing files gracefully, return error in result
- **VALIDATE**: `cd backend && uv run pytest tests/test_tools.py::test_documents -v`

Functions to implement:

1. `read_document(path: str) -> dict`
   - Read full content of a markdown file
   - Returns: {"path": str, "title": str, "content": str, "metadata": dict}

2. `get_document_metadata(path: str) -> dict`
   - Extract frontmatter and basic info without full content
   - Returns: {"path": str, "title": str, "tags": list, "created": str, "modified": str}

### CREATE backend/tests/__init__.py

- **IMPLEMENT**: Empty init for tests package
- **VALIDATE**: File exists

### CREATE backend/tests/conftest.py

- **IMPLEMENT**: Pytest fixtures for testing
- **PATTERN**: Create temp vault with sample markdown files
- **VALIDATE**: `cd backend && uv run pytest --collect-only`

```python
import pytest
from pathlib import Path
import tempfile
import shutil

@pytest.fixture
def sample_vault(tmp_path):
    """Create a temporary vault with sample documents."""
    vault = tmp_path / "vault"
    vault.mkdir()
    
    # Create sample files
    (vault / "note1.md").write_text("# First Note\n\nThis is about Python programming.")
    (vault / "note2.md").write_text("---\ntags: [recipe]\n---\n# Pasta Recipe\n\nBoil water...")
    (vault / "daily").mkdir()
    (vault / "daily/2024-01-01.md").write_text("# Daily Note\n\nToday I learned about Whoosh.")
    
    return vault

@pytest.fixture
def configured_settings(sample_vault, monkeypatch):
    """Configure settings to use sample vault."""
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(sample_vault))
    monkeypatch.setenv("INDEX_PATH", str(sample_vault / ".index"))
    
    # Reimport to pick up new env vars
    from src.config import Settings
    return Settings()
```

### CREATE backend/tests/test_tools.py

- **IMPLEMENT**: Unit tests for all tools
- **PATTERN**: Test happy path and error cases
- **VALIDATE**: `cd backend && uv run pytest tests/test_tools.py -v`

Test cases:
- `test_search_documents_finds_matches` - Full-text search returns results
- `test_search_documents_no_matches` - Empty query returns empty list
- `test_find_files_glob_pattern` - Glob finds matching files
- `test_find_files_no_matches` - Non-matching pattern returns empty
- `test_search_content_regex` - Regex finds content matches
- `test_read_document_exists` - Reading existing file returns content
- `test_read_document_not_found` - Missing file returns error dict
- `test_get_document_metadata` - Extracts frontmatter correctly

---

## TESTING STRATEGY

### Unit Tests

Each tool function tested in isolation with sample vault fixture.

### Integration Tests

Test index building and searching together with realistic vault structure.

### Edge Cases

- Empty vault
- Files with no frontmatter
- Binary files in vault (should be skipped)
- Very large files
- Unicode content
- Special characters in filenames

---

## VALIDATION COMMANDS

### Level 1: Syntax & Style

```bash
cd backend && uv run ruff check src/ tests/
cd backend && uv run ruff format --check src/ tests/
```

### Level 2: Type Checking (optional)

```bash
cd backend && uv run mypy src/ --ignore-missing-imports
```

### Level 3: Unit Tests

```bash
cd backend && uv run pytest tests/ -v
```

### Level 4: Manual Validation

```bash
# Set up real vault path
export OBSIDIAN_VAULT_PATH=/path/to/your/vault

# Test index building
cd backend && uv run python -c "from src.tools.index import build_index; build_index()"

# Test search
cd backend && uv run python -c "
from src.tools import search_documents
import asyncio
results = asyncio.run(search_documents('python'))
print(results)
"
```

---

## ACCEPTANCE CRITERIA

- [ ] All tool functions are async and return dicts/lists
- [ ] Whoosh index builds successfully from vault
- [ ] Full-text search returns relevant results with snippets
- [ ] Glob pattern search finds files by path
- [ ] Regex search finds content within files
- [ ] Document reading handles missing files gracefully
- [ ] All unit tests pass
- [ ] Code passes ruff linting
- [ ] Tools are framework-agnostic (no LiveKit/Pydantic AI imports)

---

## COMPLETION CHECKLIST

- [ ] All files created in correct locations
- [ ] Dependencies install successfully with `uv sync`
- [ ] Index builds from sample vault
- [ ] All 8+ unit tests pass
- [ ] Ruff linting passes
- [ ] Manual validation with real vault works
- [ ] Tools ready for agent integration

---

## NOTES

### Design Decisions

1. **Async functions**: Even though Whoosh is sync, we wrap with `asyncio.to_thread()` for consistency with agent frameworks.

2. **Dict returns over Pydantic models**: Simpler for agent frameworks to serialize. Can add models later if needed.

3. **Error in result vs exceptions**: Returning `{"error": "..."}` lets the LLM understand failures and potentially retry or ask for clarification.

4. **Index path in vault**: Storing `.vault_index` alongside vault keeps things simple for local use.

### Future Enhancements

- Incremental index updates (watch for file changes)
- Semantic search with embeddings
- Link/backlink traversal
- Tag-based filtering
