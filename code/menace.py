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

    def rotate(self, board):  # Input board must be copy
        clone = []
        for n in board:
            clone.append(list(n))
        for y in range(3):
            for x in range(3):
                tup = (x-1, y-1)

                turn = (y-1, -x+1)

                board[turn[1]+1][turn[0]+1] = clone[y][x]

        return board

    def rotate_move(self, move, n):
        if n > 0:
            x = move[0]-1
            y = move[1]-1
            for _ in range(4-n):

                c = x
                x = y
                y = -c

            x += 1
            y += 1
            return x, y
        else:
            return move

    def verify_position(self, pos, position):
        # Check that a position is valid for use in position list
        # Return: True if position is valid
        #         False if position is invalid
        Xs = 0
        Os = 0
        for c in pos:
            if c == 'X':
                Xs += 1
            if c == 'O':
                Os += 1
        pos = [list(pos[0:3]), list(pos[3:6]), list(pos[6:9])]

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

            for n in range(3):
                s = ""
                positions = position
                reference = self.rotate(pos)
                for n in reference:
                    for e in n:
                        s += str(e)
                if s in positions.keys():
                    return False
            return True
        return False

    def gen_positions(self):
        # Returns a dictionary with all valid positions keyed
        # to open moves and initial weights
        # Example entry: 'XOXOXO000': [[(0, 2), 0], [(1, 2), 0], [(2, 2), 0]]
        positions = {}

        for i in itertools.product('0XO', repeat=9):
            if self.verify_position(i[:], positions):
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
        # Generates a move based on stored weights
        counter = 0
        verify = False

        s = ''

        for _, e in board():
            s += str(e)

        board_clone = [list(s[0:3]), list(s[3:6]), list(s[6:9])]

        while s not in self.positions.keys():
            board_clone = self.rotate(board_clone)

            s = ''

            for k in board_clone:
                for n in k:
                    s += n

            counter += 1

        move = w.PickMove(self.positions[s])
        self.hist.append((s, move))
        return (self.rotate_move(move, counter))

        if move[0] == -1:
            print(move[1])
            print(sum(move[1]))
            raise(Exception)

        self.hist.append([s, move])
        return move

    def random(self, board):
        # Generates a truly random move
        s = ''
        for _, e in board():
            s += str(e)

        move = random.choice(self.positions[s])[0]
        return move

    def update(self, wl):
        # Updates all weights for concerned moves in history
        for i, cord in self.hist:
            w.WeightAdj(i, cord, wl, self.positions)

    def save(self):
        # Saves weightlist to text file
        pos_backup = {}
        with open(self.name + '.dat', 'r') as f:
            for line in f.readlines():
                row = line.split(',')
                pos_backup[row[0]] = row[1:-1]

        for k in pos_backup.keys():
            for i in range(len(pos_backup[k])):
                pos_backup[k][i] = str(self.positions[k][i][1])

        with open(self.name + '.dat', 'w') as f:
            for k in pos_backup.keys():
                f.write(k + ',')
                for e in pos_backup[k]:
                    f.write(e + ',')
                f.write('\n')

    def load(self):
        # Load weightlist from text file, create new file if not exist
        try:
            with open(self.name + '.dat', 'r') as f:
                for line in f.readlines():
                    row = line.split(',')
                    for i in range(len(row) - 2):
                        self.positions[row[0]][i][1] = float(row[i + 1])

        except IOError:
            with open(self.name + '.dat', 'w') as f:
                for k in self.positions.keys():
                    f.write(k + ',')
                    for i in self.positions[k]:
                        f.write(str(i[1]) + ',')
                    f.write('\n')
