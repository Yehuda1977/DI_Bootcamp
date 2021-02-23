player = 'x'


board = [
    #Row #1
    [
        {
        'x_or_o': ' ',
        'filled': False
        },
        {
        'x_or_o': ' ',
        'filled': False
        },
        {
        'x_or_o': ' ',
        'filled': False
        }
    ],
    #Row #2
    [
        {
        'x_or_o': ' ',
        'filled': False
        },
        {
        'x_or_o': ' ',
        'filled': False
        },
        {
        'x_or_o': ' ',
        'filled': False
        }
    ],
    #Row #3
    [
        {
        'x_or_o': ' ',
        'filled': False
        },
        {
        'x_or_o': ' ',
        'filled': False
        },
        {
        'x_or_o': ' ',
        'filled': False
        }
    ]
]

score = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def display_board():
    for row in board:
        print('')
        print('===============')
        for col in row:
            print('| ' + col['x_or_o'] + ' |', end = '')
        print('')


def player_input(player):
    
    display_board()
    print(f"Player {player}'s turn:")
    
    
    row = input('Which row: ')
    col = input('Which column: ')
    try:
        if board[int(row)-1][int(col)-1]['filled'] == False:
            board[int(row)-1][int(col)-1]['x_or_o'] = player
            board[int(row)-1][int(col)-1]['filled'] = True
            check_win()
        else:
            player_input(player)
    except:
        print('Invalid entry')
        player_input(player)
    
    
    

    if not check_win():
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
        player_input()
   
    
    

def check_win():
    board_array = []
    row_array = []
    for row in board:
        for col in row:
            board_array.append(col['x_or_o'])
    
    row_array = board_array.split(range(9), 3)
    print(row_array)

    # return False
        


    # if totals == 3 or totals == -3:
    #     return True
    
    
    



player_input(player)

