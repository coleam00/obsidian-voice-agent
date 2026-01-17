from datetime import datetime

from whoosh import index
from whoosh.fields import Schema, TEXT, ID, DATETIME
from whoosh.qparser import QueryParser
import frontmatter

from src.config import settings


SCHEMA = Schema(
    path=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    content=TEXT(stored=True),
    modified=DATETIME(stored=True),
)


def build_index() -> None:
    """Build or rebuild the Whoosh index from the vault."""
    index_path = settings.index_path
    index_path.mkdir(parents=True, exist_ok=True)

    ix = index.create_in(str(index_path), SCHEMA)
    writer = ix.writer()

    vault = settings.obsidian_vault_path
    for md_file in vault.rglob("*.md"):
        try:
            post = frontmatter.load(md_file)
            title = post.get("title", md_file.stem)
            content = post.content
            modified = datetime.fromtimestamp(md_file.stat().st_mtime)

            writer.add_document(
                path=str(md_file.relative_to(vault)),
                title=str(title),
                content=content,
                modified=modified,
            )
        except Exception:
            continue

    writer.commit()


def get_index() -> index.Index:
    """Get the existing Whoosh index."""
    return index.open_dir(str(settings.index_path))


def search_index(query_str: str, limit: int = 10) -> list[dict]:
    """Search the index and return results."""
    ix = get_index()
    results = []

    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        hits = searcher.search(query, limit=limit)

        for hit in hits:
            results.append(
                {
                    "path": hit["path"],
                    "title": hit["title"],
                    "snippet": hit.highlights("content", top=3) or hit["content"][:200],
                    "score": hit.score,
                }
            )

    return results
