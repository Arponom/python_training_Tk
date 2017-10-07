import pytest

from fixtura.Fixtura import testing

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = testing()

    else:
        if not fixture.is_valid():
            fixture = testing()
    fixture.auth.ensure_login(login_syss="admin", pass_syss="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.auth.ensure_logout()
        fixture.destroyer()
    request.addfinalizer(fin)
    return fixture