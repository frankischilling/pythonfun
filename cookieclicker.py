# cookie clicker project
# work on timer and time
# config file + save and load 
# work on logic 
 
import tkinter as tk
import time 

count = 0

def clicked():
    global count

    count = count + 1
    
    label2.configure(text=f'{count} click')
    if count >= 2:
        label2.configure(text=f'{count} clicks')


windows = tk.Tk()
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
custom_button2 = tk.Button(windows, text="Click me 2")
custom_button2.place(relx=.01, rely=.1)
custom_button3 = tk.Button(windows, text="Click me 3")
custom_button3.place(relx=.01, rely=.2)


windows.mainloop()