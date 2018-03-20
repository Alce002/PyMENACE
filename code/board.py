class Board(object):
    def __init__(self):
        self.current_state = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def verify_move(self, pos, player):
        # Returns True if the correct player sends av valid move
        #         False if not
        x, y = pos
        if player == self.current_player:
            if x >= 0 and x < 3 and y >= 0 and y < 3:
                if not self.current_state[y][x]:
                    return True

        return False

    def update(self, pos, player):
        # Takes pos as (x, y) coordinates
        #       player as a string 'X' or 'O'
        # Returns player if it won
        #         0 if the game goes on
        #         1 if the game is a draw
        if self.verify_move(pos, player):
            x, y = pos
            self.current_state[y][x] = player
            self.current_player = 'X' if player == 'O' else 'O'
            win = self.is_win()
            if win == 2:
                self.current_player = None
                return player
            else:
                return win
        return -1

    def is_win(self):
        # Returns 0 if the game continues
        #         1 if the game is a draw
        #         2 if there is a winner
        state = self.current_state
        for i in range(3):
            r0 = state[i][0]
            c0 = state[0][i]
            if r0:
                if state[i][1] and state[i][1] == r0:
                    if state[i][2] and state[i][2] == r0:
                        return 2
            if c0:
                if state[1][i] and state[1][i] == c0:
                    if state[2][i] and state[2][i] == c0:
                        return 2

        d0 = state[0][0]
        d1 = state[0][2]
        if d0:
            if state[1][1] and state[1][1] == d0:
                if state[2][2] and state[2][2] == d0:
                    return 2
        if d1:
            if state[1][1] and state[1][1] == d1:
                if state[2][0] and state[2][0] == d1:
                    return 2

        for row in state:
            for col in row:
                if not col:
                    return 0

        return 1

    def output_board(self):
        # Yields a tuple with
        #        0: an (x, y) coordinate
        #        1: the move occupying that coordinate
        for y in range(3):
            for x in range(3):
                yield (x, y), self.current_state[y][x]


if __name__ == '__main__':
    def loop(p):
        board = [[0 for _ in range(3)] for _ in range(3)]
        for (x, y), s in b.output_board():
            board[y][x] = s if s else '-'

        for row in board:
            for col in row:
                print(col, end=' ')
            print()

        x, y = [int(i) for i in input('> ').split(',')]
        print()
        return b.update((x, y), p)

    b = Board()
    p = 'X'
    w = loop(p)
    while not w:
        p = 'X' if p == 'O' else 'O'
        w = loop(p)

    print()
    print('Winner is:', w)
    input()
