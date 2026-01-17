import frontmatter

from src.config import settings


async def read_document(path: str) -> dict:
    """Read the full content of a markdown document.

    Args:
        path: Relative path to the document within the vault

    Returns:
        Document content with path, title, content, and metadata
    """
    full_path = settings.obsidian_vault_path / path

    if not full_path.exists():
        return {"error": "File not found", "path": path}

    try:
        post = frontmatter.load(full_path)
        return {
            "path": path,
            "title": post.get("title", full_path.stem),
            "content": post.content,
            "metadata": dict(post.metadata),
        }
    except Exception as e:
        return {"error": str(e), "path": path}


async def get_document_metadata(path: str) -> dict:
    """Get metadata for a document without full content.

    Args:
        path: Relative path to the document within the vault

    Returns:
        Document metadata including title, tags, and timestamps
    """
    full_path = settings.obsidian_vault_path / path

    if not full_path.exists():
        return {"error": "File not found", "path": path}

    try:
        post = frontmatter.load(full_path)
        stat = full_path.stat()
        return {
            "path": path,
            "title": post.get("title", full_path.stem),
            "tags": post.get("tags", []),
            "created": stat.st_ctime,
            "modified": stat.st_mtime,
        }
    except Exception as e:
        return {"error": str(e), "path": path}
