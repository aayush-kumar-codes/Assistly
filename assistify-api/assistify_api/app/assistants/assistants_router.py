from fastapi import APIRouter, Depends, HTTPException, Path

from assistify_api.database.models.user import User

from ..auth.verify_token import verify_token
from .assistants_service import AssistantsService
from .list_assistants_response import AssistantResponse, ListAssistantsResponse

router = APIRouter(prefix="/api/assistants")


@router.get("/")
@router.get("")
def get_assistants(
    assistants_service: AssistantsService = Depends(AssistantsService),
    _: User = Depends(verify_token),
) -> ListAssistantsResponse:
    return assistants_service.get_assistants()


@router.get("/{assistant_id}")
@router.get("/{assistant_id}/")
def get_assistant(
    assistant_id: str = Path(..., description="The ID of the assistant to retrieve"),
    assistants_service: AssistantsService = Depends(AssistantsService),
    _: User = Depends(verify_token),
) -> AssistantResponse:
    assistants = assistants_service.get_assistants().assistants
    matching_assistants = list(filter(lambda x: str(x.id) == assistant_id, assistants))

    if matching_assistants:
        return matching_assistants[0]

    raise HTTPException(status_code=404, detail="Assistant not found")
