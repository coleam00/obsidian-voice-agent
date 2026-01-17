import json

from dotenv import load_dotenv
from livekit.agents import Agent, AgentServer, AgentSession, JobContext, function_tool, RunContext
from livekit.plugins.openai import realtime

load_dotenv()

from src.tools import (  # noqa: E402
    search_documents,
    find_files,
    search_content,
    read_document,
    get_document_metadata,
)

SYSTEM_PROMPT = """You are a helpful voice assistant for searching and retrieving information from an Obsidian knowledge base.

You have access to these tools:
- search_documents: Full-text search across all documents
- find_files: Find files matching glob patterns (e.g., '**/daily/*.md')
- search_content: Search for regex patterns within files
- read_document: Read the full content of a specific document
- get_document_metadata: Get metadata (tags, dates) without full content

When answering questions:
1. Use search_documents for general queries
2. Use read_document to get full content when needed
3. Summarize relevant information clearly and concisely for voice
4. Keep responses conversational and brief
"""


class ObsidianVoiceAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=SYSTEM_PROMPT,
            llm=realtime.RealtimeModel(model="gpt-realtime-mini"),
        )

    async def _send_file_references(self, ctx: RunContext, files: list[dict]) -> None:
        if not files:
            return
        payload = json.dumps({"files": files[:10]})  # Limit to 10 files
        try:
            room = ctx.session.room_io.room
            for participant in room.remote_participants.values():
                await room.local_participant.perform_rpc(
                    destination_identity=participant.identity,
                    method="showReferencedFiles",
                    payload=payload,
                )
        except Exception:
            pass  # RPC failures shouldn't break the agent

    @function_tool
    async def search_documents_tool(
        self, ctx: RunContext, query: str, limit: int = 10
    ) -> list[dict]:
        """Full-text search across all documents in the vault."""
        results = await search_documents(query, limit)
        await self._send_file_references(ctx, results)
        return results

    @function_tool
    async def find_files_tool(self, ctx: RunContext, pattern: str) -> list[dict]:
        """Find files matching a glob pattern."""
        results = await find_files(pattern)
        await self._send_file_references(ctx, results)
        return results

    @function_tool
    async def search_content_tool(
        self, ctx: RunContext, pattern: str, file_pattern: str = "**/*.md"
    ) -> list[dict]:
        """Search for regex pattern within file contents."""
        results = await search_content(pattern, file_pattern)
        await self._send_file_references(ctx, results)
        return results

    @function_tool
    async def read_document_tool(self, ctx: RunContext, path: str) -> dict:
        """Read the full content of a markdown document."""
        result = await read_document(path)
        if "error" not in result:
            await self._send_file_references(ctx, [result])
        return result

    @function_tool
    async def get_document_metadata_tool(self, ctx: RunContext, path: str) -> dict:
        """Get metadata for a document without full content."""
        result = await get_document_metadata(path)
        if "error" not in result:
            await self._send_file_references(ctx, [result])
        return result


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext) -> None:
    await ctx.connect()
    session = AgentSession()
    await session.start(ObsidianVoiceAgent(), room=ctx.room)


if __name__ == "__main__":
    from livekit.agents.cli import run_app
    run_app(server)
