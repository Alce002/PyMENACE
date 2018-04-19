import pygame as pg
import canvas
import board
import menace


class TicTacToe(canvas.Window):
    def __init__(self, size):
        super().__init__("TicTacToe", '../assets/icon.png', size)
        self.cell_size = 100
        self.player = 'X'
        self.board = board.Board()
        self.menace = menace.MENACE('MENACE1')
        self.X_tile = pg.image.load('../assets/X_tile.png')
        self.O_tile = pg.image.load('../assets/O_tile.png')
        self.state = 'menu'

    def on_mouse_down(self, event):
        if not self.board.is_win():
            x, y = pg.mouse.get_pos()
            x = (x - 50) // self.cell_size
            y = (y - 50) // self.cell_size
            print((x, y), self.player)
            if not self.board.update((x, y), self.player):
                self.player = 'O' if self.player == 'X' else 'X'

    def update(self):
        getattr(self, self.state, self.state_error)()

    def menu(self):
        self.state = 'game'

    def game(self):
        if self.board.is_win():
            self.canvas.fill((0, 255, 0))
        else:
            self.canvas.fill((255, 255, 255))
        for cord, p in self.board.output_board():
            rect = pg.Rect((50 + cord[0] * self.cell_size,
                            50 + cord[1] * self.cell_size),
                           (self.cell_size, self.cell_size))
            if p == 'X':
                self.canvas.blit(self.X_tile, rect.topleft)
            if p == 'O':
                self.canvas.blit(self.O_tile, rect.topleft)
            pg.draw.rect(self.canvas, (0, 0, 0), rect, 1)

        if self.player == 'X':
            move = self.menace.gen_move(self.board.output_board)
            while self.board.update(move, self.player) == -1:
                move = self.menace.gen_move(self.board.output_board)
            self.player = 'O' if self.player == 'X' else 'X'

    def state_error(self):
        print("Internal State Error")
        pg.event.post(pg.QUIT)


if __name__ == '__main__':
    app = TicTacToe((400, 400))
    app.mainloop()
