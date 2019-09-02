import random

board = [" "]*10


def insert_letter(letter, pos):
    board[pos] = letter


def is_free(pos):
    return board[pos] == ' '


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('------------')

def is_winner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)


def player():
    run = True
    while run:
        move = input(" please enter the desired position for x (From 1 to 9) \n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print("sorry, this place is occupied")
            else:
                print("please enter a number between 1 and 9")

        except:
            print('please enter a number')


def computer():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for l in possible_moves:
            board_copy = board[:]
            board_copy[l] = letter
            if is_winner(board_copy, letter):
                move = l
                return move

    corners = []
    edges = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners.append(i)
        elif i in [2, 4, 6, 8]:
            edges.append(i)

    if len(corners) > 0:
        move = random.choice(corners)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    if len(edges) > 0:
        move = random.choice(edges)
        return move


def run():
    print_board(board)

    while not (is_board_full(board)):
        if not(is_winner(board, 'O')):
            player()
            print_board(board)
        else:
            print(" sorry, you lost.")
            break

        if not (is_winner(board, 'X')):
            move = computer()
            if move == 0:
                print("TIE!")
            else:
                insert_letter("O", move)
                print("computer played. \n")
                print_board(board)

        else:
            print("you win!!")
            break

    if is_board_full(board) and not (is_winner(board, "X") and not (is_winner(board, 'O'))):
      print("TIE!")


while True:
    x = input("Play again? y/n \n")
    if x.lower() == 'y':
        board = [' ']*10
        print('------------------------------')
        run()
    else:
        break


























































































