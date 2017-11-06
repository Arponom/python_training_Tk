from model.Help_Class_Group import add_new_group
from random import randrange
import random
def test_delete_group(app,db, check_ui):
    app.group.open_page_gr()

    old_groups = db.get_group_list()  #
    group = random.choice(old_groups)

    index = randrange(len(old_groups))
    if app.group.count() == 0:
        app.group.create(add_new_group(name="date1", header="date2", footer="date3"))

    app.group.delete_gr_byId(group.id)
    app.group.open_page_gr()

    new_groups = db.get_group_list()  #
    assert len(old_groups) - 1 == len(new_groups)  #
    old_groups.remove(group)
    #old_groups[index:index+1]=[]
    assert old_groups == new_groups
    if check_ui:
            assert sorted(new_groups, key=add_new_group.id_or_max) == sorted(app.group.get_group_list(),key=add_new_group.id_or_max())