# =========================
# imports
# =========================
import tkinter as tk
# ttk stands for themed tk. It improves GUI's look and feel.
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Addng a Label
ttk.Label(win, text="A Label").grid(column=0, row=0)

# =========================
# Start GUI
# =========================
win.mainloop()
