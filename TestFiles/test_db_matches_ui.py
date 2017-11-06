from model.Help_Class_Group import add_new_group

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return add_new_group(id=group.id, name=group.name.strip())
    db1_list = map (clean, db.get_group_list())
    assert sorted(ui_list, key=add_new_group.id_or_max) == sorted(db1_list, key=add_new_group.id_or_max)
