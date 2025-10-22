import tkinter as tk
import os
from tkinter import messagebox

def go():
    hours = h.get()
    minutes = m.get()
    seconds = s.get()

    try:
        inth = int(hours)
        intm = int(minutes)
        ints = int(seconds)
    except:
        messagebox.showinfo(title="Something Wrong...", message="Yo bro, you must put a number here!")
    else:
        time = int(int(hours)*3600 + int(minutes)*60 + int(seconds))
        print("time in seconds: ", time)
        messege = "Your computer will turn off in " + str(time) + " seconds."
        messagebox.showinfo(title=None, message=messege)
        os.system("shutdown -s -t ", time)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk() 

root.title("Shutdown timer")
root.minsize (200,300)
root.maxsize (200,300)
tk.Label(text="After what time do you want \n your computer to turn off?").pack()
tk.Label(text="Hours: ").pack()
h = tk.Entry()
h.pack()
tk.Label(text="Minutes: ").pack()
m = tk.Entry()
m.pack()
tk.Label(text="Seconds: ").pack()
s = tk.Entry()
s.pack()
tk.Label().pack()



tk.Button(text="Go!", command=go).pack()



center_window(root)

root.mainloop()