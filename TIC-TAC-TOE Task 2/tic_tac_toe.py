# implement an AI agent that plays that classic game of Tic_Tac_Toe against a human player.
# You can use algorithms like minimax with or without Alpha_Beta pruning to make the AI player unbeatable.

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if board[row][col] == " ":
                return row, col
            else:
                print("That cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 3.")

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    player_symbol = input("Choose your symbol (X or O): ").upper()
    if player_symbol not in ["X", "O"]:
        print("Invalid symbol. Defaulting to 'X'.")
        player_symbol = "X"
    ai_symbol = "O" if player_symbol == "X" else "X"
    while True:
        player_row, player_col = player_move(board)
        board[player_row][player_col] = player_symbol
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == player_symbol:
                print("Congratulations! You win!")
            else:
                print("The AI wins! Better luck next time.")
            break
        if len(get_empty_cells(board)) == 0:
            print("It's a draw!")
            break
        print("AI is making a move...")
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = ai_symbol
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == ai_symbol:
                print("The AI wins! Better luck next time.")
            else:
                print("Congratulations! You win!")
            break
        if len(get_empty_cells(board)) == 0:
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()