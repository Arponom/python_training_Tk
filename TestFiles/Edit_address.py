from model.Help_Class_Address import create_new_address
from random import randrange

def test_edit_address(app):
    #app.adress.open_page()
    #app.adress.page_auth(login_syss="admin", pass_syss="secret")

    #app.adress.click()
    app.adress.open_address_page()

    old_address = app.adress.get_address_list()
    index = randrange(len(old_address))
    address = create_new_address(firstname='HHHH', middlename='HHHH', lastname='EEEE', nickname='EEEE')
    address.id = old_address[index].id

    if app.adress.countt()==0:
        app.adress.new_address()
        app.adress.create_new_address(
            create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                               title='test5', company='test6', address='test7',
                               home='test8', mobile='test9', work='test10', fax='test11',
                               email='test12'))
        app.adress.open_address_page()

    app.adress.click_Index(index)
    app.adress.edit_addresss(address)

    app.adress.open_address_page()

    new_address = app.adress.get_address_list()
    assert len(old_address) == len(new_address)

    old_address[index]= address
    assert sorted(old_address, key=create_new_address.id_or_max) == sorted(new_address,key=create_new_address.id_or_max)

    #app.auth.logout_gr()
