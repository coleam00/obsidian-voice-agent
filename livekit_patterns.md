# LiveKit Agents SDK v1.3 - Specific Examples

## 1. Agent Class with @function_tool Decorators

```python
from livekit.agents import Agent, function_tool

class MyAgent(Agent):
    @function_tool
    async def calculate(self, expression: str) -> str:
        """Calculate mathematical expressions"""
        try:
            result = eval(expression)  # Use safely in production
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    @function_tool
    async def get_time(self) -> str:
        """Get current time"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

## 2. AgentSession Setup with STT, LLM, TTS

```python
from livekit.agents import AgentSession, JobContext, stt, llm, tts
from livekit.agents.llm import ChatContext, ChatMessage

async def setup_session(ctx: JobContext, agent: Agent):
    # STT Configuration
    stt_instance = stt.StreamAdapter(
        stt=stt.DeepgramSTT(model="nova-2-general"),
        vad=stt.silero.VAD.load()
    )
    
    # LLM Configuration  
    llm_instance = llm.openai.LLM(
        model="gpt-4",
        temperature=0.7
    )
    
    # TTS Configuration
    tts_instance = tts.openai.TTS(
        model="tts-1", 
        voice="alloy"
    )
    
    # Create AgentSession
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
                    content="You are a helpful assistant."
                )
            ]
        )
    )
    
    return session
```

## 3. Send Data to Frontend via RPC from Tool

```python
@function_tool
async def notify_frontend(self, data: dict) -> str:
    """Send data to frontend via RPC"""
    import json
    
    # Method 1: Using room data channel
    if self._session and self._session.room:
        await self._session.room.local_participant.publish_data(
            json.dumps(data).encode(),
            reliable=True,
            destination_identities=None  # Broadcast to all
        )
    
    # Method 2: Using RPC call
    if hasattr(self._session, 'rpc'):
        await self._session.rpc.call(
            method="frontend_update",
            data=data,
            participant_identity="frontend_client"
        )
    
    return "Data sent to frontend"

@function_tool  
async def update_ui(self, component: str, value: str) -> str:
    """Update specific UI component"""
    update_data = {
        "type": "ui_update",
        "component": component,
        "value": value,
        "timestamp": time.time()
    }
    
    # Send via data channel
    await self._send_to_frontend(update_data)
    return f"Updated {component} with {value}"
```

## 4. Complete Minimal Example

```python
from livekit.agents import (
    Agent, AgentSession, function_tool, 
    JobContext, WorkerOptions, stt, llm, tts
)
from livekit.agents.llm import ChatContext, ChatMessage
import json

class MinimalAgent(Agent):
    @function_tool
    async def send_data(self, message: str) -> str:
        """Send data to frontend"""
        data = {"type": "message", "content": message}
        await self._session.room.local_participant.publish_data(
            json.dumps(data).encode()
        )
        return "Sent"

async def entrypoint(ctx: JobContext):
    agent = MinimalAgent()
    
    session = AgentSession(
        ctx=ctx,
        stt=stt.StreamAdapter(stt=stt.DeepgramSTT()),
        llm=llm.openai.LLM(model="gpt-4"),
        tts=tts.openai.TTS(),
        agent=agent
    )
    
    agent._session = session
    await session.astart()

if __name__ == "__main__":
    from livekit.agents.cli import run_app
    run_app(WorkerOptions(entrypoint_fnc=entrypoint))
```