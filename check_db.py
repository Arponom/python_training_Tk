import pymysql.cursors
from fixtura.orm import ORMFixture
from model.Help_Class_Group import add_new_group

#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    """l=db.get_contacts_in_group(add_new_group(id="40"))
    for item in l:
        print(item)
    print(len(l))"""
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    pass#connection.close()