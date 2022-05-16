from simple_term_menu import TerminalMenu
import os 
import runpy
os.system("clear")

second_menu = ["[a] min2sec", "[b] mathfun", "[c]  main menu", "[q] quit"]

loop2 = True

while loop2:
    choice2 = second_menu[TerminalMenu(second_menu, title="frank's menu (2)").show()]

    if choice2 == "[a] min2sec":
        runpy.run_path("min2sec.py")
    
    elif choice2 == "[b] mathfun":
        runpy.run_path("")

    elif choice2 == "[c] main menu":
        runpy.run_path("mainmenu.py")
    
    elif choice2 == "[q] quit":
        loop2 = False 