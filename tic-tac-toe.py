import random

name = input("Enter your name: ").strip().capitalize()
print(f"Welcome to Tic-Tac-Toe, {name}!")

player_score = 0
ai_score = 0
draws = 0

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def reset_board():
    global board
    board = [" " for _ in range(9)]

def player_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid input! Enter a number from 0 to 8.")

def ai_move():
    print("AI is thinking...")

    def minimax(is_maximizing):
        if check_winner("O"):
            return 1
        elif check_winner("X"):
            return -1
        elif is_draw():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = minimax(True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

def is_draw():
    return " " not in board

def main():
    global player_score, ai_score, draws

    while True:
        reset_board()
        print_board()
        user_turn = True

        while True:
            if user_turn:
                player_move()
                print_board()
                if check_winner("X"):
                    print(f"{name}, you win! 🎉")
                    player_score += 1
                    break
            else:
                ai_move()
                print_board()
                if check_winner("O"):
                    print("AI wins! 🤖")
                    ai_score += 1
                    break

            if is_draw():
                print(f"It's a draw, {name}. 🤝")
                draws += 1
                break

            user_turn = not user_turn

        print("\n📊 Scoreboard:")
        print(f"{name}: {player_score}")
        print(f"AI: {ai_score}")
        print(f"Draws: {draws}")

        again = input("\nDo you want to play again?:").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
