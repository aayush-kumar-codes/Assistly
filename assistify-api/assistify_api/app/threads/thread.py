from typing import Literal

from pydantic import BaseModel

from assistify_api.database.models.message import Message


class ThreadRequest(BaseModel):
    assistant_id: str
    assistant_name: str
    model: str
    provider: Literal["OpenAI"]


class ThreadResponse(BaseModel):
    id: str
    user_id: str

    assistant_id: str
    assistant_name: str
    is_welcome_thread: bool
    model: str
    provider: Literal["OpenAI"]
    provider_thread_id: str
    summary: str

    messages: list[Message]
