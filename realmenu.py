#menu made by me 

from datetime import date, datetime
import os
import datetime as obj_dt
import runpy
from secrets import choice
date_now = obj_dt.date.today()
os.system("clear")

def showmenu():
    print(f"This menu was created by Frank Hagan for fun")
    print(f"Today's date is {date_now}")
    print("1 >> This will print a cat")
    print("2 >> cat 2 ")
    print("3 >> open strings.py")
    print("4 >> open whatever you like ")


def menu_choice(choice_made):
    if choice_made == "1": 
        print("cat")
    elif choice_made == "2": 
        print("cat 2")
    elif choice_made == "3":
        runpy.run_path(path_name='strings.py')
    elif choice_made == "4":
        inputuser = input("Please type list to list (ls) the files you can run: ")
        if inputuser == "ls":
           os.system("ls")
        userchoice = input("What script would you like to run? ")
        runpy.run_path(f"{userchoice}")
    
showmenu()  
#GROSS STOPPP
choice_made = input("What would you like to do: ")
userflag = True 
if choice_made == "Q":
    userflag = False 
    print("Quit")
elif choice_made != "Q":
    menu_choice(choice_made)