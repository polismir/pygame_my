import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 900, 819


class MyShip(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\my_ship\myship_move.png").convert_alpha()
        self.image = pg.transform.rotate(self.image, 90)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1 / 1.20, self.image.get_height() * 1 / 1.20))
        self.rect = self.image.get_rect(center=(WIDTH * 1 / 2, HEIGHT - 100))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed

    def shot(self):
        self.image = pg.image.load(r"images\my_ship\myship_attack.png").convert_alpha()



class EnemyShips(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        images = [r'images/enemy_ship1.png', r'images/enemy_ship2.png', r'images/enemy_ship3.png',
                  r'images/enemy_ship4.png']
        random_image = random.choice(images)
        self.image = pg.image.load(random_image).convert_alpha()
        self.image = pg.transform.rotate(self.image, 270)
        self.random_start = random.randint(50, 950)
        self.rect = self.image.get_rect(center=(1000, self.random_start))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += EnemyShips.speed


class Meteors(pg.sprite.Sprite):

    speed = 3

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        images = [(r'images/meteors/meteor_01.png', 0.5), (r'images/meteors/meteor_02.png', 0.333), (r'images/meteors/meteor_03.png', 0.333), (r'images/meteors/meteor_04.png', 0.333),
                    r'images/meteors/meteor_05.png', r'images/meteors/meteor_06.png', r'images/meteors/meteor_07.png', r'images/meteors/meteor_08.png']
        # random_image = random.choice(images)
        random_image = images[3]
        self.image = pg.image.load(random_image).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1 / 3, self.image.get_height() * 1 / 3))
        self.random_start = random.randint(100, 900)
        self.rect = self.image.get_rect(center=(WIDTH / 2, 200))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += Meteors.speed


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.image.load(r"images/cosmic_background.png")

my_ship = MyShip()
enemy_ships = pg.sprite.Group()
meteors = pg.sprite.Group()

my_meteor = Meteors()

screen.blit(background, (0, 0))
enemy_ships.draw(screen)
my_ship.draw(screen)
meteors.draw(screen)
my_meteor.draw(screen)
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

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_ship.update(dx=-1)
    if keys[pg.K_RIGHT]:
        my_ship.update(dx=1)
    if keys[pg.K_UP]:
        my_ship.update(dy=-1)
    if keys[pg.K_DOWN]:
        my_ship.update(dy=1)

    screen.blit(background, (0, 0))
    enemy_ships.draw(screen)
    my_ship.draw(screen)
    meteors.draw(screen)
    my_meteor.draw(screen)
    pg.display.update()
