from glob import glob
from platform import release
from tkinter import *
import tkinter as tk
import time
# work on command log 
windows = Tk()
count = 0
mult = 1
dcp1 = 0
autoclickers = 0


def commandlog():
    loglabel = tk.Label(windows)
    loglabel.place(relx= .7, rely=.9)
    loglabel.configure(text=f"hello this is {}")

def clicked():
        global count
        count = count + 1
        if clicked:
            for i in range(10):
                label2.configure(text=f'{count} click')
                if count >= 2:
                    label2.configure(text=f'{count} clicks')
            time.sleep(0.0000001)

def purchaseDoubleClicksCommand():
    global count
    global mult
    if count < 5:
        print("Not enough clicks!")
    elif count >= 5:
        mult = mult*2
        count = count - 5
        print("Double Clicks Purchased!")

def purchaseAutoClickerCommand():
    global count
    global autoclickers # declare global
    if count < 7:
        #commandlog("Not enough clicks!")
        print("a")
    else:
        count -= 7 # pay for an autoclicker
        ("Auto clicker purchased!")
        autoclickers += 1 # receive an autoclicker

def autoclick():
    global master
    global count
    global autoclickers
    count += autoclickers # get clicks from autoclickers
    windows.after(1000, autoclick) # do this again 1 second later
    if autoclickers:
        label2.configure(text=f"{count} clicks")
autoclick() 

windows.title("off brand cookie clicker v0.0001")
windows.geometry("500x300")

label = tk.Label(windows, text="welcome 2 cookie clicker\n this is going to be trash")
label.place(relx = 0.5,rely = 0.13,anchor = 'center')

label1 = tk.Label(windows)
label1.grid(column=0, row=5)
label2 = tk.Label(windows)
label2.place(relx= 0.45, rely=0.0001)




custom_button = tk.Button(windows, text="Click me", command=clicked)
custom_button.place(relx=.01, rely=0)
custom_button2 = tk.Button(windows, text="Auto Clicker", command=purchaseAutoClickerCommand)
custom_button2.place(relx=.01, rely=.1)
custom_button3 = tk.Button(windows, text="Double Click", command=purchaseDoubleClicksCommand)
custom_button3.place(relx=.01, rely=.2)
windows.mainloop()
