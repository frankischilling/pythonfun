# idk what to do i am just going to think
# password gen programmed by francis may 19th 9:32 AM, updated may 24th 8:24 AM

import string
import random
import os 
import pyperclip
import runpy
from simple_term_menu import TerminalMenu

os.system("clear")
main_menu = ["[a] main", "[b] password gen", "[q] quit"]

loop = True
while loop:
    choice = main_menu[TerminalMenu(main_menu, title="frank's menu - password gen").show()]

    if choice == "[a] main":
        runpy.run_path("mainmenu.py")

    elif choice == "[b] password gen":
        print("Welcomre to frank's password gen")
        a = int(input("How many char do you want the password to be? ")) # char
        b = input("Do you want letters? ") # letters 
        c = input("Do you want numbers? ") # numbers 
        d = input("Do you want punctuation? ") # punc 

        letters1 = string.ascii_letters
        letters2 = string.digits
        letters3 = string.punctuation


        if b and c and d == "yes":
            password = (''.join(random.choice(letters1 + letters2 + letters3) for i in range(a)))
            print(f"Your password is {password}")
            print("Your new password has been copied to your clipboard")
            pyperclip.copy(password)

    elif choice == "[q] quit":
        loop = False
