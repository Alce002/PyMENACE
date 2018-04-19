import itertools
import random
import weighting as w
random.seed()


class MENACE(object):
    def __init__(self, name):
        self.positions = self.gen_positions()
        self.hist = []
        self.name = name
        self.load()

    def verify_position(self, pos):
        Xs = 0
        Os = 0
        for c in pos:
            if c == 'X':
                Xs += 1
            if c == 'O':
                Os += 1
        pos = [pos[0:3], pos[3:6], pos[6:9]]
        if (Xs == Os) or (Xs == Os + 1):
            for i in range(3):
                r0 = pos[i][0]
                c0 = pos[0][i]
                if r0 != '0':
                    if pos[i][1] == r0:
                        if pos[i][2] == r0:
                            return False
                if c0 != '0':
                    if pos[1][i] == c0:
                        if pos[2][i] == c0:
                            return False

            d0 = pos[0][0]
            d1 = pos[0][2]
            if d0 != '0':
                if pos[1][1] == d0:
                    if pos[2][2] == d0:
                        return False
            if d1 != '0':
                if pos[1][1] == d1:
                    if pos[2][0] == d1:
                        return False
            return True
        return False

    def gen_positions(self):
        positions = {}
        for i in itertools.product('0XO', repeat=9):
            if self.verify_position(i[:]):
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

        move = w.PickMove(self.positions[s])
        if move[0] == -1:
            print(move[1])
            print(sum(move[1]))
            raise(Exception)

        self.hist.append([s, move])
        return move

    def random(self, board):
        s = ''
        for _, e in board():
            s += str(e)

        move = random.choice(self.positions[s])[0]
        return move

    def update(self, wl):
        for i, cord in self.hist:
            w.WeightAdj(i, cord, wl, self.positions)

    def save(self):
        pos_backup = {}
        with open(self.name + '.txt', 'r') as f:
            for line in f.readlines():
                row = line.split(',')
                pos_backup[row[0]] = row[1:-1]

        for k in pos_backup.keys():
            for i in range(len(pos_backup[k])):
                pos_backup[k][i] = str(self.positions[k][i][1])

        with open(self.name + '.txt', 'w') as f:
            for k in pos_backup.keys():
                f.write(k + ',')
                for e in pos_backup[k]:
                    f.write(e + ',')
                f.write('\n')

    def load(self):
        try:
            with open(self.name + '.txt', 'r') as f:
                for line in f.readlines():
                    row = line.split(',')
                    for i in range(len(row) - 2):
                        self.positions[row[0]][i][1] = float(row[i + 1])

        except IOError:
            with open(self.name + '.txt', 'w') as f:
                for k in self.positions.keys():
                    f.write(k + ',')
                    for i in self.positions[k]:
                        f.write(str(i[1]) + ',')
                    f.write('\n')


if __name__ == '__main__':
    app = MENACE()
    for i in list(app.positions.keys())[:5]:
        print(i)
        print(app.positions[i])
