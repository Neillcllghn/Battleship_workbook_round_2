from random import randint

HIDDEN_BOARD = [[' ']*7 for x in range(6)]
GUESS_PATTERN = [[' ']*7 for x in range(6)]
let_to_nums={'A': 0,'B': 1, 'C': 2,'D': 3,'E': 4,'F': 5,'G': 6}


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
    print('  A B C D E F G')
    print(' ---------------')
    row_of_numbers = 1
    for row in board:
        print("%d|%s|" % (row_of_numbers, "|".join(row)))
        row_of_numbers += 1


def no_of_ships():
    """
    This is to allow the user to select the number of ships they want.
    """
    ships = input('How many ships do you want to sink? Between 1-6 :\n')
    while not ships.isdigit() or int(ships) < 1 or int(ships) >= 6:
        print(f'You selected invaild {ships} number of ships, please try again')
        ships = input('How many ships do you want to sink? Between 1-6 :\n')
    return int(ships)


def ship_creation(board):

    """
    This creates the ships and places them on the board randomly.
    """
    global ships
    ships = no_of_ships()
    for ship in range(ships):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'

        

def ship_location_choices():
    """
    Allows the user to input a row number a column letter to guess where
    the ships are on the board.
    """
    
    row = input("Please enter a ship row 1-6:\n")
    while not row.isdigit() or int(row) < 1 or int(row) > 6:
        print(f'Youclear selected invaild {row} row, please try again')
        row = input("Please enter a ship row 1-6:\n")
    column = input('Please enter a ship column A-G:\n').upper()
    while column not in 'ABCDEFG':
        print(f'You selected invaild {column} column, please try again')
        column = input('Please enter a ship column A-G:\n').upper()
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
    """
    This is to allow the user to select the number of turns they want.
    """
    turns = input('How many turns do you want? Between 1-10 :\n')
    while not turns.isdigit() or int(turns) < 1 or int(turns) >= 10:
        print(f'You selected invaild {turns} number of turns, please try again')
        turns = input('How many turns do you want? Between 1-10 :\n')
    return int(turns)


def game_logistics():
    """
    The game function - what is needed to win, how many turns you have 
    (based on what was selected by the user), and when the game ends
    """
    ship_creation(HIDDEN_BOARD)
    turns = no_of_turns()
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
        if count_hit_ships(GUESS_PATTERN) == ships:
            print('SUCCESS, YOU ARE THE WINNER')
            print(f'You scored {count_hit_ships(GUESS_PATTERN)}')
            break
        print(f'You have {turns} turn(s) remaining')
        if turns == 0:
            print('Game over! You lose.')
            print(f'You scored {count_hit_ships(GUESS_PATTERN)}')
            break



"""
def reset_game():
    option = input('Would you like to play again(Y/N):\n').upper()
    if option == 'Y':
        turns = no_of_turns()
        print(f'Game resetting.....You have {turns} turns to sink my battleships')
        game_logistics()
    else:
        print('Goodbye')
"""

def new_game ():
    login_data = input_details()
    game = game_logistics()

new_game ()