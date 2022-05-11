from os import terminal_size
from secrets import choice
from ssl import Options
from simple_term_menu import TerminalMenu
import os
os.system("clear")

def main():
    options = ["main", "run any script", "quit"]
    terminal_menu = TerminalMenu(options, title="frank's new menu")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    
    if menu_entry_index == "main":
        print("main")
    elif menu_entry_index == "run any script":
        print("any script")


if __name__ == "__main__":
    main()

#loop = True

#while loop:

 #   if choice == "main":
  #      print (choice)

   # elif choice == "run any script":
    #    print("meow")

    #elif choice == "quit":
     #   loop = False