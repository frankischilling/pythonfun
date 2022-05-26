import os 
import pyperclip
import string
import random 


os.system("clear")
input1 = input("Letters")
input2 = input("Numbers")
choice1 = string.ascii_letters
choice2 = string.digits
pass1 = (''.join(random.choice(choice1) for i in range(10)))
pass2 = (''.join(random.choice(choice2) for i in range(10)))

if input1 == "yes":
    pass1 = (''.join(random.choice(choice1) for i in range(10)))
if input2 == "yes":
    pass2 = (''.join(random.choice(chouce2) for i in range(10)))

pass3 = pass1 + pass2 

print(pass3)