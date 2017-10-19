
from model.Help_Class_Address import create_new_address


def test_autinsystem(app):
    app.adress.open_page()
    app.adress.page_auth(login_syss="admin", pass_syss="secret")
    #time.sleep(2)

def test_create(app):
    #app.auth.login(login_sys="admin", pass_sys="secret")
    app.adress.new_address()
    app.adress.create_new_address(create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                           title='test5', company='test6', address='test7',
                           home='test8', mobile='test9', work='test10', fax='test11',
                           email='test12'))
    #app.auth.logout()
    #time.sleep(1)

def test_edit(app):
    #app.auth.login(login_sys="admin", pass_sys="secret")
    app.adress.open_page_address()
    app.adress.click()
    app.adress.edit_address(firstname_='111', middlename_='111', lastname_='111', nickname_='111',
                           title_='111', company_='111', address_='111',
                           home_='111', mobile_='111', work_='111', fax_='111',
                           email_='111')
    #app.auth.logout()
    #time.sleep(1)

def test_delete(app):
    #app.auth.login(login_sys="admin", pass_sys="secret")
    app.adress.check_del()
    #app.auth.logout()

def test_logout(app):
    app.auth.logout()
    app.destroyer()




