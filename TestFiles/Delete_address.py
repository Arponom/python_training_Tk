from model.Help_Class_Address import create_new_address
import time
from random import randrange

def test_delete_address(app,db):
    #app.adress.open_page()
    #app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.adress.open_page()

    old_address = db.get_contact()
    index = randrange(len(old_address))

    if app.adress.countt()==0:
        app.adress.new_address()
        app.adress.create_new_address(
            create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                               title='test5', company='test6', address='test7',
                               home='test8', mobile='test9', work='test10', fax='test11',
                               email='test12'))
    app.adress.open_page()

    app.adress.check_del_Index(index)
    time.sleep(1)
    app.adress.open_page()
    time.sleep(1)
    new_address = db.get_contact()
    assert len(old_address) - 1 == len(new_address)

    old_address[index:index+1]=[]
    assert old_address == new_address
    #app.auth.logout_gr()
