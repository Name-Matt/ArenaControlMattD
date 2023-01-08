import tkinter as tk
from tkinter import ttk

def say_hi():
    print("Hi there!")

root = tk.Tk()

button = ttk.Button(root, text="Click me", command=say_hi)
button.pack()

root.mainloop()
