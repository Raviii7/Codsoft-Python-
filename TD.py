import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.tasks = []
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=20, pady=20)
        
        add_button = tk.Button(master, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=10)

        remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=0, column=2, padx=5, pady=10)

        display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks)
        display_button.grid(row=0, column=3, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Success", f'Task "{task}" added to the To-Do List.')
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        task = self.task_entry.get()
        if task in self.tasks:
            self.tasks.remove(task)
            messagebox.showinfo("Success", f'Task "{task}" removed from the To-Do List.')
        else:
            messagebox.showwarning("Warning", f'Task "{task}" not found in the To-Do List.')
        self.task_entry.delete(0, tk.END)

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "To-Do List is empty.")
        else:
            tasks_str = "\n".join([f'{i + 1}. {task}' for i, task in enumerate(self.tasks)])
            messagebox.showinfo("To-Do List", tasks_str)

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
