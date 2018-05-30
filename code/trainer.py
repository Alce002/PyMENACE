import board
import menace


def train(name, n):
    m = menace.MENACE(name)

    # Both play randomly but moves are saved
    for i in range(n):
        print('\r', end='')
        b = board.Board()
        p = 'X'
        while not b.is_win():
            pos = m.random(b.output_board, True)
            b.update(pos, p)
            p = 'X' if p == 'O' else 'O'
        m.update(b.is_win())
        print('1:' + str(int((i + 1) / n * 100)) + '%', end='')
    print()

    # X plays fully random
    for i in range(n):
        print('\r', end='')
        b = board.Board()
        while not b.is_win():
            b.update(m.random(b.output_board), 'X')
            if not b.is_win():
                pos = m.gen_move(b.output_board)
                b.update(pos, 'O')
        m.update(b.is_win())
        print('2:' + str(int((i + 1) / n * 100)) + '%', end='')
    print()

    # Random first move for X
    for i in range(n):
        print('\r', end='')
        b = board.Board()
        b.update(m.random(b.output_board), 'X')
        p = 'O'
        while not b.is_win():
            pos = m.gen_move(b.output_board)
            b.update(pos, p)
            p = 'X' if p == 'O' else 'O'
        m.update(b.is_win())
        print('3:' + str(int((i + 1) / n * 100)) + '%', end='')
    print()

    # Basic training
    for i in range(n):
        print('\r', end='')
        b = board.Board()
        p = 'X'
        while not b.is_win():
            pos = m.gen_move(b.output_board)
            b.update(pos, p)
            p = 'X' if p == 'O' else 'O'
        m.update(b.is_win())
        print('4:' + str(int((i + 1) / n * 100)) + '%', end='')
    print()

    m.save()


if __name__ == '__main__':
    train('MENACE0', 50000)
