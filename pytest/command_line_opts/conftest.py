import pytest

def pytest_addoption(parser):
    parser.addoption("--apikey", action="store")
    parser.addoption("--token", action="store")

@pytest.fixture
def apikey(request):
    return request.config.getoption("apikey")

@pytest.fixture
def token(request):
    return request.config.getoption("token")