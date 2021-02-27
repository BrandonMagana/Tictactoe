import os
import random
from time import sleep

def display_board(board):
    os.system("cls")
    print("\n\n\t   |   |   ")
    print("\t "+board[7]+" | "+board[8]+" | "+board[9])
    print("\t   |   |   ")
    print("\t------------")
    print("\t   |   |   ")
    print("\t "+board[4]+" | "+board[5]+" | "+board[6])
    print("\t   |   |   ")
    print("\t------------")
    print("\t   |   |   ")
    print("\t "+board[1]+" | "+board[2]+" | "+board[3])
    print("\t   |   |   ")

def player_names():
    names=[]
    print("\n\tType your name\n")
    for i in range(2):
        names.append(input(f"\tPlayer {i+1}: ").title())
    return names

def player_marker(names):
    choice=""
    while choice not in["X","O"]:
        choice=input(f"\n\t{names[0]} choose your marker(X/O): ").upper()
    if(choice=="X"):
        return("X","O")
    else:
        return("O","X")

def place_marker(board,marker,position):
    board[position]=marker

def check_win(board,marker):
    return ((board[1]==marker and board[2]== marker and board[3]==marker) or (board[4]== marker and board[5]==marker and board[6]==marker) or 
            (board[7]==marker and board[8]==marker and board[9]==marker) or (board[1]==marker and board[4]==marker and board[7]==marker) or
            (board[2]==marker and board[5]==marker and board[8]==marker)or(board[3]==marker and board[6]==marker and board[9]==marker) or 
            (board[1]==marker and board[5]==marker and board[9]==marker)or (board[3]==marker and board[5]==marker and board[7]==marker))

def choose_first(names):
    flip=random.randint(0,1)
    if flip==0:
        return names[0]
    else:
        return names[1] 

def space_check(board,position):
    return board[position]==" "

def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full
    return True

def player_choice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        while True:
            try:
                position=int(input("\nChoose a position (1-9): "))      
            except ValueError:
                print("Not an number! Try again.")
                continue
            else:
                break
        if position in[1,2,3,4,5,6,7,8,9]:
            if not board[position]==" ":
                print("This space is already taken!")
        else:
            print("Invalid space")
    return position

def replay():
    choice=""
    while choice not in["Y", "N"]:
        choice=input("\n\tPlay again? (Y/N): ").upper()
    return choice=="Y"

def show_score(names,score,player):
    score[names[player]]+=1
    if player==0:
        otherplayer=1
    else:
        otherplayer=0
    print(f"\n\tScore:\n\n\t{names[player]} = {score[names[player]]}\n\t{names[otherplayer]} = {score[names[otherplayer]]}")

os.system("cls")
print("\tWelcome to tic tac toe")
names=player_names()
player1_mark,player2_mark=player_marker(names)
score={names[0]:0,names[1]:0}
while True:
    #First, set up the game(board, Whos First,)
    board=[" "]*10
    turn=choose_first(names)
    if turn==names[0]:
        print(f"\n\t{names[0]} will go first")
    else:
        print(f"\n\t{names[1]} will go first")
    sleep(3)
    game_on=True
    #GamePlay
    while game_on:
        if turn==names[0]:
            display_board(board)
            position=player_choice(board)
            place_marker(board,player1_mark,position)
            if check_win(board,player1_mark):
                display_board(board)
                game_on=False
                print(f"\n\t{names[0]} has won!!")
                show_score(names,score,0)
            else:
                if fullboard_check(board):
                    display_board(board)
                    print("\n\tTied Game")
                    game_on=False
                else:
                    turn=names[1]
        else:
            display_board(board)
            position=player_choice(board)
            place_marker(board,player2_mark,position)
            if check_win(board,player2_mark):
                display_board(board)
                game_on=False
                print(f"\n\t{names[1]} has won!!")
                show_score(names,score,1)
            else:
                if fullboard_check(board):
                    display_board(board)
                    print("\n\tTied Game")
                    game_on=False
                else:
                    turn=names[0]
    if not replay(): #Break out of the Loop On replay()
        os.system("cls")
        if score[names[0]]==score[names[1]]:
            print("\n\tIt's a draw")
        elif score[names[0]]>score[names[1]]:
            print(f"\n\t{names[0]} has won!!")
        else:
            print(f"\n\t{names[1]} has won!!")
        sleep(5)
        os.system("cls")
        break 