from Help_Class_Group import add_new_group


def test_delete_group(app):
    app.group.open_page_gr()
    if app.group.count() == 0:
        app.group.create(add_new_group(name="date1", header="date2", footer="date3"))
    app.group.delete_gr()
