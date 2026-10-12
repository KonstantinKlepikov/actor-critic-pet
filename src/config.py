from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Unified Mafia service settings - combines LLM and Game settings."""

    # LLM settings
    ollama_model: str = 'llama3.1:8b'
    ollama_timeout: int = 120
    llm_pool_size: int = 0

    log_level: str = 'INFO'

    model_config = SettingsConfigDict(env_prefix='', extra='ignore')


settings = Settings()
