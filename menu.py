# menu v2 by da god James H Neathawk

from pyclbr import Function
from consolemenu import *
from consolemenu.items import *


menu = ConsoleMenu("frank's menu", "really programmed by james")


submenu = ConsoleMenu("This is the sub menu")
item1 = MenuItem("hi", menu=menu)
sub1 = SubmenuItem("hi2", submenu, menu=menu)

menu.append_item(item1)
#menu.append_item(sub1)

menu.show()