import json
import importlib
import pytest
import os.path
from fixtura.Fixtura import testing
import jsonpickle
from fixtura.DB import DbFixture
#
fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),file )
        with open(config_file) as file:
            target = json.load(file)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    """if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)"""
    #base_url = request.config.getoption("--base_url")
    if fixture is None or not fixture.is_valid():
        fixture = testing(browser=browser, base_url=web_config['baseUrl'])
    """else:
        if not fixture.is_valid():
            fixture = testing()"""
    fixture.auth.ensure_login(login_syss=web_config['username'], pass_syss=web_config['password'])
    return fixture

@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture=DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    global fixture
    def fin():
        fixture.auth.ensure_logout()
        fixture.destroyer()
    request.addfinalizer(fin)

    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    #parser.addoption("--base_url", action="store", default="http://localhost:8443/addressbook/")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check ui")
