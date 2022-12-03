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
    print('  A B C D E F G H I J')
    print(' ---------------------')
    row_of_numbers = 1
    for row in board:
        print("%d|%s|" % (row_of_numbers, "|".join(row)))
        row_of_numbers += 1

def ships_creation(board):
    for ship in range(6):
        ship_row, ship_column = randint(0,8), randint(0,8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,8), randint(0,8)
        board[ship_row][ship_column] = 'X'

        

def ship_location_choices():
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
   
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def game_logistics():
    turns = 2
    while turns > 0:
        print_board(GUESS_PATTERN)
        row, column = ship_location_choices()
        if GUESS_PATTERN[row][column] == '-':
            print('You already guess that')
        elif HIDDEN_BOARD[row][column] == 'X':
            print('Great job!, you sunk my Battleship')
            GUESS_PATTERN[row][column] = 'X'
            turns -= 1
        else:
            print('Sorry you missed!')
            GUESS_PATTERN[row][column] = '-'
            turns -= 1
        if count_hit_ships(GUESS_PATTERN) == 6:
            print('SUCCESS, YOU ARE THE WINNER')
            break
        print(f'You have {turns} turn(s) remaining')
        if turns == 0:
            print('Sorry you lose....Game Over!')
            reset_game()
            break

def reset_game():
    option = input('Would you like to play again(Y/N):\n').upper()
    if option == 'Y':
        turns = 2
        print(f'Game resetting.....You have {turns} turns to sink my battleships')
        game_logistics()
    elif option == 'N':
        print('Goodbye')


def new_game ():
    login_data = input_details()
    ships = ships_creation(GUESS_PATTERN)
    game = game_logistics()

new_game ()