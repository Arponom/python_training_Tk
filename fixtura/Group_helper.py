from model.Help_Class_Group import add_new_group
#
class grouphelp:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
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
        self.group_cache = None
    #------------------ оптимизация переходов между страницами
    def open_page_gr(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) >0):
            wd.find_element_by_link_text("groups").click()

    def click_grIndex(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()

    def edit_gr(self,group):
        wd = self.app.wd
        self.changefield("group_name",group.name)
        self.changefield("group_header", group.header)
        self.changefield("group_header", group.footer)
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def changefield(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_gr(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def modiry_group(self, new_group_data):
        wd = self.app.wd

    def count(self):
        wd = self.app.wd
        self.open_page_gr()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:

            wd = self.app.wd
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(add_new_group(name=text, id=id))

        return list(self.group_cache)

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_gr_byIndex(self, index):
        wd = self.app.wd
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.group_cache = None
#