from IPython.display import clear_output

def display(board):
    clear_output()
    print(board[1]+" | "+board[2], "| "+ board[3])
    print("---------")
    print(board[4]+" | "+board[5]+ " | "+ board[6])
    print("---------")
    print(board[7]+" | "+board[8]+ " | "+ board[9])

def playerInput():
    i=""
    while(i!="x" and i!="o"):
        i=input("PLAYER 1 =>  choose x or o :")
    p1=i
    if(p1=="x"):
        p2="o"
    else:
        p2="x"
    return(p1,p2)

def fullBoard(b):
    temp=0
    for i in b:
        if(i!=" "):
            temp+=1
    if(temp==9):
        return True
    else:
        False

def placePosition(board,marker,position):
    board[position]=marker

def checkWinner(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def replay():    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

import random
def chooseFirst():
    if random.randint(0, 1) == 0:
        return 'player2'
    else:
        return 'player1'

def playerChoice(board):
    inp= int(input('choose your position: (1-9) =>'))
    if(inp in [1,2,3,4,5,6,7,8,9]):
        if(space_check(sampleBoard,inp)==False):
            position=inp
    return position

def space_check(board, position):
    return board[position] == ' '

print("welcome to tik tak toe")
while True:
    sampleBoard =['#','1','2','3','4','5','6','7','8','9']
    player1,player2=playerInput()
    turn=chooseFirst()
    print(turn +"will go first...")
    start= input("Shall we start the game (y or n) :")
    if(start=="y"):
        start=True
    else:
        start=False
    while start:
        if(turn=="player1"):
            display(sampleBoard)
            pos=playerChoice(sampleBoard)
            placePosition(sampleBoard,player1,pos)
            
            if(checkWinner(sampleBoard,player1)):
                display(sampleBoard)
                print("Congratulation!, player1 had won...")
                start = False
            else:
                if(fullBoard(sampleBoard)):
                    display(sampleBoard)
                    print("The Game is Drawn !!")
                    break
                else:
                    turn="player2"
                    
                    
        if(turn=="player2"):
            display(sampleBoard)
            pos=playerChoice(sampleBoard)
            placePosition(sampleBoard,player2,pos)
            if(checkWinner(sampleBoard,player2)):
                display(sampleBoard)
                print("Congratulation!, player2 had won...")
                start=False
            else:
                if(fullBoard(sampleBoard)):
                    display(sampleBoard)
                    print("The Game is Drawn !!")
                    break
                else:
                    turn="player1"
                    
    if not replay():
            break

