import re

"""def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)
"""
def test_phones_on_home_page_reverse(app):
    contact_from_home_page = app.contact.get_contact_list_reverse()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_reverse(0)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_haome_page == merge_email(contact_from_edit_page)
def clear(s):
    return re.sub("[()-]","", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                                 filter(lambda x: x is not None,
                                                        [contact.homephone,contact.mobilephone ,contact.workphone,contact.secondaryphone]))))

def merge_email(mail):
    return "\n".join([mail.email,mail.email2,mail.email3])