# menu not using anything but python
import runpy
import os
from secrets import choice
os.system("clear")


def showmenu():
    print("menu programmed by james (navy seal)")
    print("1 >> go back to main menu")

showmenu()

def menu_choice(choice_made):
    if choice_made == "1":
        runpy.run_path("realmenu.py")



choice_made = input("What would you like to do: ")
userflag = True 
if choice_made == "Q":
    userflag = False 
    print("Quit")
elif choice_made != "Q":
    menu_choice(choice_made)