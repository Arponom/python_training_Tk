from Help_Class_Group import add_new_group
import time

def test_edit_group(app):
    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(add_new_group(name="sdf"))
    app.adress.logout_gr()
    time.sleep(1)

def test_edit_groupp(app):
    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(add_new_group(name=""))
