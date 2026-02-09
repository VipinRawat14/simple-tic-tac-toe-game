import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [""] * 9

score = {
    "X": 0,
    "O": 0,
    "Draw": 0
}

# ---------- FUNCTIONS ----------

def update_score_label():
    score_label.config(
        text=f"X: {score['X']}   O: {score['O']}   Draws: {score['Draw']}"
    )

def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return True
    return False

def is_draw():
    return "" not in board

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", fg="black")

def ask_play_again():
    answer = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if answer:
        reset_board()
    else:
        root.quit()

def on_click(i):
    global current_player

    if board[i] != "":
        return

    board[i] = current_player

    if current_player == "X":
        buttons[i].config(text="X", fg="red")
    else:
        buttons[i].config(text="O", fg="blue")

    if check_winner():
        score[current_player] += 1
        update_score_label()
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        ask_play_again()
        return

    if is_draw():
        score["Draw"] += 1
        update_score_label()
        messagebox.showinfo("Game Over", "It's a draw!")
        ask_play_again()
        return

    current_player = "O" if current_player == "X" else "X"

# ---------- UI ----------

score_label = tk.Label(
    root,
    text="X: 0   O: 0   Draws: 0",
    font=("Arial", 14)
)
score_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 28),
        width=5,
        height=2,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(btn)

root.mainloop()
