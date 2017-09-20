import pytest

from fixtura.Create_Group_Fixtura import testing

@pytest.fixture(scope="session")
def app(request):
    fixture = testing()
    request.addfinalizer(fixture.destroyer)
    return fixture