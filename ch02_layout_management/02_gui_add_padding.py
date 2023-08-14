import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()

win.title('LabelFrame column one')

def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number.get())

# Create a Label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)
# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Label for Combobox
ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
# Adding a Combobox
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['value'] = tuple(range(1, 6))
number_chosen.grid(column=1, row=1)
number_chosen.current(4)

# Adding a Button
action = ttk.Button(win, text='Click Me!', command=click_me)
action.grid(column=2, row=1)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
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

def checkCallback(*ignoreArgs):
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

# First we change our Radiobutton global variables into a list
colors = ['Blue', 'Gold', 'Red']

def radCall():
    radSel = radVar.get()
    win.configure(background=colors[radSel])


# Create three Radiobuttons using one variable
radVar = tk.IntVar()
# Next we are selecting a non-existing index value for radVar
radVar.set(99)

# Nw we are creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

# Using a scrolled Text control
scroll_w = 40
scroll_h = 3
scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
# remove the name of LabelFrame to see the effect padx has on the position of labels
# buttons_frame = ttk.LabelFrame(win, text='')
buttons_frame.grid(column=0, row=7, padx=20, pady=40)

# Place labels into the container element
ttk.Label(buttons_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
# make the label longer to see the spacing to the right
# ttk.Label(buttons_frame, text='Label1 -- sooooo much looooooooonger...').grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='Label2').grid(column=0, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text='Label3').grid(column=0, row=2, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# Place cursor into name Entry
name_entered.focus()

win.mainloop()