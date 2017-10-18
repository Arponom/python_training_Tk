from model.Help_Class_Group import add_new_group


def test_delete_group(app):
    app.group.open_page_gr()

    old_groups = app.group.get_group_list()  #

    if app.group.count() == 0:
        app.group.create(add_new_group(name="date1", header="date2", footer="date3"))
    app.group.delete_gr()
    app.group.open_page_gr()

    new_groups = app.group.get_group_list()  #
    assert len(old_groups) - 1 == len(new_groups)  #

    old_groups[0:1]=[]
    assert old_groups == new_groups
