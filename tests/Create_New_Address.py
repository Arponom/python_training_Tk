
from model.Help_Class_Address import create_new_address

def test_new_address(app):

    app.auth.login(login_sys="admin", pass_sys="secret")
    app.adress.new_address()
    app.adress.create_new_address(create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                                              title='test5', company='test6', address='test7',
                                              home='test8', mobile='test9', work='test10', fax='test11',
                                              email='test12'))
    app.auth.logout()

    app.destroyer()
