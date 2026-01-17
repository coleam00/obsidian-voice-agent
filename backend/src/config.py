from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    obsidian_vault_path: Path
    index_path: Path = Path(".vault_index")
    livekit_api_key: str = ""
    livekit_api_secret: str = ""
    livekit_url: str = ""

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
