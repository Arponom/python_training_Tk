import pytest

from fixtura.Fixtura import testing

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = testing(browser=browser)
    else:
        if not fixture.is_valid():
            fixture = testing(browser=browser)
    fixture.auth.ensure_login(login_syss="admin", pass_syss="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.auth.ensure_logout()
        fixture.destroyer()
    request.addfinalizer(fin)
    return fixture

def python_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
