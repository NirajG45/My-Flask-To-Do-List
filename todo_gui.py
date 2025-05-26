import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        tasks.pop(selected[0])
    else:
        messagebox.showwarning("Select Task", "Select a task to delete.")

root = tk.Tk()
root.title("To-Do List - Tkinter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack()

root.mainloop()
