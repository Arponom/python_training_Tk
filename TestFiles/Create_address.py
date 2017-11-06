#

import pytest

from model.Help_Class_Address import create_new_address
import time

#@pytest.mark.parametrize("add_address", address_data , ids=[repr(x) for x in address_data ])
def test_create_address(app, db, json_address):
    add_address=json_address
    #app.adress.open_page()
    #app.adress.page_auth(login_syss="admin", pass_syss="secret")
    #old_address = app.adress.get_address_list()
    old_address = db.get_contact()
    """address = create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                           title='test5', company='test6', address='test7',
                           home='test8', mobile='test9', work='test10', fax='test11',
                           email='test12')"""

    app.adress.new_address()
    app.adress.create_new_address(add_address)
    app.adress.open_page()
    time.sleep(1)
    new_address = db.get_contact()
    assert len(old_address)+1 == len(new_address)

    old_address.append(add_address)
    assert sorted(old_address, key=create_new_address.id_or_max) == sorted(new_address, key=create_new_address.id_or_max)
#

