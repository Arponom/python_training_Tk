from selenium.webdriver.firefox.webdriver import WebDriver

from fixtura.address_helper import adress_helper
from fixtura.group_auth import aut_helper
from fixtura.group_helper import grouphelp


class configurate:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

        self.auth = aut_helper(self)
        self.group = grouphelp(self)
        self.adress = adress_helper(self)

    def go_on_page(self):
        wd = self.wd
        wd.get("http://localhost:8443/addressbook/")

    def destroyer(self):
        self.wd.quit()