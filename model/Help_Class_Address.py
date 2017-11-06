from sys import maxsize
####
class create_new_address:
    def __init__(self,firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None,
                           work=None, fax=None, email=None, byear=None, id=None ):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.byear = byear
        self.id = id
        ####

    def __repr__(self):
        return "%s: %s: %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize