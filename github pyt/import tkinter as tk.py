import tkinter as tk
from tkinter import messagebox

def add_task():
    t = entry.get()
    if t:
        l.insert(tk.END, t)
        e.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    s = l.curselection()
    if s:
        l.delete(s)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
a = tk.Tk()
a.title("To-Do List App")

# Entry widget for new tasks
e = tk.Entry(a, width=40)
e.pack(pady=10)

# Button to add tasks
b = tk.Button(a, text="Add Task", command=add_task)
b.pack(pady=5)

# Listbox to display tasks
l = tk.Listbox(a, selectmode=tk.SINGLE, width=40, height=10)
l.pack(pady=10)

# Button to delete selected task
d = tk.Button(a, text="Delete Task", command=delete_task)
d.pack(pady=5)

# Start the main loop
a.mainloop()