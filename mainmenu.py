from simple_term_menu import TerminalMenu
import os
import runpy
os.system("clear")


# add items to menu
main_menu = ["[a] main", "[b] run any script", "[c] realmenu.py", "[d] second page", "[e] password gen", "[q] quit"]

#hello
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
        runpy.run_path("second menu.py")
    
    elif choice == "[e] password gen":
        runpy.run_path("password gen.py")
    # IGNORE OLD LOOP
    elif choice == "[q] quit":
        loop = False