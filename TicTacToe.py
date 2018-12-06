def display_board(testboard):
    print(f'{testboard[0]:^3} | {testboard[1]:^3} | {testboard[2]:^3}')
    print('{:-^16}'.format('-'))
    print(f'{testboard[3]:^3} | {testboard[4]:^3} | {testboard[5]:^3}')
    print('{:-^16}'.format('-'))
    print(f'{testboard[6]:^3} | {testboard[7]:^3} | {testboard[8]:^3}')
    print('{:-^16}'.format('-'))

test = [' ', ' ',' ',' ', ' ',' ',' ', ' ',' ']
def clear_board():
    test = [' ', ' ',' ',' ', ' ',' ',' ', ' ',' ']

def player_input():
    choice = -1
    while choice> 9 or choice < 0:
        choice = int(input('Place your marker on the board. Enter 0 to quit'))
        if choice> 9 or choice < 0:
            print('Input not within range. 1-9 only')
    return choice

def place_marker(board, marker, position):
    if board[position]!= ' ':
        print("Position is already filled. Pick an empty spot")
        return False
    else:
        board[position] = marker
        return True

from IPython.display import clear_output
def tic_tac_toe():
    test = [' ', ' ',' ',' ', ' ',' ',' ', ' ',' ']
    ans = input('What marker do you want to start with?')
    counter = 0
    spot = -1
    success = False
    while counter < 9 and spot != 0 and not success:
        spot = player_input()
        if spot == 0:
            print('Quitting')
            break
        marked = False
        while not marked:
            if ans.upper() == 'X':
                marked = place_marker(test,ans,(spot-1))
                if marked:
                    ans = 'O'
            else:
                marked = place_marker(test,ans,(spot-1))
                if marked:
                    ans = 'X'
            if not marked:
                spot = player_input()
        success = win_check(test, ans.upper())
        if success:
            print('Winner!')
        clear_output()
        display_board(test)
        counter += 1
        if counter == 9:
            print("No Winner!")

def win_check(board, mark):
    if board[0:3] == ['X','X','X'] or board[0:3] == ['O','O', 'O']:
        return True
    elif board[3:6] == ['X','X','X'] or board[3:6] == ['O','O', 'O']:
        return True
    elif board[6:9] == ['X','X','X'] or board[6:9] == ['O','O', 'O']:
        return True
    elif board[0:9:4] == ['X','X','X'] or  board[0:9:4] == ['O','O', 'O']:
        return True
    elif board[2:7:2] == ['X','X','X'] or board[2:7:2] == ['O','O', 'O']:
        return True
    elif board[0:7:3] == ['X','X','X'] or board[1:8:3] == ['X','X','X'] or board[2:9:3] == ['X','X','X']:
        return True
    elif board[0:7:3] == ['O','O', 'O'] or board[1:8:3] == ['O','O', 'O'] or board[2:9:3] == ['O','O', 'O']:
        return True
    else:
        return False

Ans = input("Do you want to play a game? Yes or No")
Ans = Ans.upper()
while Ans[0] == 'Y':
    tic_tac_toe()
    Ans  = input("Do you want to play again? Yes or No")
    Ans = Ans.upper()
if Ans[0] != 'Y':
    print('Goodbye')