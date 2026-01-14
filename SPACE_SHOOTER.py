import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600


class MyShip(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\my_ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH * 1 / 2, HEIGHT * 1 / 2))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()
