import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('Radiobutton widget')


def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number.get())


# Create a Label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Lable for Combobox
ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
# Adding a Combobox
number = tk.StringVar()
number_chosen = ttk.Combobox(
    win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 6))
number_chosen.grid(column=1, row=1)
number_chosen.current(1)

# Adding a Button
action = ttk.Button(win, text='Click Me!', command=click_me)
action.grid(column=2, row=1)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled',
                        variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get():
        check3.configure(state='disabled')
    else:
        check3.configure(state='normal')
    if chVarEn.get():
        check2.configure(state='disabled')
    else:
        check2.configure(state='normal')


# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2: checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2: checkCallback())

# Radiobutton Globals
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'

# Radiobutton Callback


def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)


# Create three Radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar,
                      value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar,
                      value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar,
                      value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# Place cursor into name Entry
name_entered.focus()

win.mainloop()
