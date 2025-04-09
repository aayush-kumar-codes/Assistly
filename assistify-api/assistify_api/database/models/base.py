from datetime import UTC, datetime
from uuid import UUID

from bson import ObjectId
from pydantic import BaseModel, Field


class Base(BaseModel):
    id: UUID = Field(None, alias="_id")

    created: datetime = datetime.now(UTC)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
