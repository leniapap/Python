# This is a classic tic tac toe game
# global variables
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


# functions
def print_board():
    # print the board
    print("  +---+---+---+")
    print(str(2) + " |" + board[2][0] + "  | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " |" + board[1][0] + "  | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " |" + board[0][0] + "  | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2")


def check_rows(row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2]) and board[row][0] != " "


def check_col(col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col]) and board[0][col] != " "


def main():
    player = "O"
    for i in range(9):
        print_board()
        # choose the next player
        if player == "X":
            player = "0"
        else:
            player = "X"

        # user input
        print(player + " is next!")

        while True:
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
            if row < 0 or row > 2:
                print("You cannot enter that number.Row number must be between 0 and 2.")
                continue
            elif column < 0 or column > 2:
                print("You cannot enter that number.Column number must be between 0 and 2.")
                continue
            elif board[row][column] != " ":
                print("Please choose an empty box!")
                continue
            else:
                board[row][column] = player
                break

        # time to check for a winner!
        winner = False

        for i in range(3):
            if check_rows(i):
                winner = player
                break
            if check_col(i):
                winner = player
                break
            if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ":
                winner = player
            if (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != " ":
                winner = player

        if winner:
            print_board()
            print(player + " is the winner!")
            break
    else:
        print("Tie!")
        print_board()


# start
main()
