from ai_assistant_manager.chats.chat import Chat
from ai_assistant_manager.clients.openai_api import OpenAIClient, build_openai_client
from fastapi import Depends

from assistify_api.app.threads.threads_service import ThreadsService
from assistify_api.database.dao.assistants_dao import AssistantsDao
from assistify_api.database.dao.threads_dao import ThreadsDao
from assistify_api.database.dao.users_dao import UsersDao
from assistify_api.database.models.assistant import Assistant

from ..messages.messages_service import MessagesService


def get_openai_client() -> OpenAIClient:
    return OpenAIClient(build_openai_client())


def get_messages_service(
    assistants_dao: AssistantsDao = Depends(AssistantsDao),
    threads_dao: ThreadsDao = Depends(ThreadsDao),
    users_dao: UsersDao = Depends(UsersDao),
) -> MessagesService:
    assistants: Assistant = [
        assistant
        for assistant in assistants_dao.find_all(model_class=Assistant)
        if assistant.assistant_id == hardcoded_assistant_id
    ]

    if len(assistants) == 0:
        raise ValueError("Assistant not found")

    return MessagesService(
        Chat(get_openai_client(), assistants[0].assistant_id), assistants[0], assistants_dao, threads_dao, users_dao
    )


def get_threads_service(
    threads_dao: ThreadsDao = Depends(ThreadsDao),
    assistants_dao: AssistantsDao = Depends(AssistantsDao),
    users_dao: UsersDao = Depends(UsersDao),
) -> ThreadsService:
    return ThreadsService(threads_dao, assistants_dao, users_dao)


# temporary hardcoded assistant id - Assistant Concierge
hardcoded_assistant_id = "asst_1covfp75taVovUbQpoiOyMEL"
