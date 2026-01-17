import asyncio
import re

from src.config import settings
from src.tools.index import search_index


async def search_documents(query: str, limit: int = 10) -> list[dict]:
    """Full-text search across all documents in the vault.

    Args:
        query: Search query string
        limit: Maximum number of results to return

    Returns:
        List of matching documents with path, title, snippet, and score
    """
    return await asyncio.to_thread(search_index, query, limit)


async def find_files(pattern: str) -> list[dict]:
    """Find files matching a glob pattern.

    Args:
        pattern: Glob pattern (e.g., '**/daily/*.md', '*recipe*')

    Returns:
        List of matching files with path and title
    """
    vault = settings.obsidian_vault_path
    results = []

    for path in vault.glob(pattern):
        if path.is_file() and path.suffix == ".md":
            results.append(
                {
                    "path": str(path.relative_to(vault)),
                    "title": path.stem,
                }
            )

    return results


async def search_content(pattern: str, file_pattern: str = "**/*.md") -> list[dict]:
    """Search for regex pattern within file contents.

    Args:
        pattern: Regex pattern to search for
        file_pattern: Glob pattern to filter files

    Returns:
        List of matches with path, line number, and context
    """
    vault = settings.obsidian_vault_path
    results = []
    regex = re.compile(pattern, re.IGNORECASE)

    for path in vault.glob(file_pattern):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
            for i, line in enumerate(content.splitlines(), 1):
                if regex.search(line):
                    results.append(
                        {
                            "path": str(path.relative_to(vault)),
                            "line": i,
                            "content": line.strip(),
                        }
                    )
        except Exception:
            continue

    return results
