import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('Set focus')

# Click event handler


def click_me():
    action.configure(text='Hello ' + name.get())


# Creating a Label
ttk.Label(text='Enter a name:').grid(column=0, row=0)

# Adding a text box Entry widget
name = tk.StringVar()
name_enterted = ttk.Entry(win, width=12, textvariable=name)
name_enterted.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)
# action.configure(state='disabled')  # Disable the Button widget

# Place cursor into name Entry
name_enterted.focus()

win.mainloop()
