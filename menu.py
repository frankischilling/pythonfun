# menu v2 by da god James H Neathawk

import functools
import os
from pyclbr import Function
from consolemenu import *
from consolemenu.items import *


def clear():
    os.system("clear")

menu = ConsoleMenu("frank's menu", "really programmed by james")

function_item2 = FunctionItem(clear(), ["Enter some input"])

def happyfun():
    print("hello")
    menu.append_item(function_item2)


happyfun()

menu.show()