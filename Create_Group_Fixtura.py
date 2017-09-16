from selenium.webdriver.firefox.webdriver import WebDriver
#16.09.17
class testing:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def log_off(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, group):
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def go_on_group(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def auth_on_sys(self, login_sys, pass_sys):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login_sys)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pass_sys)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def go_on_page(self):
        wd = self.wd
        wd.get("http://localhost:8443/addressbook/")

    def teardown1(self):
        self.wd.quit()
