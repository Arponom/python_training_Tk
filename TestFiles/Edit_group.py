

def test_edit_group(app):
    app.adress.open_page()
    app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(name_e="sdf", header_e="aaa", footer_e="asd")
    app.auth.logout_gr()