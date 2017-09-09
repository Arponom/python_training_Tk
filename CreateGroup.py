# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import  unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_CreateGroup(self):

        login_account = 'admin'
        login_pass = 'secter'

        name_new_group = 'some test'
        header_group = 'headerCap'
        footer_group = 'footerCap'

        wd = self.wd
        self.open_home_page(wd)
        self.login_admin(wd, user_name='admin', user_pass='secter')

        self.create_new_group(wd, group_name=name_new_group, group_header=header_group, group_footer=footer_group)
        self.open_group_page(wd)
        self.logout(wd)

    def logout(self, wd):

        wd.find_element_by_link_text("Logout").click()

    def open_group_page(self, wd):

        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, wd, group_name, group_header, group_footer):

        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()

        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_footer)

        wd.find_element_by_name("submit").click()

    def login_admin(self, wd, user_name, user_pass):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user_pass)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8443/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
