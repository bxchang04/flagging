import os

import pytest
import pandas as pd
from flagging_site.data.keys import get_data_store_file_path 
# init.py makes folder module, and folders inside sub modules
from flagging_site import create_app
from flagging_site.config import TestingConfig

# if the app fixture is used, make sure it is the first
@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    if 'VAULT_PASSWORD' not in os.environ:
        os.environ['VAULT_PASSWORD'] = input('Enter vault password: ')

    app = create_app(config=TestingConfig)
    yield app

@pytest.fixture
def hobolink_data(data):
    df = pd.read_pickle(get_data_store_file_path('hobolink.pickle'))
    # do something similar for USGS data
    # final step is find a way to represent this in proper way. How do you yield this dataframe? 
        # 2 different fixtures, hobolink and USGS. Fixtures will input 2 separate data sources.
        # website processes the data after it is fixed
        # alt - test processed dataframe. Is this correct?

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
