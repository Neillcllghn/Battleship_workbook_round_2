from random import randint

HIDDEN_BOARD = [[' ']*10 for x in range(9)]
GUESS_PATTERN = [[' ']*10 for x in range(9)]
let_to_nums={'A': 0,'B': 1, 'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7, 'I': 8, 'J': 9}


def input_details():
    """
    This function allows the user/player to enter a username.
    """
  
    while True:
        print('Please enter your username.')
        print('username must not contain numbers or/and special characters')
        print('Must be no longer than 6 characters')
        print("Example: Neocal etc.....\n")

        username = input("Enter your username here:\n")
        
        if validate_username(username):
            print(f'Hello {username}, Welcome to Battleship Madness!')
            break

def validate_username(values):
    """
    Validate the username being entered. So that it is exactly:
    1. Is 6 characters long.
    2. Contains no numbers or special characters.
    """
    if len(values) < 3 or len(values) > 6:
        print(f"username must be more than 3 and less than 6 characters long, you provided {len(values)}.")
        return False
    elif any(char.isnumeric() for char in values):
        print(f"the username {values} cannot be used, please don't use numbers.")
        return False
    elif not any(char.isalnum() for char in values):
        print(f"the username {values} cannot be used, please don't use non-alphabetic characters.")
        return False

    return True

def print_board(board):
    """
    This creates the board.
    """
    print('  A B C D E F G H I J')
    print(' ---------------------')
    row_of_numbers = 1
    for row in board:
        print("%d|%s|" % (row_of_numbers, "|".join(row)))
        row_of_numbers += 1

def ship_creation(board):

    """
    This creates the ships and places them on the board randomly.
    """
    for ship in range(1):
        ship_row, ship_column = randint(0,8), randint(0,8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,8), randint(0,8)
        board[ship_row][ship_column] = 'X'

        

def ship_location_choices():
    """
    Allows the user to input a row number a column letter to guess where
    the ships are on the board.
    """
    
    row = input("Please enter a ship row 1-9:\n")
    while not row.isdigit() or int(row) < 1 or int(row) > 9:
        print(f'You selected invaild {row} row, please try again')
        row = input("Please enter a ship row 1-9:\n")
    column = input('Please enter a ship column A-J:\n').upper()
    while column not in 'ABCDEFGHIJ':
        print(f'You selected invaild {column} column, please try again')
        column = input('Please enter a ship column A-J:\n').upper()
    return int(row) - 1, let_to_nums[column]


def count_hit_ships(board):
    """
    This reduces the number of ships if the user guessed correctly.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count



def no_of_turns():
    turns = input('How many turns do you want? Between 1-20 :\n')
    while not turns.isdigit() or int(turns) < 1 or int(turns) >= 20:
        print(f'You selected invaild {turns} number of turns, please try again')
        turns = input('How many turns do you want? Between 1-20 :\n')
    print(f'You have {turns} turns to sink my battleships')
    return int(turns)

def game_logistics():
    """
    The rules of the game:
    How many turns.
    """
    turns = no_of_turns()
    ship_creation(HIDDEN_BOARD)
    while turns > 0:
        print_board(GUESS_PATTERN)
        row, column = ship_location_choices()
        if GUESS_PATTERN[row][column] == '-':
            print('You already guess that. Please try again')
        elif HIDDEN_BOARD[row][column] == 'X':
            print('Great job!, you sunk my Battleship')
            GUESS_PATTERN[row][column] = 'X'
            turns -= 1
        else:
            print('Sorry, you missed!')
            GUESS_PATTERN[row][column] = '-'
            turns -= 1
        if count_hit_ships(GUESS_PATTERN) == 1:
            print('SUCCESS, YOU ARE THE WINNER')
            print(f'You scored {count_hit_ships(GUESS_PATTERN)}')
            break
        print(f'You have {turns} turn(s) remaining')
        if turns == 0:
            print('Game over! You lose.')
            print(f'You scored {count_hit_ships(GUESS_PATTERN)}')
            reset_game()
            break

def reset_game():
    option = input('Would you like to play again(Y/N):\n').upper()
    if option == 'Y':
        turns = no_of_turns()
        print(f'Game resetting.....You have {turns} turns to sink my battleships')
        game_logistics()
    else:
        print('Goodbye')



def new_game ():
    login_data = input_details()
    game = game_logistics()

new_game ()