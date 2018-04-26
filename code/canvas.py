import pygame as pg


class Label(object):
    def __init__(self, parent, rect, text=''):
        self.parent = parent
        self.rect = rect
        self.canvas = pg.Surface((rect.w, rect.h))
        self.font = pg.font.SysFont('Sans', 20)
        self.text = self.font.render(text, True, (0, 0, 0))

    def set_text(self, text):
        self.text = self.font.render(text, True, (0, 0, 0))

    def draw(self):
        textrect = self.text.get_rect()
        textrect.center = self.canvas.get_rect().center
        self.canvas.fill((255, 255, 255))
        self.canvas.blit(self.text, textrect)
        self.parent.canvas.blit(self.canvas, self.rect)


class Button(object):
    def __init__(self, parent, rect, text='', color=(200, 200, 200)):
        self.parent = parent
        self.rect = rect
        self.canvas = pg.Surface((rect.w, rect.h))
        self.font = pg.font.SysFont('Sans', 20)
        self.text = self.font.render(text, True, (0, 0, 0))
        self.color = color

    def draw(self):
        if self.is_hover(pg.mouse.get_pos()):
            color = self.color
        else:
            color = (255, 255, 255)

        textrect = self.text.get_rect()
        textrect.center = self.canvas.get_rect().center
        self.canvas.fill(color)
        self.canvas.blit(self.text, textrect)
        pg.draw.rect(self.canvas, (0, 0, 0), self.canvas.get_rect(), 1)
        self.parent.canvas.blit(self.canvas, self.rect)

    def is_hover(self, point):
        if self.rect.collidepoint(point):
            return True
        else:
            return False


class Window(object):
    def __init__(self, title, icon, size):
        pg.init()

        # Set display attributes
        self._screen = pg.display.set_mode(size)  # Internal pygame surface DNT
        pg.display.set_caption(title)
        pg.display.set_icon(pg.image.load(icon))

        # Internal variables
        self.canvas = pg.Surface(size)  # Pygame surface for drawing
        self.running = True  # Mainloop control

    # ___Event handlers___
    def on_event(self, event):
        # Delegate to specialized handlers
        if event.type == pg.QUIT:
            self.on_quit(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            self.on_mouse_down(event)
        if event.type == pg.KEYDOWN:
            self.on_key_down(event)

    def on_quit(self, event):
        self.running = False

    def on_mouse_down(self, event):
        pass

    def on_key_down(self, event):
        pass

    def update(self):
        self.canvas.fill((255, 255, 255))

    def mainloop(self):
        # Mainloop process:
        # - Call event handler
        # - Update internal surface
        while self.running:
            for e in pg.event.get():
                self.on_event(e)

            self.update()

            self._screen.blit(self.canvas, (0, 0))
            pg.display.update()
        pg.quit()
