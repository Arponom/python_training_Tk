from model.Help_Class_Address import create_new_address
from random import choice
import time
from fixtura.orm import ORMFixture


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_contact_to_group(app):
    app.adress.open_address_page()

    old_groups = db.get_group_list()
    old_address = db.get_contact_list()
    group_id = choice(old_groups).id
    address_id = choice(old_address).id


    old_address_in_group = db.get_contacts_in_group(create_new_address(id='%s' % group_id))

    app.adress.click_checkbox(address_id)
    app.group.click_on_value(group_id)

    new_address_in_group=db.get_contacts_in_group(create_new_address(id='%s' % group_id))

    assert len(old_address_in_group) +1 == len (new_address_in_group)

