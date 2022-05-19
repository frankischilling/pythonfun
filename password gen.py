# idk what to do i am just going to think
# password gen programmed by francis may 19th 9:32 AN

import string
import random
import os 
import pyperclip

os.system("clear")
print("Welcomre to frank's password gen")
a = int(input("How many char do you want the password to be? ")) # char
b = input("Do you want letters? ") # letters 
c = input("Do you want numbers? ") # numbers 
d = input("Do you want punctuation? ") # punc 

letters1 = string.ascii_letters
letters2 = string.digits
letters3 = string.punctuation

if b and c and d == "Yes" or "yes" or "y":
    password = (''.join(random.choice(letters1 + letters2 + letters3) for i in range(a)))
    print(f"Your password is {password}")
    print("Your new password has been copied to your clipboard")
    pyperclip.copy(password)
