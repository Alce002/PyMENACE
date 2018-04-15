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

        move = w.PickMove(self.positions[s])
        if move[0] == -1:
            print(move[1])
            print(sum(move[1]))
            raise(Exception)
        # move = random.choice(self.positions[s])[0]
        self.hist.append([s, move])
        
        return move
        
    def update(self, wl):
        for i, cord in self.hist:
            w.WeightAdj(i, cord, wl, self.positions)
        self.hist=[]

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
