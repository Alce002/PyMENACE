import time
import pygame as pg
import canvas
import board
import menace


class TicTacToe(canvas.Window):
    def __init__(self, size):
        super().__init__("TicTacToe", '../assets/icon.png', size)
        # Objects
        self.board = board.Board()
        self.menace = menace.MENACE('MENACE0')

        # Main menu buttons
        self.b_PvP = canvas.Button(self, pg.Rect(160, 5, 80, 20), 'PvP')
        self.b_PvC = canvas.Button(self, pg.Rect(160, 30, 80, 20), 'PvC')
        self.b_CvC = canvas.Button(self, pg.Rect(160, 55, 80, 20), 'CvC')
        self.b_quit = canvas.Button(self, pg.Rect(150, 375, 100, 20),
                                    'Quit', (255, 0, 0))

        # Player Select menu buttons
        self.b_pX = canvas.Button(self, pg.Rect(150, 5, 100, 20), 'Play as X')
        self.b_pO = canvas.Button(self, pg.Rect(150, 30, 100, 20), 'Play as O')
        self.b_back = canvas.Button(self, pg.Rect(150, 375, 100, 20), 'Back')

        # Game menu buttons
        self.b_menu = canvas.Button(self, pg.Rect(50, 5, 100, 20), 'Menu')
        self.b_replay = canvas.Button(self, pg.Rect(250, 5, 100, 20), 'Replay')
        # Game menu labels
        self.l_winner = canvas.Label(self, pg.Rect(160, 5, 80, 20), 'None')

        # Images
        self.X_tile = pg.image.load('../assets/X_tile.png')
        self.O_tile = pg.image.load('../assets/O_tile.png')

        # Internal settings
        self.cell_size = 100  # Size of a game cell
        self.player = 'X'  # Current player
        self.state = 'menu'  # Current state
        # False: No AI, X: AI plays X, O: AI plays O, XO: AI plays X&O
        self.ai = 'X'

    # Reset game
    def reset(self):
        self.board = board.Board()
        self.menace.hist = []
        self.player = 'X'

    # ____Event handlers____
    def on_mouse_down(self, event):
        # Handle "menu" state
        if self.state == 'menu':
            if self.b_PvP.is_hover(event.pos):
                self.reset()
                self.ai = False
                self.state = 'game'

            if self.b_PvC.is_hover(event.pos):
                self.reset()
                self.state = 'player_select'

            if self.b_CvC.is_hover(event.pos):
                self.reset()
                self.ai = 'XO'
                self.state = 'game'

            if self.b_quit.is_hover(event.pos):
                self.running = False

        # Handle "player_select" state
        elif self.state == 'player_select':
            if self.b_pX.is_hover(event.pos):
                self.ai = 'O'
                self.state = 'game'

            if self.b_pO.is_hover(event.pos):
                self.ai = 'X'
                self.state = 'game'

            if self.b_back.is_hover(event.pos):
                self.state = 'menu'

        # Handle "game" state
        elif self.state == 'game':
            if self.b_menu.is_hover(event.pos):
                self.state = 'menu'

            if self.board.is_win():
                if self.b_replay.is_hover(event.pos):
                    self.reset()

            else:
                x, y = pg.mouse.get_pos()
                x = (x - 50) // self.cell_size
                y = (y - 50) // self.cell_size
                if not self.board.update((x, y), self.player):
                    self.player = 'O' if self.player == 'X' else 'X'

    # ____Update methods____
    def update(self):
        # Tick setup and delegation
        # Method selected based on state
        self.canvas.fill((255, 255, 255))
        state = getattr(self, self.state, self.state_error)
        state()

    def menu(self):
        # Draw menu screen
        self.b_PvP.draw()
        self.b_PvC.draw()
        self.b_CvC.draw()
        self.b_quit.draw()

    def player_select(self):
        # Draw player select screen
        self.b_pX.draw()
        self.b_pO.draw()
        self.b_back.draw()

    def game(self):
        # Draw game screen
        self.b_menu.draw()
        if self.board.is_win():
            if self.board.is_win() == 1:
                self.l_winner.set_text("It's a draw!")
            else:
                self.l_winner.set_text(self.board.is_win() + ' wins!')

            self.l_winner.draw()
            self.b_replay.draw()

        for cord, p in self.board.output_board():
            rect = pg.Rect((50 + cord[0] * self.cell_size,
                            50 + cord[1] * self.cell_size),
                           (self.cell_size, self.cell_size))
            if p == 'X':
                self.canvas.blit(self.X_tile, rect.topleft)
            if p == 'O':
                self.canvas.blit(self.O_tile, rect.topleft)
            pg.draw.rect(self.canvas, (0, 0, 0), rect, 1)

        # Allow the AI to make its move on correct turn
        if not self.board.is_win():
            if self.ai and self.player in self.ai and not self.board.is_win():
                if self.ai == 'XO':
                    time.sleep(0.1)
                move = self.menace.gen_move(self.board.output_board)
                while self.board.update(move, self.player) == -1:
                    move = self.menace.gen_move(self.board.output_board)
                self.player = 'O' if self.player == 'X' else 'X'

    def state_error(self):
        # Called if application enters an undefined state
        print("Internal State Error")
        self.running = False


if __name__ == '__main__':
    app = TicTacToe((400, 400))
    app.mainloop()
