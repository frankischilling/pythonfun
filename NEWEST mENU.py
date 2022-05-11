from simple_term_menu import TerminalMenu
import os
import runpy
os.system("clear")


# add items to menu
main_menu = ["[a] main", "[b] run any script", "[c] realmenu.py", "[d] second page", "[q] quit"]
second_menu = ["[a] min2sec", "[b] mathfun", "[c]  math", "[q] quit"]


loop = True
#loop for selecting items
while loop:
    choice = main_menu[TerminalMenu(main_menu, title="jame's menu").show()]

    if choice == "[a] main":
        print(choice)

    elif choice == "[b] run any script":
        userchoice = input("What script would you like to run? ")
        runpy.run_path(f"{userchoice}")

    elif choice == "[c] realmenu.py":
        runpy.run_path("realmenu.py")

    elif choice == "[d] second page":
        choice2 = second_menu[TerminalMenu(second_menu, title="frank's menu").show()]

    if choice2 == "[a] min2sec":
            runpy.run_path("min2sec.py")
        
    elif choice == "[q] quit":
        loop = False