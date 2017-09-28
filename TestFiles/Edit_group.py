from Help_Class_Group import add_new_group

def test_edit_group(app):
    #app.adress.open_page()

    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(add_new_group(name="sdf"))
    #app.adress.logout_gr()

def test_edit_groupp(app):
    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(add_new_group(name=""))
