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
    system_prompt=SYSTEM_PROMPT,
    tools=[
        search_documents,
        find_files,
        search_content,
        read_document,
        get_document_metadata,
    ],
)
