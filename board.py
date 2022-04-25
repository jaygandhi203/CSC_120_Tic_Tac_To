
#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the print_board function
    so that we can easily print the board everytime by calling this function. '''

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def check_mark(row,col):

    turn = 'X'
    count = 0


    for i in range(10):
        print_board(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

def place_mark(row,col,player_id)
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            print_board(theBoard)
            print("\nGame Over.\n")                                print(" **** " +turn + " won. ****")                
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
             print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            print_board(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +turn + " won. ****")
            break 

def check_win(player_id):
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

def main():
    

