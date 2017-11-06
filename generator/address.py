import getopt
import os
import random
import string
import sys

import jsonpickle

from model.Help_Class_Address import create_new_address
##
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of address", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/address.json"

for o, a in opts:
    if 0=="-n":
        n= int(a)
    elif o=="-f":
        f=a


def random_date(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

address_data=[
create_new_address(firstname=random_date('firstname',10), middlename=random_date('firstname',10), lastname=random_date('firstname',10), nickname=random_date('firstname',10),
                           title=random_date('firstname',10), company=random_date('firstname',10), address=random_date('firstname',10),
                           home=random_date('firstname',10), mobile=random_date('firstname',10), work=random_date('firstname',10), fax=random_date('firstname',10),
                           email=random_date('firstname',10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    out.write(jsonpickle.encode(address_data))
