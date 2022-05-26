# cookie clicker thing maybe 
import tkinter as tk
from tkinter import ttk


count = 0

def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1
    upgradecount = count + 15

    label1.configure(text=f'Button was clicked {count} times!!!')

    def upgradeclick():
        if count == 15:
            new_button = ttk.Button(windows, text="upgrade 1", command=upgradecount)
            new_button.grid(column=1, row=1)

windows = tk.Tk()
windows.title("off brand cookie clicker ")

label = tk.Label(windows, text="welcome 2  cook")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button = ttk.Button(windows, text="Click me", command=clicked)
custom_button.grid(column=1, row=0)




windows.mainloop()