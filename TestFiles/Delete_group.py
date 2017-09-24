

def test_delete_address(app):
    app.adress.open_page()
    app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.adress.check_del()
    app.auth.logout_gr()
