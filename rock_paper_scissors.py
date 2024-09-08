import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("500x400")
        self.root.config(bg="lightblue")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 24, "bold"), bg="lightblue")
        self.title_label.pack(pady=20)

        self.score_frame = tk.Frame(self.root, bg="lightblue")
        self.score_frame.pack(pady=10)

        self.user_score_label = tk.Label(self.score_frame, text="Your Score: 0", font=("Helvetica", 14), bg="lightblue")
        self.user_score_label.grid(row=0, column=0, padx=20)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Helvetica", 14), bg="lightblue")
        self.computer_score_label.grid(row=0, column=1, padx=20)

        self.choices_frame = tk.Frame(self.root, bg="lightblue")
        self.choices_frame.pack(pady=20)

        self.rock_button = tk.Button(self.choices_frame, text="Rock", font=("Helvetica", 14), command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.choices_frame, text="Paper", font=("Helvetica", 14), command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.choices_frame, text="Scissors", font=("Helvetica", 14), command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"), bg="lightblue")
        self.result_label.pack(pady=20)

        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Helvetica", 14), command=self.reset_game)
        self.play_again_button.pack(pady=20)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="Your Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
