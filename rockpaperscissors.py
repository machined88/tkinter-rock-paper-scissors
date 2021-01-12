import tkinter as tk
import random


class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.geometry("350x180")
        self.master.resizable(False, False)

        text = "Choose between rock, paper and scissors."
        self.rules = tk.Label(master, text=text).pack()
        self.user_input = tk.Entry(master, relief=tk.GROOVE)
        self.user_input.pack()
        self.confirm = tk.Button(master, text="Confirm", relief=tk.GROOVE, command=self.rock_paper_scissors).pack()

        self.result = tk.Label(master, text="Result here")
        self.result.pack()
        tk.Label(master, text="Computer score:").pack()
        self.computer_score = tk.Label(master, text="0")
        self.computer_score.pack()
        tk.Label(master, text="Your score:").pack()
        self.user_score = tk.Label(master, text="0")
        self.user_score.pack()

    def rock_paper_scissors(self):
        options = ["rock", "paper", "scissors"]

        user_choice = self.user_input.get().strip().lower()
        computer_choice = random.choice(options)

        def win():
            self.result['text'] = f"You win ! Computer choose {computer_choice}."
            user_score = int(self.user_score["text"])
            user_score += 1
            self.user_score["text"] = str(user_score)

        if user_choice not in options:
            self.result['text'] = "Not a valid choice."
        else:
            if user_choice == "rock" and computer_choice == "scissors":
                win()
            elif user_choice == "paper" and computer_choice == "rock":
                win()
            elif user_choice == "scissors" and computer_choice == "paper":
                win()
            elif computer_choice == user_choice:
                self.result['text'] = "It's a tie."
            else:
                self.result['text'] = f"You lost... Computer choose {computer_choice}."
                computer_score = int(self.computer_score["text"])
                computer_score += 1
                self.computer_score['text'] = str(computer_score)


window = tk.Tk()
rps = RockPaperScissors(window)
window.mainloop()
