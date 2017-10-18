from model.Help_Class_Address import create_new_address
import time

def test_create_address(app):
    app.adress.open_page()
    #app.adress.page_auth(login_syss="admin", pass_syss="secret")

    old_address = app.adress.get_address_list()

    address = create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                           title='test5', company='test6', address='test7',
                           home='test8', mobile='test9', work='test10', fax='test11',
                           email='test12')

    app.adress.new_address()
    app.adress.create_new_address(address)
    app.adress.open_page()
    time.sleep(1)
    new_address = app.adress.get_address_list()
    assert len(old_address)+1 == len(new_address)

    old_address.append(address)
    assert sorted(old_address, key=create_new_address.id_or_max) == sorted(new_address, key=create_new_address.id_or_max)

    #app.auth.logout_gr()

