from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from livekit import api
from pydantic import BaseModel

load_dotenv()

from src.agents.text_agent import agent  # noqa: E402
from src.config import settings  # noqa: E402
from src.tools.index import build_index  # noqa: E402

app = FastAPI(title="Obsidian Voice Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class TokenRequest(BaseModel):
    room_name: str
    participant_name: str


class TokenResponse(BaseModel):
    token: str


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    result = await agent.run(request.message, model="openai:gpt-4o-mini")
    return ChatResponse(response=result.output)


@app.post("/livekit-token", response_model=TokenResponse)
async def livekit_token(request: TokenRequest) -> TokenResponse:
    token = (
        api.AccessToken(settings.livekit_api_key, settings.livekit_api_secret)
        .with_identity(request.participant_name)
        .with_grants(api.VideoGrants(room_join=True, room=request.room_name, can_publish=True))
    )
    return TokenResponse(token=token.to_jwt())


@app.post("/index/rebuild")
async def rebuild_index():
    build_index()
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok"}
