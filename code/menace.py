import itertools
import random
random.seed()


class MENACE(object):
    def __init__(self):
        self.positions = self.gen_positions()
        self.hist = []

    def gen_positions(self):
        positions = {}
        for i in itertools.product('0XO', repeat=9):
            str = ''
            for e in i:
                str += e

            positions[str] = []

            for i, e in enumerate(str):
                if e == '0':
                    x = i % 3
                    y = i // 3
                    positions[str].append([(x, y), 0])

        return positions

    def gen_move(self, board):
        s = ''
        for _, e in board():
            s += str(e)

        # move = funcs.PickMove(self.positions[str])
        move = random.choice(self.positions[s])[0]
        return move


if __name__ == '__main__':
    app = MENACE()
    for i in list(app.positions.keys())[:5]:
        print(i)
        print(app.positions[i])
