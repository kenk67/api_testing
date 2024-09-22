from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    api_key: str

@lru_cache(maxsize=1)  # Cache the settings, with a maximum of one setting
def get_settings() -> Settings:
    return Settings()
