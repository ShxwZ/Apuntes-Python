# own modules
# thirdy party modules
# python modules

import datetime 
# or
from datetime import timedelta, date

print(datetime.date.today())
print(date.today())
print(datetime.timedelta(minutes=70))
print(timedelta(minutes=70))

import fmath
from fmath import add, substract

fmath.add(1,2)
fmath.substract(1,2)
add(1,2)
substract(1,2)

from colorama import Fore, Style, init
init(convert=True)

print(Fore.RED + "Hello World")
print(Fore.BLUE + "Hello World")
print(Fore.CYAN + "Hello World")