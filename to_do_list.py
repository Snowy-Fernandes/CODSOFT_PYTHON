import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.configure(bg="light blue")

        # Task entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg="light blue")
        self.add_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="light blue")
        self.delete_task_button.pack(pady=5)

        # Task treeview
        self.task_tree = ttk.Treeview(root, columns=("sr", "task", "datetime"), show="headings")
        self.task_tree.heading("sr", text="Sr. No.")
        self.task_tree.heading("task", text="Task")
        self.task_tree.heading("datetime", text="Date & Time")
        self.task_tree.column("sr", width=50, anchor='center')
        self.task_tree.column("task", width=300)
        self.task_tree.column("datetime", width=150)
        self.task_tree.pack(pady=10)

        self.task_count = 0  # Initialize task counter

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_count += 1
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.task_tree.insert("", tk.END, values=(self.task_count, task, current_time))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            self.task_tree.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
