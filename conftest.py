import pytest

from fixtura.Fixtura import testing

@pytest.fixture(scope="session")
def app(request):
    fixture = testing()
    request.addfinalizer(fixture.destroyer)
    return fixture