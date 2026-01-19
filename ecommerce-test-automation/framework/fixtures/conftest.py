import os
import pytest

@pytest.fixture(scope='session')
def api_base():
    return os.getenv('API_BASE', 'http://localhost:8000')

@pytest.fixture(scope='session')
def frontend_base():
    return os.getenv('FRONTEND_BASE', 'http://localhost:3000')
