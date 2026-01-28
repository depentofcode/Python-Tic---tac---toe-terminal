import os

# ANSI colors for terminal
class Colors:
    X = '\033[91m'  # Red
    O = '\033[94m'  # Blue
    END = '\033[0m' # Reset

# Initialize board with numbers
board = [str(i+1) for i in range(9)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear_screen()
    def color_cell(c):
        if c == 'X':
            return f"{Colors.X}{c}{Colors.END}"
        elif c == 'O':
            return f"{Colors.O}{c}{Colors.END}"
        else:
            return c
    print()
    print(f"{color_cell(board[0])} | {color_cell(board[1])} | {color_cell(board[2])}")
    print("--|---|--")
    print(f"{color_cell(board[3])} | {color_cell(board[4])} | {color_cell(board[5])}")
    print("--|---|--")
    print(f"{color_cell(board[6])} | {color_cell(board[7])} | {color_cell(board[8])}")
    print()

def check_win(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

def is_draw():
    return all(cell in ['X','O'] for cell in board)

# Start game
player = 'X'
print_board()

while True:
    try:
        move = int(input(f"Player {player}, choose position (1-9): ")) - 1
        if move not in range(9) or board[move] in ['X','O']:
            continue

        board[move] = player
        print_board()

        if check_win(player):
            print(f"🎉 Player {player} wins!")
            break

        if is_draw():
            print("🤝 It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

    except ValueError:
        continue
