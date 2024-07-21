import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f8ff")

        # Title label
        self.title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#4682b4")
        self.title_label.pack(pady=10)

        # Password length label and entry
        self.length_label = tk.Label(root, text="Enter Password Length:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
        self.length_label.pack(pady=5)

        self.length_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack(pady=5)

        # Complexity level label and combobox
        self.complexity_label = tk.Label(root, text="Select Complexity Level:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
        self.complexity_label.pack(pady=5)

        self.complexity_var = tk.StringVar()
        self.complexity_combobox = ttk.Combobox(root, textvariable=self.complexity_var, font=("Helvetica", 12), state='readonly')
        self.complexity_combobox['values'] = ("Low", "Medium", "High")
        self.complexity_combobox.current(1)
        self.complexity_combobox.pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#4682b4", fg="#ffffff", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Password display label
        self.password_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#4682b4")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError

            complexity = self.complexity_var.get()
            if complexity == "Low":
                characters = string.ascii_lowercase
            elif complexity == "Medium":
                characters = string.ascii_letters + string.digits
            elif complexity == "High":
                characters = string.ascii_letters + string.digits + string.punctuation
            else:
                raise ValueError

            password = ''.join(random.choice(characters) for i in range(length))

            self.password_label.config(text=password)
        except ValueError:
            self.password_label.config(text="Please enter a valid number and select a complexity level.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
