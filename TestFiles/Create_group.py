from model.Help_Class_Group import add_new_group
import time

def test_create_group(app):

    app.group.open_page_gr()
    old_groups = app.group.get_group_list() #
    group = add_new_group(name="date1", header="date2", footer="date3")
    app.group.create(group)
    app.group.open_page_gr()
    new_groups = app.group.get_group_list() #
    assert len(old_groups) + 1 == len(new_groups) #

    old_groups.append(group)

    assert sorted(old_groups,key=add_new_group.id_or_max) == sorted(new_groups,key=add_new_group.id_or_max)