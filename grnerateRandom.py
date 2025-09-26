
import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    """Initialize a new game round."""
    global secret_number, attempts_left
    secret_number = random.randint(1, 100)
    attempts_left = 3
    lbl_status.config(text="Guess a number between 1 and 100")
    lbl_chances.config(text=f"Chances Left: {attempts_left}")
    entry_guess.delete(0, tk.END)

    # Show/Hide widgets for game play
    frame_game.pack(pady=10)
    frame_start.pack_forget()
    frame_end.pack_forget()

def check_guess():
    """Check the user's guess against the secret number."""
    global attempts_left
    try:
        guess = int(entry_guess.get())
        attempts_left -= 1

        if guess < secret_number:
            lbl_status.config(text="Too Low!")
        elif guess > secret_number:
            lbl_status.config(text="Too High!")
        else:
            messagebox.showinfo("🎯 Correct!", "You guessed the number!")
            end_game()
            return

        lbl_chances.config(text=f"Chances Left: {attempts_left}")
        entry_guess.delete(0, tk.END)

        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"Out of chances! The number was {secret_number}.")
            end_game()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def end_game():
    """Show end-game options (Continue or Exit)."""
    frame_game.pack_forget()
    frame_end.pack(pady=10)

def exit_game():
    root.destroy()

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.state("zoomed")
#root.resizable(False, False)

# Start screen
frame_start = tk.Frame(root)
tk.Label(frame_start, text="Number Guessing Game", font=("Arial", 40, "bold")).pack(pady=20)
tk.Button(frame_start, text="Start Game", font=("Arial", 40, "bold"),
          bg="#4CAF50", fg="white", width=15, command=start_game).pack()
frame_start.pack(pady=60)

# Game play screen
frame_game = tk.Frame(root)
lbl_status = tk.Label(frame_game, text="", font=("Arial", 40))
lbl_status.pack(pady=10)

lbl_chances = tk.Label(frame_game, text="", font=("Arial", 40))
lbl_chances.pack()

entry_guess = tk.Entry(frame_game, font=("Arial", 40), justify="center")
entry_guess.pack(pady=10)

tk.Button(frame_game, text="Check Guess", font=("Arial", 40, "bold"),
          bg="#2196F3", fg="white", command=check_guess).pack()

# End screen
frame_end = tk.Frame(root)
tk.Label(frame_end, text="Game Over!", font=("Arial", 40, "bold")).pack(pady=10)
tk.Button(frame_end, text="Continue", font=("Arial", 40, "bold"),
          bg="#4CAF50", fg="white", width=12, command=start_game).pack(pady=5)
tk.Button(frame_end, text="Exit", font=("Arial", 40, "bold"),
          bg="#f44336", fg="white", width=12, command=exit_game).pack(pady=5)

root.mainloop()

