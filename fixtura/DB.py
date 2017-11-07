import mysql.connector
import re
from model.Help_Class_Group import add_new_group
from model.Help_Class_Address import create_new_address
class DbFixture:
#
    def __init__(self, host, name, user,password):
        self.host = host
        self.name= name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name,group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(add_new_group(id=str(id), name=name, header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id,firstname,lastname) = row
                list.append(create_new_address(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_more_contact(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, home, mobile, work, fax  from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id,firstname,lastname,address,email,home, mobile, work, fax ) = row
                list.append(create_new_address(id=str(id), firstname=firstname, lastname=lastname,address=address,email=email,
                                               home=home,mobile=mobile,work=work,fax=fax))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()