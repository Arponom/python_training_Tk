

def test_delete_group(app):
    app.adress.open_page()
    app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.group.open_page_gr()
    app.group.delete_gr()
    app.auth.logout_gr()