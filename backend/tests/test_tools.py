class TestSearchDocuments:
    async def test_search_documents_finds_matches(self, configured_settings):
        from src.tools.index import build_index
        from src.tools import search_documents

        build_index()
        results = await search_documents("Python")

        assert len(results) >= 1
        assert any("note1" in r["path"] for r in results)

    async def test_search_documents_no_matches(self, configured_settings):
        from src.tools.index import build_index
        from src.tools import search_documents

        build_index()
        results = await search_documents("xyznonexistent")

        assert results == []


class TestFindFiles:
    async def test_find_files_glob_pattern(self, configured_settings):
        from src.tools import find_files

        results = await find_files("**/daily/*.md")

        assert len(results) == 1
        assert "daily/2024-01-01.md" in results[0]["path"]

    async def test_find_files_no_matches(self, configured_settings):
        from src.tools import find_files

        results = await find_files("**/nonexistent/*.md")

        assert results == []


class TestSearchContent:
    async def test_search_content_regex(self, configured_settings):
        from src.tools import search_content

        results = await search_content("Whoosh")

        assert len(results) >= 1
        assert any("daily" in r["path"] for r in results)


class TestReadDocument:
    async def test_read_document_exists(self, configured_settings):
        from src.tools import read_document

        result = await read_document("note1.md")

        assert "error" not in result
        assert result["path"] == "note1.md"
        assert "Python" in result["content"]

    async def test_read_document_not_found(self, configured_settings):
        from src.tools import read_document

        result = await read_document("nonexistent.md")

        assert "error" in result
        assert result["path"] == "nonexistent.md"


class TestGetDocumentMetadata:
    async def test_get_document_metadata(self, configured_settings):
        from src.tools import get_document_metadata

        result = await get_document_metadata("note2.md")

        assert "error" not in result
        assert result["tags"] == ["recipe"]
