# import os
#
# import pytest
# from starlette.testclient import TestClient
#
# from space_app.app import app
#
#
# @pytest.fixture(name="client", scope="session", autouse=True)
# def create_client():
#     os.environ["JWT_SECRET"] = "INSERT_ENV_VAR_VALUE"
#
#     client = TestClient(app)
#     yield client

import pytest
from fastapi.testclient import TestClient

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from space_app.app import app
from space_app.database import get_session
from space_app.models import Base

# Create the new database session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():

    # Create the database

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):

    # Dependency override

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_session] = override_get_db

    yield TestClient(app)




