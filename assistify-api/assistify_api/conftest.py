from dataclasses import dataclass
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from pymongo.database import Database

from assistify_api.app.users.users_service import UsersService
from assistify_api.database.dao.assistants_dao import AssistantsDao
from assistify_api.database.dao.users_dao import UsersDao
from assistify_api.database.models.assistant import Assistant
from assistify_api.database.models.thread import Thread
from assistify_api.database.models.user import User

from .app.api import api
from .app.assistants.assistants_service import AssistantsService
from .app.dependencies.api_dependencies import get_messages_service, get_openai_client, get_threads_service
from .database.handle_migrations import run_migrations
from .database.mongodb import MongoDb
from .env_variables import set_env_variables

default_user_id = "test_user_id"

mock_idinfo = {
    "iss": "accounts.google.com",
    "sub": "123456789",
    "email": "test@example.com",
    "name": "test name",
    "given_name": "test given name",
    "family_name": "test family name",
    "picture": "test picture",
}

default_assistant_dict = {
    "name": "test_assistant_name",
    "assistant_id": "default_id",
    "model": "gpt-4o",
    "status": "Private",
    "image": "",
}


@dataclass
class TestClientWithMocks:
    api_client: TestClient
    mock_messages_service: MagicMock
    mock_threads_service: MagicMock
    mock_openai_client: MagicMock


@pytest.fixture
def test_client_with_mocks():
    """
    Fixture to provide a TestClient instance with mocked dependencies for the API.

    Mocks the chat service and OpenAI client dependencies, sets environment variables
    from a test-specific .env file, and yields a TestClientWithMocks instance.

    Yields:
        TestClientWithMocks: The TestClient instance and its associated mocks.
    """
    mock_messages_service = MagicMock()
    mock_threads_service = MagicMock()
    mock_openai_client = MagicMock()

    api.dependency_overrides[get_messages_service] = lambda: mock_messages_service
    api.dependency_overrides[get_threads_service] = lambda: mock_threads_service
    api.dependency_overrides[get_openai_client] = lambda: mock_openai_client

    set_env_variables(".env.test")

    with TestClient(api) as api_client:
        yield TestClientWithMocks(
            api_client=api_client,
            mock_messages_service=mock_messages_service,
            mock_threads_service=mock_threads_service,
            mock_openai_client=mock_openai_client,
        )

    api.dependency_overrides[get_messages_service] = get_messages_service
    api.dependency_overrides[get_threads_service] = get_threads_service
    api.dependency_overrides[get_openai_client] = get_openai_client


@pytest.fixture
def mongo_db() -> Database:
    """
    Fixture to provide a fresh MongoDB instance for testing.

    Sets environment variables from a test-specific .env file, forces a new MongoDB instance,
    drops all collections to start fresh, runs migrations, and returns the database instance.

    Returns:
        Database: The MongoDB instance.
    """
    set_env_variables(".env.test")

    _mongo_db = MongoDb.instance(force=True)

    # Drop all collections to start fresh
    [_mongo_db.drop_collection(collection_name) for collection_name in _mongo_db.list_collection_names()]

    run_migrations("assistify_api/database/migrations")
    return _mongo_db


@pytest.fixture
def mock_openai_client():
    return MagicMock()


@pytest.fixture
def assistants_service(
    mock_openai_client,
):
    return AssistantsService(open_ai_client=mock_openai_client, assistants_dao=MagicMock())


@pytest.fixture
def users_service():
    return UsersService(
        assistants_dao=MagicMock(),
        threads_dao=MagicMock(),
        users_dao=MagicMock(),
    )


@pytest.fixture
def default_thread(mongo_db: MongoDb) -> Thread:
    users_dao = UsersDao(mongo_db)
    users_dao.upsert(User(email=default_user_id, name="user name"))

    assistants_dao = AssistantsDao(mongo_db)
    assistant = assistants_dao.find_all(model_class=Assistant)[0]

    return Thread(
        user_id=default_user_id,
        assistant_id=str(assistant.id),
        assistant_name=assistant.name,
        model=assistant.model,
        provider=assistant.provider,
        provider_thread_id="test_provider_thread_id",
    )
