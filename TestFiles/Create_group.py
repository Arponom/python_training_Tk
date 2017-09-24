from Help_Class_Group import add_new_group

def test_create_group(app):
    app.adress.open_page()
    app.adress.page_auth(login_syss="admin", pass_syss="secret")
    app.group.open_page_gr()
    app.group.create(add_new_group(n_name="date1", h_header="date2", f_footer="date3"))
    app.auth.logout_gr()