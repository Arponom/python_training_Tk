from model.Help_Class_Group import add_new_group
#from data.groups import testdata
#import pytest


#
#@pytest.mark.parametrize("add_new", testdata, ids=[repr(x) for x in testdata])
def test_create_group(app, json_data_groups):
    add_new = json_data_groups
    app.group.open_page_gr()
    old_groups = app.group.get_group_list() #
    app.group.create(add_new)
    app.group.open_page_gr()
    new_groups = app.group.get_group_list() #
    assert len(old_groups) + 1 == len(new_groups) #

    old_groups.append(add_new)

    assert sorted(old_groups, key=add_new_group.id_or_max) == sorted(new_groups,key=add_new_group.id_or_max)