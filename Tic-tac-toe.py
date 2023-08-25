game_over = False
table = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
turn_pl1 = True
turns = 0
winner = 0


def print_table(tbl):
    """Prints the table."""
    print('- - - - - - -')
    for row in range(3):
        print('| ', end='')
        for column in range(3):
            print(tbl[row][column], end=' | ')
        print('\n- - - - - - -')


def game_over_check(tbl):
    """Checks the game is over or not."""
    for row in range(3):
        if tbl[row][0] == tbl[row][1] == tbl[row][2] != ' ':
            return tbl[row][0]
    for column in range(3):
        if tbl[0][column] == tbl[1][column] == tbl[2][column] != ' ':
            return tbl[0][column]
    if tbl[0][0] == tbl[1][1] == tbl[2][2] != ' ' or tbl[0][2] == tbl[1][1] == tbl[2][0] != ' ':
        return tbl[1][1]
    return 0


while not game_over:
    if turn_pl1:
        print('Player1', end=' ')
    else:
        print('Player2', end=' ')
    print('your turn. Please type a field you want to fill: ')
    try:
        x = int(input('X: '))
        y = int(input('Y: '))
    except ValueError:
        print('The coordinates must be integers from 0 to 2. Please try again...')
        continue
    if not (0 <= x <= 2 and 0 <= y <= 2):
        print('The coordinates must be integers from 0 to 2. Please try again...')
        continue
    if table[x][y] != ' ':
        print('The field has already been filled. Please try another one...')
        continue
    if turn_pl1:
        table[x][y] = 'X'
    else:
        table[x][y] = 'O'
    turns += 1
    print_table(table)
    turn_pl1 = not turn_pl1
    winner = game_over_check(table)
    if (not winner and turns == 9) or winner:
        game_over = True


if winner == 'X':
    print('Player1 won!')
elif winner == 'O':
    print('Player2 won!')
else:
    print('Game over. Drow!')
