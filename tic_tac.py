# X global state
player = 1


def main():
    # first game board render
    n = 4
    cells = n ** 2 * '_'
    board = create_board(cells, n)
    board_view(board)

    # game loop
    while True:
        user_input = input('Enter the coordinates: ')

        if not is_enter_numbers(user_input):
            print('You should enter numbers!')
            continue
        elif not is_in_grid(user_input, n):
            print('Coordinates should be from 1 to 3!')
            continue
        elif is_not_empty(user_input, board):
            print('This cell is occupied! Choose another one!')
            continue

        board = add_move(user_input, board)

        if is_win(board, n, 'X'):
            board_view(board)
            print('X wins')
            break
        elif is_win(board, n, 'O'):
            board_view(board)
            print('O wins')
            break
        elif is_draw(board):
            board_view(board)
            print('Draw')
            break
        else:
            board_view(board)


def create_board(cells, n):
    return [cells[i * n:(i + 1) * n] for i in range(n)]


def board_view(board):
    view = ''
    n = len(board)
    for row in board:
        view += '|'
        for cell in row:
            view += ' ' + cell
        view += ' |\n'
    print(n * '---')
    print(view.rstrip("\n").replace('_', ' '))
    print(n * '---')


def is_enter_numbers(coordinates):
    def is_number(n): return n in [str(x) for x in range(10)]

    is_len = len(coordinates) == 3
    return is_len and is_number(coordinates[0]) and is_number(coordinates[2])


def is_in_grid(coordinates, n):
    return 1 <= int(coordinates[0]) <= n and 1 <= int(coordinates[2]) <= n


def is_not_empty(coordinates, board):
    x = int(coordinates[0]) - 1
    y = int(coordinates[2]) - 1
    return board[x][y] != '_'


def add_move(coordinates, board):
    global player
    x = int(coordinates[0]) - 1
    y = int(coordinates[2]) - 1
    new_board = []
    for row in enumerate(board):
        new_row = ''
        for cell in enumerate(row[1]):
            if row[0] == x and cell[0] == y:
                if player:
                    new_row += 'X'
                    player = 0
                else:
                    new_row += 'O'
                    player = 1
            else:
                new_row += cell[1]
        new_board.append(new_row)
    return new_board


def is_draw(board):
    return not any([True for row in board if row.count('_')])


def is_win(board, n, play_as):
    board_transpose = [''.join(list(i)) for i in zip(*board)]
    left_diagonal = [n[1][n[0]] for n in enumerate([list(i) for i in board])]
    right_diagonal = [n[1][2 - n[0]] for n in enumerate([list(i) for i in board])]
    diagonals = [''.join(left_diagonal), ''.join(right_diagonal)]
    is_horizontal = True if board.count(n * play_as) else False
    is_vertical = True if board_transpose.count(n * play_as) else False
    is_diagonal = True if diagonals.count(n * play_as) else False
    return any([is_horizontal, is_vertical, is_diagonal])


# main function
main()
