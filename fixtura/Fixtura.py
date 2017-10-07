from selenium.webdriver.firefox.webdriver import WebDriver
#16.09.17
from fixtura.Session import aut_helper
from fixtura.Group_helper import grouphelp
from fixtura.Address_helper import adress_helper
##
class testing:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.auth = aut_helper(self)
        self.group = grouphelp(self)
        self.adress = adress_helper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def go_on_page(self):
        wd = self.wd
        wd.get("http://localhost:8443/addressbook/")

    def destroyer(self):
        wd = self.wd
        wd.quit()
