# здесь подключаются модули:
import pygame as pg

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 600, 700
GREY = (105, 105, 105)


class Car(pg.sprite.Sprite):

    speed = 3

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\car.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH * 1 / 2, HEIGHT * 1 / 2))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
my_car = Car()
background.fill(GREY)
my_car.draw(screen)
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    screen.blit(background, (0, 0))
    my_car.draw(screen)
    pg.display.update()
