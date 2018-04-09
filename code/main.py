import board
import menace


app = board.Board()
player1 = menace.MENACE()


def loop():
    pos = player1.gen_move(app.output_board)
    while app.update(pos, 'X') == -1:
        pos = player1.gen_move(app.output_board)

    board = [[0 for _ in range(3)] for _ in range(3)]
    for (x, y), s in app.output_board():
        board[y][x] = s if s else '-'

    for row in board:
        for col in row:
            print(col, end=' ')
        print()

    if app.is_win():
        print()
        return

    pos = [int(i) for i in input('> ').split(',')]
    while app.update(pos, 'O') == -1:
        pos = [int(i) for i in input('> ').split(',')]

    print()


while not app.is_win():
    loop()

print('Winner:', app.is_win())
