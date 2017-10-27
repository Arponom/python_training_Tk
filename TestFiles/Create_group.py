from model.Help_Class_Group import add_new_group
import time
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [
add_new_group(name=random_string("name",10), header=random_string("header",15), footer=random_string("footer",5))]

@pytest.mark.parametrize("add_new", testdata, ids=[repr(x) for x in testdata])
def test_create_group(app, add_new):

    app.group.open_page_gr()
    old_groups = app.group.get_group_list() #
    app.group.create(add_new)
    app.group.open_page_gr()
    new_groups = app.group.get_group_list() #
    assert len(old_groups) + 1 == len(new_groups) #

    old_groups.append(add_new)

    assert sorted(old_groups, key=add_new_group.id_or_max) == sorted(new_groups,key=add_new_group.id_or_max)