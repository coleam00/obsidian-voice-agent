import pytest


class TestVoiceAgentTools:
    """Test voice agent tool wrappers."""

    @pytest.mark.asyncio
    async def test_search_documents_tool(self, configured_settings):
        from src.tools.index import build_index
        from src.tools import search_documents

        build_index()
        results = await search_documents("Python", limit=5)
        assert isinstance(results, list)

    @pytest.mark.asyncio
    async def test_find_files_tool(self, configured_settings):
        from src.tools import find_files

        results = await find_files("**/*.md")
        assert isinstance(results, list)
        assert len(results) > 0

    @pytest.mark.asyncio
    async def test_read_document_tool(self, configured_settings):
        from src.tools import read_document

        result = await read_document("note1.md")
        assert "content" in result
        assert "Python" in result["content"]

    @pytest.mark.asyncio
    async def test_read_document_not_found(self, configured_settings):
        from src.tools import read_document

        result = await read_document("nonexistent.md")
        assert "error" in result

    @pytest.mark.asyncio
    async def test_get_document_metadata_tool(self, configured_settings):
        from src.tools import get_document_metadata

        result = await get_document_metadata("note2.md")
        assert "tags" in result
        assert "recipe" in result["tags"]
