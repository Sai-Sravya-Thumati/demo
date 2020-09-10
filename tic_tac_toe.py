import os
import time
import random

#Defining the board
board=[" "," "," "," "," "," "," "," "," ", " "]

def print_header():
    print("You can choose between 1 and 9")

#define board function
def print_board():
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" |"+board[3]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" |"+board[6]+"  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" |"+board[9]+"  ")
    print("   |   |   ")

while True:
    os.system("clear")
    print_header()
    print_board()

    choice=input("Please choose an empty space for X. ")
    choice=int(choice)

    #Check to see if the space is empty first
    if board[choice]==" ":
        board[choice]="X"
    else:
        print("Sorry that sace isn't empty")

    #check for X win
    if((board[1]=="X" and board[2]=="X" and board[3]=="X")or
            (board[4]=="X" and board[5]=="X" and board[6]=="X")or
            (board[7]=="X" and board[8]=="X" and board[9]=="X")or
            (board[1]=="X" and board[5]=="X" and board[9]=="X")or
            (board[3]=="X" and board[5]=="X" and board[7]=="X")or
            (board[1]=="X" and board[4]=="X" and board[7]=="X")or
            (board[2]=="X" and board[5]=="X" and board[8]=="X")or
            (board[3]=="X" and board[6]=="X" and board[9]=="X")):
        print("X won !! Congratulations")
        os.system("clear")
        print_header()
        print_board()
        break

    os.system("clear")
    print_header()
    print_board()
    
    choice=input("Please choose an empty space for O. ")
    choice=int(choice)

    #Check to see if the space is empty first
    if board[choice]==" ":
        board[choice]="O"
    else:
        print("Sorry that sace isn't empty")

    #check for X win
        if((board[1]=="O" and board[2]=="O" and board[3]=="O")or
            (board[4]=="O" and board[5]=="O" and board[6]=="O")or
            (board[7]=="O" and board[8]=="O" and board[9]=="O")or
            (board[1]=="O" and board[5]=="O" and board[9]=="O")or
            (board[3]=="O" and board[5]=="O" and board[7]=="O")or
            (board[1]=="O" and board[4]=="O" and board[7]=="O")or
            (board[2]=="O" and board[5]=="O" and board[8]=="O")or
            (board[3]=="O" and board[6]=="O" and board[9]=="O")):
            print("O won !! Congratulations")
            os.system("clear")
            print_header()
            print_board()
            break
        
