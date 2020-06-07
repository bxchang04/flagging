# tests/conftest.py
# https://github.com/pallets/flask/blob/master/examples/tutorial/tests/conftest.py

import os

import pytest
from flagging_site.config import TestingConfig


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    if 'VAULT_PASSWORD' not in os.environ:
        os.environ['VAULT_PASSWORD'] = input('Enter vault password: ')

    app = create_app(config=TestingConfig)
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def data():
    """Create and configure a new data instance for each test."""
    if 'VAULT_PASSWORD' not in os.environ:
        os.environ['VAULT_PASSWORD'] = input('Enter vault password: ')

    data = create_data(config=TestingConfig)
    yield data


@pytest.fixture
def client(data):
    """A test client for the data."""
    return data.test_client()
