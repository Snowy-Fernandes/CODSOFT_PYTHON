import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="light blue")

        self.expression = ""

        # Display entry
        self.display = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief="solid", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, col):
        button = tk.Button(self.root, text=value, font=('Arial', 18), bg="white", fg="black", width=5, height=2, 
                           command=lambda: self.on_button_click(value))
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif value == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
