
# coding: utf-8

# In[ ]:

#Makes the board
player1_board = []
fill_board = 10
while fill_board > 0:
    player1_board.append([0,0,0,0,0,0,0,0,0,0])
    fill_board -= 1
player2_board = []
fill_board = 10
while fill_board > 0:
    player2_board.append([0,0,0,0,0,0,0,0,0,0])
    fill_board -= 1

#function to print field
def print_field(field, perspective):
    if field == 0:
        return "O"
    elif field == 1:
        return "H"
    elif field == 2:
        return "M"
    elif field == 3 and perspective == 0:
        return "S"
    elif field == 3 and perspective == 1:
        return "O"
    
    
#Function to print entire board
def print_board(board, perspective):
    times = 9
    j = 10
    while j > 0:
        print ""
        print times + 1,
        for i in board[times]:
            print(print_field(i,perspective)),
        times -= 1
        j -= 1
    print ""
    print("  " + "1 " + "2 " + "3 " + "4 " + "5 " + "6 " + "G " + "7 " + "8 " + "9 "),
    
def place_ship(board):
    done = "y"
    while done == "y":
        x_cordinate = input("X cordinate ")
        y_cordinate = input("Y cordinate ")
        ship_length = input("ship length ")
        get_direction = raw_input("Direction north = N east = E west = W south = S  ")
        set_ship(x_cordinate,y_cordinate,ship_length,board,get_direction)
        done = raw_input("Type y/n to place more ships ")
    print_board(board,0)
        
def set_ship(x,y,length,board,direction):
    extra = -1
    while length > 0:
        if direction == "N" or direction == "n":
            board[y + extra][x - 1] = 3
        elif direction == "E" or direction == "e":
            board[y - 1][x + extra] = 3
        elif direction == "S" or direction == "s":
            board[y - extra][x - 1] = 3
        elif direction == "W" or direction == "w":
            board[y - 1][x - extra] = 3
        extra += 1
        length -= 1
        
        
def validate_board(board):
    count = 0
    times = 0
    while times <= 9:
        for i in board[times]:
            if i == 3:
                count += 1
        times += 1
    return count == 10


def shoot(board):
    x = input("X cordinate ")
    y = input("Y cordinate ")
    if board[y-1][x-1] == 0:
        board[y-1][x-1] = 2
    elif board[y-1][x-1] == 3:
        board[y-1][x-1] = 1
    else:
        return False
def board_health_state(board):
    count = 0
    times = 0
    while times <= 9:
        for i in board[times]:
            if i == 3:
                count += 1
        times += 1
    return count > 0

while validate_board(player1_board) == False or validate_board(player2_board) == False:
    if validate_board(player1_board) == False:
        print "Set player 1 board"
        place_ship(player1_board)
    elif validate_board(player2_board) == False:
        print "" 
        print "Set player 2 board"
        place_ship(player2_board)
turn = 0
while board_health_state(player1_board) and board_health_state(player2_board):
    if turn == 0:
        print("print board y/n")
        if raw_input() == "y":
            if input("player 1 or 2") == 1:
                print_board(player1_board, 1)
            else:
                print_board(player2_board, 0)
        print "player 2 shoots"
        shoot(player1_board)
        turn = 1
    elif turn == 1:
        print("print board y/n")
        if raw_input() == "y":
            if input("player 1 or 2") == 1:
                print_board(player1_board, 0)
            else:
                print_board(player2_board, 1)
        print "player 1 shoots"
        shoot(player2_board)
        turn = 0
if board_health_state(player1_board):
    print "player 1 won"
else:
    print "player 2 won"


# In[ ]:




# In[ ]:




# In[ ]:



