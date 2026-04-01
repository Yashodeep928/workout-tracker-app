from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.base import Base
from app.db.session import get_db
from app.main import app


# This is a separate SQLite database only for tests
# It will create a local file named test_workout_tracker.db
TEST_DATABASE_URL = "sqlite:///./test_workout_tracker.db"


# Create SQLAlchemy engine for test database
# check_same_thread=False is needed for SQLite when used with FastAPI/TestClient
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)


# Create a separate session factory for tests
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# This function will replace the real get_db() during tests
def override_get_db() -> Generator[Session, None, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# This fixture runs before each test function
# It resets the database so every test starts clean
@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    # Drop all tables first to ensure clean state
    Base.metadata.drop_all(bind=engine)

    # Recreate all tables fresh
    Base.metadata.create_all(bind=engine)

    # Create a fresh DB session for this test
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


# This fixture gives us a test client with DB dependency overridden
@pytest.fixture(scope="function")
def client(db_session: Session) -> Generator[TestClient, None, None]:
    # Override the app's real database dependency with test DB dependency
    app.dependency_overrides[get_db] = override_get_db

    # Create test client
    with TestClient(app) as test_client:
        yield test_client

    # Clear dependency overrides after test finishes
    app.dependency_overrides.clear()