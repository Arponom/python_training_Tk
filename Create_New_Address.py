from Create_New_Address_Fixtura import address
from Help_Class_Address import create_new_address

import pytest

@pytest.fixture
def app(request):
    fixture = address()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_address(app):

    app.open_page()
    app.login(adm_login='admin', secret='secret')
    app.new_address()
    app.create_new_address(create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                                              title='test5', company='test6', address='test7',
                                              home='test8', mobile='test9', work='test10', fax='test11',
                                              email='test12'))
    app.return_home_page()

    app.destroy()
