
from model.Help_Class_Address import create_new_address

def test_check_all_contacts(app, db):
    app.adress.open_page()
    contact_from_web = app.adress.get_address_more_list()

    contact_from_db = db.get_more_contact()
   # return print(contact_from_db)


    assert sorted(contact_from_web, key=create_new_address.id_or_max) == sorted(contact_from_db, key=create_new_address.id_or_max)
