# Andrew Butler             11-2-2022
# module for modules.py modules demo

import math

print("This text will print out, because stuff is called when you import modules")
def val(x, y, z):
    value = math.trunc(x) + math.comb(y, z)
    return value