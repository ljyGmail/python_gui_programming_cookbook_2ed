import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('textbox widget')

# Modified Button Click Function


def click_me():
    action.configure(text='Hello ' + name.get())


# Creating a Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_enterted = ttk.Entry(win, width=12, textvariable=name)
name_enterted.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(text='Click Me!', command=click_me)
action.grid(column=1, row=1)

win.mainloop()
