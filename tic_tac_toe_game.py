import random
import time

# creating board.
#setting a global variable
board = [" " for _ in range(9)]
current_player = "x"
winner = None
game_running = True


#printing the game board
def printboard(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('|' + "|".join(row) +'|')

def player_input(board):
    move = int(input("enter a move from 0 - 8:"))
    if move >= 0 and move <= 8 and board[move] == " ":
        print(f"{current_player} makes a move to position {move}")

        board[move] = current_player
    else:
        print("space already taken ******")


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True
    
def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True

def check_diagonals(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True
        

def check_tie(board):
    global game_running
    if " " not in board:
        printboard(board)
        print("it's a tie")
        game_running = False

def check_win():
    global game_running
    if check_diagonals(board) or check_horizontal(board) or check_row(board):
        printboard(board)
        print(f"the winner is {winner}")
        if winner == current_player:
            game_running = False


#switcjing the current player.
def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"


def computer_player(board):
    while current_player == "o":
        position = random.randint(0,8)
        if board[position]== " ":
            time.sleep(0.5)
            print(f"{current_player} makes a move to position {position}")
            board[position] = "o"
            switch_player()
            check_win()



while game_running:
    printboard(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()    
    computer_player(board)
    check_win()