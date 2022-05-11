import os
os.system("clear")
print("Please use int only thx :)")
cat = int(input("How many min you want to convert to secs? "))

def min2sec(cat):
    b = cat * 60
    print(f"{cat} min is {b} seconds") 
min2sec(cat)