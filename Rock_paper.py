import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f8ff")

        self.user_score = 0
        self.computer_score = 0

        self.choices = ["rock", "paper", "scissors"]
        self.emojis = {
            "rock": "✊",
            "paper": "🖐",
            "scissors": "✌"
        }

        # Title label
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#1c3c84")
        self.title_label.pack(pady=10)

        # User choice buttons
        self.buttons_frame = tk.Frame(root, bg="#f0f8ff")
        self.buttons_frame.pack(pady=20)

        for choice in self.choices:
            button = tk.Button(self.buttons_frame, text=f"{choice.capitalize()} {self.emojis[choice]}", font=("Helvetica", 12, "bold"), bg="#ffffff", fg="#000000", command=lambda ch=choice: self.play_round(ch))
            button.pack(side=tk.LEFT, padx=10)

        # Display user choice, computer choice, and result
        self.user_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f8ff", fg="#1c3c84")
        self.user_choice_label.pack(pady=10)

        self.computer_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f8ff", fg="#1c3c84")
        self.computer_choice_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#1c3c84")
        self.result_label.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"), bg="#f0f8ff", fg="#1c3c84")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(root, text="User: 0  Computer: 0", font=("Helvetica", 14), bg="#f0f8ff", fg="#1c3c84")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 12, "bold"), bg="#1c3c84", fg="#ffffff", command=self.reset_game)
        self.play_again_button.pack(pady=20)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)

        self.user_choice_label.config(text=f"User choice: {user_choice.capitalize()} {self.emojis[user_choice]}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice.capitalize()} {self.emojis[computer_choice]}")

        if user_choice == computer_choice:
            result = "It's a tie!"
            feedback = "😐"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            feedback = "😊"
            self.user_score += 1
        else:
            result = "You lose!"
            feedback = "😢"
            self.computer_score += 1

        self.result_label.config(text=result)
        self.feedback_label.config(text=feedback)
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

    def reset_game(self):
        self.user_choice_label.config(text="")
        self.computer_choice_label.config(text="")
        self.result_label.config(text="")
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
