import pachet

print(pachet.my_var)
from pachet import my_var, my_function
print(my_var)

from pachet.modul1 import my_function
my_function()
# from pachet import *

from .part1 import math.pi