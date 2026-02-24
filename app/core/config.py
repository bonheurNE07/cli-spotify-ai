import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    database_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings(database_url=os.getenv("DATABASE_URL", ""))
