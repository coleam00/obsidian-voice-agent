import pytest
from pydantic_ai.models.test import TestModel


class TestTextAgent:
    @pytest.mark.asyncio
    async def test_agent_responds(self, configured_settings):
        from src.tools.index import build_index
        from src.agents import agent

        build_index()

        test_model = TestModel()
        result = await agent.run("What notes do I have?", model=test_model)

        assert result.output is not None

    @pytest.mark.asyncio
    async def test_agent_has_tools(self):
        from src.agents import agent

        tool_names = list(agent._function_toolset.tools)
        assert "search_documents" in tool_names
        assert "read_document" in tool_names
