from random import randrange
board = [
        [1,2,3],
        [4,'X',6],
        [7,8,9]
        ]

def display_board(board):
    for rw in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for col in range(len(board)):
            pos = board[rw][col]
            print("|  ",pos,"  ", end="")               #Inserting the board values in the middle of every square
        else: print("|")
        print("|       |       |       |")
    else:       
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9: 
                print("Move is out of range try again") #Validate input
                continue
        except ValueError:
            print("Invalid Value, try again")
            continue
        spaces = make_list_of_free_fields(board)        #Find a match with all available fields 
        for rw in range(len(board)):
            for col in range(len(board)):
                if move == board[rw][col]:
                    pos = (rw,col,)
                    if pos in spaces:
                        board[rw][col] = 'O'
                        display_board(board)
                        return
        else: print("Space is already occupied, try again")
    
    
def make_list_of_free_fields(board):
    spaces = []
    for rw in range(len(board)):
        for col in range(len(board)):
            if board[rw][col] != 'X' and board[rw][col] != 'O':
                spaces.append((rw,col))
    return spaces


def victory_for(board, sign):
    final_board = []
    for row in range(len(board)):
        for col in range(len(board)):
            final_board.append(board[row][col])
            
    solutions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(1,5,9)]
    for sol in solutions:
        counter = 0
        for index in sol:
            if final_board[index-1] == sign:
                counter += 1
        if counter == 3:
            return True
    else:
        return False
            
    
def draw_move(board):    
    spaces = make_list_of_free_fields(board)
    while len(spaces) > 0:
        move = randrange(1,10)
        for rw in range(len(board)):
            for col in range(len(board)):
                if board[rw][col] == move:
                    board[rw][col] = 'X'
                    display_board(board)
                    return
    else: return                                         #Allow a return escape if the board finished on the player's turn

                                                         #Start the game
display_board(board)  
while True:
    spaces = make_list_of_free_fields(board)
    if len(spaces) > 0:
        enter_move(board)
        if victory_for(board, 'O') == True:
            print("You won!")
            break
        draw_move(board)
        if victory_for(board, 'X') == True:
            print("You Lost")
            break
    else:
        print("No more moves left, its a tie!")
        break
