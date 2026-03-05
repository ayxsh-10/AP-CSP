import tkinter as tk
from tkinter import messagebox

# Board state: list of 9 elements (X or O)
board = [''] * 9
current_player = 'X'
game_active = True

wins = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

# Handle button click: place symbol, switch player, check win/draw
def button_click(pos):
    global current_player, game_active
    if board[pos] == '' and game_active:
        board[pos] = current_player
        buttons[pos].config(text=current_player, state='disabled')
        if check_win(current_player):
            messagebox.showinfo("Game Over", current_player + " wins!")
            game_active = False
        elif '' not in board:
            messagebox.showinfo("Game Over", "It's a draw.")
            game_active = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Check if player has winning combination
def check_win(player):
    for combo in wins:
        if all(board[i] == player for i in combo):
            disable_board()
            return True
    return False

# Disable all buttons to end game
def disable_board():
    global game_active
    for button in buttons:
        button.config(state='disabled')
    game_active = False

# Reset board, buttons, player, and game state.
def reset_game():
    global board, current_player, game_active
    board = [''] * 9
    current_player = 'X'
    game_active = True
    for button in buttons:
        button.config(text='', state='normal')

# Hide start screen and show the game screen.
def show_game_screen():
    # remove start screen
    start_frame.pack_forget()
    # show game area
    game_frame.pack(fill="both", expand=True)
    # make sure the game is reset when opened
    reset_game()

# Create main window
main_window = tk.Tk()
main_window.title("Tic-Tac-Toe")
main_window.resizable(False, False)
main_window.geometry("500x550")

# Start Screen
start_frame = tk.Frame(main_window)

title_label = tk.Label(
    start_frame,
    text="Tic-Tac-Toe",
    font=('Comic Sans MS', 32, 'bold')
)
title_label.pack(pady=40)

# start game button
start_button = tk.Button(
    start_frame,
    text="Start Game",
    font=('Comic Sans MS', 16, 'bold'),
    width=12,
    command=show_game_screen
)
start_button.pack(pady=10)

# quit game button
quit_button = tk.Button(
    start_frame,
    text="Quit",
    font=('Comic Sans MS', 16, 'bold'),
    width=12,
    command=main_window.destroy
)
quit_button.pack(pady=10)

start_frame.pack(fill="both", expand=True)

# Game Screen
game_frame = tk.Frame(main_window)

# Title label on game screen
tk.Label(
    game_frame,
    text="Tic-Tac-Toe",
    font=('Comic Sans MS', 28, 'bold')
).pack(pady=10)

# Game board frame
board_frame = tk.Frame(game_frame)
board_frame.pack(pady=10)

# Create the 9 buttons in a 3x3 grid
buttons = []
for i in range(3):
    for j in range(3):
        pos = i*3 + j
        btn = tk.Button(
            board_frame,
            text='',
            font=('Comic Sans MS', 24, 'bold'),
            width=4, height=2,
            command=lambda p=pos: button_click(p)
        )
        btn.grid(row=i, column=j, padx=2, pady=2)
        buttons.append(btn)

# Reset Game button
tk.Button(
    game_frame,
    text="Reset Game",
    font=('Comic Sans MS', 12, 'bold'),
    command=reset_game,
    bg='lightblue'
).pack(pady=10)

# run
main_window.mainloop()

#Reflection:

#The most challenging aspect was maintaining oversight of the game state and ensuring the
#buttons could not be pressed twice while appropriately changing turns since I had to both
#know that it changed users and save that as a final value.

#I discovered how to utilize Tkinter to develop a GUI, which involves making frames,
#buttons, and labels, along with the method to link button clicks to functions that
#revise a game status.

#In the future, I would enhance this project by incorporating a score tracker throughout so
#you could play multiple games through several iterations, and enhanced visual refinement such as
#hues or animations.
