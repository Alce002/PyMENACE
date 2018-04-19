import pygame as pg


class Window(object):
    def __init__(self, title, icon, size):
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(title)
        pg.display.set_icon(pg.image.load(icon))
        self.canvas = pg.Surface(size)
        self.running = True

    def on_event(self, event):
        if event.type == pg.QUIT:
            self.on_quit(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            self.on_mouse_down(event)

    def on_quit(self, event):
        self.running = False

    def on_mouse_down(self, event):
        pass

    def update(self):
        self.canvas.fill((255, 255, 255))

    def mainloop(self):
        while self.running:
            for e in pg.event.get():
                self.on_event(e)

            self.update()

            self.screen.blit(self.canvas, (0, 0))
            pg.display.update()
        pg.quit()


if __name__ == '__main__':
    app = Window('Window', (600, 400))
    app.mainloop()
