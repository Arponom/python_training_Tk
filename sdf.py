# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class new(unittest.TestCase):
    
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_new(self):
        wd = self.wd

        self.go_on_page(wd)

        self.auth_on_sys(wd, login_sys="admin", pass_sys="secret")

        self.go_on_group(wd)

        self.create_new_group(wd, group_name="date1", group_header="date2", group_footer="date3")

        self.go_on_group(wd)

        self.log_off(wd)

    def log_off(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd, group_name, group_header, group_footer):
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

    def go_on_group(self, wd):
        wd.find_element_by_link_text("groups").click()

    def auth_on_sys(self, wd, login_sys, pass_sys):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login_sys)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pass_sys)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def go_on_page(self, wd):
        wd.get("http://localhost:8443/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
