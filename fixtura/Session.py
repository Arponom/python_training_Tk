
class aut_helper:

    def __init__(self, app):
        self.app = app

    def login_q(self, login_sys, pass_sys):
        wd = self.app.wd
        self.app.go_on_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login_sys)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pass_sys)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout_q(self):
        wd=self.app.wd
        wd.find_element_by_link_text("Logout").click()
#------------------------------------------------------
    def ensure_logout(self):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            self.logout_q()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, login_syss):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + login_syss + ")"

    def ensure_login(self, login_syss, pass_syss):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(login_syss):
                return
            else:
                self.logout_q()
        self.login_q(login_syss, pass_syss)
