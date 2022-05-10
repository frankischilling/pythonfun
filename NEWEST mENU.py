from simple_term_menu import TerminalMenu
import os
import runpy
os.system("clear")


main_menu = ["[a] main", "[b] run any script", "[c] realmenu.py", "[q] quit"]

loop = True

while loop:
    choice = main_menu[TerminalMenu(main_menu, title="jame's menu").show()]

    if choice == "[a] main":
        print (choice)

    elif choice == "[b] run any script":
        userchoice = input("What script would you like to run? ")
        runpy.run_path(f"{userchoice}")

    elif choice == "[c] realmenu.py":
        runpy.run_path("realmenu.py")

    elif choice == "[q] quit":
        loop = False