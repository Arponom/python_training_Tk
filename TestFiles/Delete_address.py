from Help_Class_Address import create_new_address


def test_delete_address(app):
    #app.adress.open_page()
    #app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.adress.open_page()

    if app.adress.countt()==0:
        app.adress.new_address()
        app.adress.create_new_address(
            create_new_address(firstname='test1', middlename='test2', lastname='test3', nickname='test4',
                               title='test5', company='test6', address='test7',
                               home='test8', mobile='test9', work='test10', fax='test11',
                               email='test12'))
    app.adress.open_page()

    app.adress.check_del()
    #app.auth.logout_gr()
