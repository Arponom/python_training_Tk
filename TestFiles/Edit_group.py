from model.Help_Class_Group import add_new_group
from random import randrange

def test_edit_group(app, db):
    app.group.open_page_gr()

    old_groups = db.get_group_list()  #
    index = randrange(len(old_groups))
    group = add_new_group(name="sdf")
    group.id = old_groups[index].id

    if app.group.count() == 0:
        app.group.create(add_new_group(name="date1", header="date2", footer="date3"))
        app.group.open_page_gr()

    app.group.click_grIndex(index)

    app.group.edit_gr(group)
    app.group.open_page_gr()

    new_groups = db.get_group_list()  #
    assert len(old_groups) == len(new_groups)  #

    old_groups[index]=group
    assert sorted(old_groups, key=add_new_group.id_or_max) == sorted(new_groups, key=add_new_group.id_or_max)

"""def test_edit_groupp(app):
    app.group.open_page_gr()
    app.group.click_gr()
    app.group.edit_gr(add_new_group(name=""))"""
