import random
import string
from model.Help_Class_Group import add_new_group
##

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [
add_new_group(name=random_string("name",10), 
              header=random_string("header",15), 
              footer=random_string("footer",5))]

