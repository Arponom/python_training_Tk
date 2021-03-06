from sys import maxsize
#

class Contact:
    def __init__(self, firstname=None,homephone=None, lastname=None,
                 mobilephone=None, workphone=None, secondaryphone=None,
                 id=None, address=None, all_phones_from_home_page=None,
                 all_email_from_haome_page=None,email=None,email2=None,email3=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.address=address
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_email_from_haome_page =all_email_from_haome_page
        self.email = email
        self.email2=email2
        self.email3=email3

    def __repr__(self):
        return "%s: %s: %s: %s: %s: %s:" % (self.id, self.firstname, self.lastname,self.homephone,self.mobilephone,self.workphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and self.firstname ==other.firstname and self.lastname==other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


