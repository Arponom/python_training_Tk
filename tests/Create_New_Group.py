# -*- coding: utf-8 -*-


from model.Help_Class_Group import add_new_group



#16.09.17

def test_new(app):
    app.auth.login(login_sys="admin", pass_sys="secret")
    app.group.open_page_address()
    app.group.create(add_new_group(n_name="date1", h_header="date2", f_footer="date3"))
    app.group.open_page_address()
    app.auth.logout()
    app.destroyer()


