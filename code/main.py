import board
import menace

menace = menace.MENACE('MENACE0')


def loop():
    pos = menace.gen_move(app.output_board)
    while app.update(pos, 'X') == -1:
        pos = menace.gen_move(app.output_board)

    # board = [[0 for _ in range(3)] for _ in range(3)]
    # for (x, y), s in app.output_board():
    #     board[y][x] = s if s else '-'
    #
    # for row in board:
    #     for col in row:
    #         print(col, end=' ')
    #     print()
    # print()

    if app.is_win():
        print()
        return

    pos = menace.gen_move(app.output_board)
    while app.update(pos, 'O') == -1:
        pos = menace.gen_move(app.output_board)

    # board = [[0 for _ in range(3)] for _ in range(3)]
    # for (x, y), s in app.output_board():
    #     board[y][x] = s if s else '-'
    #
    # for row in board:
    #     for col in row:
    #         print(col, end=' ')
    #     print()

    if app.is_win():
        print()
        return

    # while app.update([int(i) for i in pos], 'O') == -1:
    #     pos = input('> ').split(',')
    #     while len(pos) != 2:
    #         pos = input('> ').split(',')

    print()


for set in range(50):
    for round in range(1000):
        app = board.Board()
        while not app.is_win():
            loop()

        print('Winner:', app.is_win())
        print(set * 1000 + round)
        menace.update(app.is_win())
    menace.save()
print('Done!')
