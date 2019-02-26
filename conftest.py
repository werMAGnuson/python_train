import pytest
from fixture.app import Applikation

fixture = None


@pytest.fixture  # (scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Applikation()
    else:
        if not fixture.is_valid():
            fixture = Applikation()
    fixture.session.ensure_login(user_email="sprint52stag1msp@yopmail.com", password="!!TEst123")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
