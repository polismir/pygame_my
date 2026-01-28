import pygame as pg
import random
import math

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

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        images = [(r'images/meteors/meteor_01.png', 0.5), (r'images/meteors/meteor_02.png', 0.333), (r'images/meteors/meteor_03.png', 0.333), (r'images/meteors/meteor_04.png', 0.333),
                  (r'images/meteors/meteor_05.png', 0.333), (r'images/meteors/meteor_06.png', 0.333), (r'images/meteors/meteor_07.png', 0.333), (r'images/meteors/meteor_08.png', 0.333)]
        random_image, k = random.choice(images)
        self.image = pg.image.load(random_image).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * k, self.image.get_height() * k))
        self.random_start = random.randint(150, 800)
        self.rect = self.image.get_rect(center=(self.random_start, 0))
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

s = pg.mixer.Sound("music/destructions_music.wav")

screen.blit(background, (0, 0))
enemy_ships.draw(screen)
my_ship.draw(screen)
meteors.draw(screen)
pg.display.update()

cnt = 0
flag_play = True
while flag_play:
    clock.tick(FPS)
    cnt += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    if cnt == 120:
        meteors.add(Meteors())
        cnt = 0

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_ship.update(dx=-1)
    if keys[pg.K_RIGHT]:
        my_ship.update(dx=1)
    if keys[pg.K_UP]:
        my_ship.update(dy=-1)
    if keys[pg.K_DOWN]:
        my_ship.update(dy=1)

    meteors.update()

    screen.blit(background, (0, 0))
    enemy_ships.draw(screen)
    my_ship.draw(screen)
    meteors.draw(screen)
    pg.display.update()

    if pg.sprite.spritecollideany(my_ship, meteors, collided=pg.sprite.collide_mask):
        s.play()
        miliseconds = math.ceil(s.get_length()) * 1000
        pg.time.wait(miliseconds)
        break
