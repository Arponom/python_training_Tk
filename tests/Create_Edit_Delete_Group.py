
from Help_Class_Group import add_new_group
import time



def test_create(app):
    app.auth.login_gr(login_sys="admin", pass_sys="secret")
    app.group.open_page_gr()
    app.group.create(add_new_group(n_name="date1", h_header="date2", f_footer="date3"))
    app.auth.logout_gr()
    time.sleep(1)

def test_edit(app):
    app.auth.login_gr(login_sys="admin", pass_sys="secret")
    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(name_e="sdf", header_e="aaa", footer_e="asd")
    app.auth.logout_gr()
    time.sleep(1)

def test_delete(app):
    app.auth.login_gr(login_sys="admin", pass_sys="secret")
    app.group.open_page_gr()
    app.group.delete_gr()
    app.auth.logout_gr()



