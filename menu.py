# menu v2 by da god James H Neathawk

import functools
from pyclbr import Function
from consolemenu import *
from consolemenu.items import *


menu = ConsoleMenu("frank's menu", "really programmed by james")

def happyfun():
    print("hello")


happyfun()

menu.show()