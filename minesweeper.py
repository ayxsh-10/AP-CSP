import random

def create_board (rows, cols):
    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        board.append(row)
    return board

def place_mines(board, num_mines):
    rows = len(board)
    cols = len(board[0])
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] == "M":
            continue
        else:
            board[row][col] = "M"
            mines_placed += 1

def calculate_numbers(board):
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "M":
                continue
            else:
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if board[nr][nc] == "M":
                                count += 1
                board[r][c] = count

def print_board(board, revealed, flagged):
    rows = len(board)
    cols = len(board[0])
    
    header = " "
    for c in range(cols):
        header += str(c) + "  "
    print(header)
    
    for r in range(rows):
        row_display = str(r) + "  "
        for c in range(cols):
            if revealed[r][c] == True:
                row_display += str(board[r][c]) + " "
            elif flagged[r][c]:
                row_display += "F "
            else:
                row_display += "- "
        print(row_display)

def reveal_empty_cells(board, revealed, flagged, r, c):
    rows = len(board)
    cols = len(board[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if revealed[r][c] == True:
        return
    if board[r][c] == "M":
        return
    if flagged[r][c] == True:
        return "Flagged"
    revealed[r][c] = True
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            reveal_empty_cells(board, revealed, nr, nc)

def reveal_cell(board, revealed, flagged, r, c):
    rows = len(board)
    cols = len(board[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return "Invalid Move"
    elif revealed[r][c] == True:
        return "Already Revealed"
    elif flagged[r][c] == True:
        return "Flagged"
    revealed[r][c] = True
    if board[r][c] == "M":
        return "Game Over"
    if board[r][c] == 0:
        reveal_empty_cells(board, revealed, flagged, r, c)
    return "OK"

def check_win(board, revealed):
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] != "M" and revealed[r][c] == False:
                return False
    return True

def game_loop():
    board = create_board(6, 6)
    place_mines(board, 5)
    calculate_numbers(board)
    flagged = []
    for r in range(6):
        row = []
        for c in range(6):
            row.append(False)
        flagged.append(row)
    revealed = []
    for r in range(6):
        row = []
        for c in range(6):
            row.append(False)
        revealed.append(row)

    while True:
        print_board(board, revealed, flagged)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        action = input("(r)eveal or (f)lag")
        result = None
        if action == "f":
            flagged[row][col] = not flagged[row][col]
        else:
            result = reveal_cell(board, revealed, flagged, row, col)
        if result == "Game Over":
            print("BOOM! You hit a mine.")
            for r in range(6):
                for c in range(6):
                    revealed[r][c] = True
            print_board(board, revealed, flagged)
            break
        elif result == "Already Revealed":
            print("That cell is already revealed!")
        elif result == "Invalid Move":
            print("That's out of bounds!")
        if check_win(board, revealed):
            print("You win!")
            break

game_loop()
        

