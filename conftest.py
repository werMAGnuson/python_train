import pytest
from fixture.app import Applikation


@pytest.fixture(scope="session")
def app(request):
    fixture = Applikation()
    request.addfinalizer(fixture.destroy)
    return fixture
