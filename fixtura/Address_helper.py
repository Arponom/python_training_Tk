from model.Help_Class_Address import create_new_address
##

class adress_helper:

    def __init__(self, app):
        self.app = app

    def new_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    #------------------ оптимизация переходов между страницами
    def open_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) >0):
            wd.get("http://localhost:8443/addressbook/")

    def page_auth(self, login_syss, pass_syss):
        wd = self.app.wd
        wd.get("http://localhost:8443/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login_syss)

        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pass_syss)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_new_address(self, group):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(group.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(group.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(group.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1900")

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.address_cache = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_page_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def click_Index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//tr[@class='odd']/td[8]/a/img").click()


    def edit_addresss(self, addresss):
        wd = self.app.wd
        self.change_field("firstname", addresss.firstname)
        self.change_field("middlename", addresss.middlename)
        self.change_field("lastname", addresss.lastname)
        self.change_field("nickname", addresss.nickname)
        self.change_field("title", addresss.title)
        self.change_field("company", addresss.company)
        self.change_field("address", addresss.address)
        self.change_field("home", addresss.home)
        self.change_field("mobile", addresss.mobile)
        self.change_field("work", addresss.work)
        self.change_field("fax", addresss.fax)
        self.change_field("email", addresss.email)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

        self.change_field("byear", addresss.byear)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.address_cache = None

    def change_field(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    """def edit_address(self,firstname_,middlename_,lastname_,nickname_,title_,company_,address_,home_,
        mobile_,work_,fax_,email_):
        wd = self.app.wd"""



    def open_address_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8443/addressbook/")

    def check_del(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.address_cache = None

    def check_del_Index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.address_cache = None

    def countt(self):
        wd = self.app.wd
        self.open_address_page()
        return len(wd.find_elements_by_name("selected[]"))

    def logout_lr(self):
        wd = self.app.wd

    def logout_gr(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.address_cache = []
            for element in wd.find_elements_by_name("entry"):
                #text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")

                first_name = element.find_element_by_xpath("./td[2]").text
                last_name = element.find_element_by_xpath("./td[3]").text

                self.address_cache.append(create_new_address(id=id, firstname=first_name,lastname=last_name))
        return list(self.address_cache)

    def get_address_more_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.address_cache = []
            for element in wd.find_elements_by_name("entry"):
                # text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")

                first_name = element.find_element_by_xpath("./td[2]").text
                last_name = element.find_element_by_xpath("./td[3]").text
                address = element.find_element_by_xpath("./td[4]").text
                email = element.find_element_by_xpath("./td[5]").text
                phone = element.find_element_by_xpath("./td[6]").text

                self.address_cache.append(create_new_address(id=id, firstname=first_name,address=address,email=email, lastname=last_name, phone=phone))
        return list(self.address_cache)
# ----------------------------------
###