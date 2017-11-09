from fixtura.orm import ORMFixture
from random import choice

from model.Help_Class_Address import create_new_address

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_delete_address_from_group(app):
    app.adress.open_address_page()

    old_groups = db.get_group_list()
    #old_address = db.get_contact_list()
    group_id = choice(old_groups).id
    #address_id = choice(old_address).id
    old_address_in_group = db.get_contacts_in_group(create_new_address(id='%s' % group_id))

    app.group.select_group_dropdown(group_id)

    if len(db.get_contacts_in_group(create_new_address(id='%s' % group_id))) == 0:

        app.adress.click_dropdown()
        choise_address = app.adress.get_address_list()
        delete = choice(choise_address).id
        app.adress.click_checkbox(delete)
        app.group.click_on_value(group_id)
        list_of_address_in_choise_group = app.adress.get_address_list()
        choice_id_to_delete = choice(list_of_address_in_choise_group).id

        app.adress.select_address_checkbox(choice_id_to_delete)

        new_address_in_group = db.get_contacts_in_group(create_new_address(id='%s' % group_id))

        assert len(old_address_in_group) - 1 == len(new_address_in_group)

    else:

        list_of_address_in_choise_group = app.adress.get_address_list()
        choice_id_to_delete = choice(list_of_address_in_choise_group).id


        app.adress.select_address_checkbox(choice_id_to_delete)

        new_address_in_group = db.get_contacts_in_group(create_new_address(id='%s' % group_id))

        assert len(old_address_in_group) - 1 == len(new_address_in_group)

