from IPython.display import clear_output

def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def player_input():
    
    marker = ''
    
    # Keep asking player 1 to choose X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose X or O: ')
    #  Assign Player 2 the opposite marker    
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def place_marker(board, marker, position):
    board[position] = marker   
    
def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
            
    return int(choice)
    
print('Welcome to Tic TAC TOE')
while True:
    
    # Play the game
    
    # Set everything up (board, who's first, choose markers X,O)
    
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    # Turn function 
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Y or N? ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    # Game on 
    
    while game_on:
        
        if turn == 'Player 1':
            # Show board
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie!')
                    game_on = False
                else: 
                    turn = 'Player 2'
                    
        else:
            # Show board
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie!')
                    game_on = False
                else: 
                    turn = 'Player 1'
            
    
    if not replay():
        break
    

# Break out on replay()
