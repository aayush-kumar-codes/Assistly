from typing import Literal

from pydantic import Field

from .base import Base


class Assistant(Base):
    assistant_id: str  # ID from OpenAI or other service
    image: str = Field(default="")
    is_available: bool = True
    model: str  # e.g., gpt-4o
    name: str
    provider: Literal["OpenAI"] = Field(default="OpenAI", alias="provider")
    status: Literal["Public", "Market", "Private"] = Field(default="Private", alias="status")
    summary_full: str = Field(default="")
    summary_short: str = Field(default="")

    # tracking
    thread_ids: list[str] = Field(default_factory=list)
    token_count: int = 0
