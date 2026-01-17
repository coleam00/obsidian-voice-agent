"""
LiveKit Agents Python SDK v1.3 Example
Shows Agent class with @function_tool decorators, AgentSession setup, and RPC communication
"""

# Essential imports for LiveKit Agents SDK v1.3
from livekit.agents import (
    Agent,
    AgentSession,
    function_tool,
    llm,
    stt,
    tts,
    JobContext,
    WorkerOptions,
)
from livekit.agents.llm import ChatContext, ChatMessage
from livekit.agents.stt import STTCapabilities
from livekit.agents.tts import TTSCapabilities
from livekit import rtc
import asyncio
import logging

logger = logging.getLogger(__name__)


class MyAgent(Agent):
    """Agent class with function tools"""
    
    def __init__(self):
        super().__init__()
        
    @function_tool
    async def get_weather(self, location: str) -> str:
        """Get weather information for a location"""
        # Tool implementation
        return f"Weather in {location}: 72°F, sunny"
    
    @function_tool  
    async def send_notification(self, message: str, user_id: str = None) -> str:
        """Send notification to frontend via RPC"""
        # Send data to frontend via RPC
        if hasattr(self, '_session') and self._session:
            await self._session.room.local_participant.publish_data(
                message.encode(),
                destination_identities=[user_id] if user_id else None
            )
        return f"Notification sent: {message}"
    
    @function_tool
    async def search_documents(self, query: str) -> str:
        """Search through documents"""
        # Document search implementation
        results = f"Found documents matching '{query}'"
        
        # Send results to frontend via RPC
        if hasattr(self, '_session'):
            await self._send_to_frontend({
                "type": "search_results",
                "query": query,
                "results": results
            })
        
        return results
    
    async def _send_to_frontend(self, data: dict):
        """Helper to send data to frontend via RPC"""
        if self._session and self._session.room:
            import json
            await self._session.room.local_participant.publish_data(
                json.dumps(data).encode(),
                reliable=True
            )


async def entrypoint(ctx: JobContext):
    """Main entrypoint for the agent"""
    
    # Initialize STT (Speech-to-Text)
    stt_instance = stt.StreamAdapter(
        stt=stt.DeepgramSTT(
            model="nova-2-general",
            language="en",
        ),
        vad=stt.silero.VAD.load()
    )
    
    # Initialize LLM
    llm_instance = llm.openai.LLM(
        model="gpt-4",
        temperature=0.7,
    )
    
    # Initialize TTS (Text-to-Speech)  
    tts_instance = tts.openai.TTS(
        model="tts-1",
        voice="alloy",
    )
    
    # Create agent instance
    agent = MyAgent()
    
    # Set up AgentSession with STT, LLM, TTS
    session = AgentSession(
        ctx=ctx,
        stt=stt_instance,
        llm=llm_instance, 
        tts=tts_instance,
        agent=agent,
        chat_ctx=ChatContext(
            messages=[
                ChatMessage(
                    role="system",
                    content="You are a helpful assistant with access to tools."
                )
            ]
        )
    )
    
    # Store session reference in agent for RPC communication
    agent._session = session
    
    # Start the session
    await session.astart()


# Worker configuration
if __name__ == "__main__":
    from livekit.agents.cli import run_app
    
    run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=None,  # Optional prewarm function
        )
    )