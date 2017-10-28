from model.contact import Contact
#

class ContactHelper:

    def __init__(self,app):
        self.app = app

    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    address_cache = None

    def open__page(self):
        wd = self.app.wd
        wd.get("http://localhost:8443/addressbook/")

    def get_contact_list(self):
        if self.address_cache is None:
            wd=self.app.wd
            self.open__page()
            self.address_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text.splitlines()
                self.address_cache.append(Contact(firstname=firstname, lastname=lastname,id=id,address=address,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))

            return list(self.address_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open__page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.open__page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        address = wd.find_element_by_name("address").get_attribute("value")

        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname,lastname=lastname,id=id,address=address,
                       homephone=homephone,workphone=workphone,
                       mobilephone=mobilephone,secondaryphone=secondaryphone)



    #--------------------------------------------------------------------------
    def get_contact_list_reverse(self):
        if self.address_cache is None:
            wd=self.app.wd
            self.open__page()
            self.address_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text
                all_email = cells[4].text
                self.address_cache.append(Contact(firstname=firstname, lastname=lastname,id=id,address=address,
                                                  all_phones_from_home_page=all_phones, all_email_from_haome_page=all_email))

            return list(self.address_cache)

    def get_contact_info_from_edit_page_reverse(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        address = wd.find_element_by_name("address").get_attribute("value")

        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname,lastname=lastname,id=id,address=address,
                       homephone=homephone,workphone=workphone,
                       mobilephone=mobilephone,secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)