import pygame as pg
import random
import math

FPS = 60
WIDTH, HEIGHT = 900, 819


class MyShip(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images/my_ship/my_ship.png").convert_alpha()
        self.image = pg.transform.rotate(self.image, 90)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1 / 1.20, self.image.get_height() * 1 / 1.20))
        self.rect = self.image.get_rect(center=(WIDTH * 1 / 2, HEIGHT - 100))
        self.mask = pg.mask.from_surface(self.image)

    def change_skin(self):
        self.image = pg.image.load(r"images/my_ship/myship_destroyed.png").convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed


class Shot(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images/my_ship/shot.png").convert_alpha()
        self.image = pg.transform.rotate(self.image, 90)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1 / 4, self.image.get_height() * 1 / 4))
        x = my_ship.rect.centerx
        y = my_ship.rect.centery
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= Shot.speed


class EnemyShips(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        images = [(r'images/enemy_ships/enemy_ship1.png', 1.3), (r'images/enemy_ships/enemy_ship2.png', 1.5), (r'images/enemy_ships/enemy_ship3.png', 1.5),
                  (r'images/enemy_ships/enemy_ship4.png', 2)]
        random_image, k = random.choice(images)
        self.image = pg.image.load(random_image).convert_alpha()
        self.image = pg.transform.rotate(self.image,  270)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * k, self.image.get_height() * k))
        self.random_start = random.randint(100, 800)
        self.rect = self.image.get_rect(center=(self.random_start, 0))
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
        self.random_start = random.randint(100, 800)
        self.rect = self.image.get_rect(center=(self.random_start, 0))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += Meteors.speed


class Heart(pg.sprite.Sprite):

    def __init__(self, k):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images/my_ship/heart.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1 / 9, self.image.get_height() * 1 / 9))
        if k == 1:
            self.rect = self.image.get_rect(center=(WIDTH * 1 / 16, HEIGHT - 760))
        if k == 2:
            self.rect = self.image.get_rect(center=(WIDTH * 1 / 7, HEIGHT - 760))
        if k == 3:
            self.rect = self.image.get_rect(center=(WIDTH * 1 / 4.5, HEIGHT - 760))
        self.active = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.image.load(r"images/cosmic_background.png")

my_ship = MyShip()
heart1 = Heart(1)
heart2 = Heart(2)
heart3 = Heart(3)
enemy_ships = pg.sprite.Group()
meteors = pg.sprite.Group()
shots = pg.sprite.Group()

pg.mixer.music.load("music/background_music.wav")
pg.mixer.music.play()
s = pg.mixer.Sound("music/destructions_music.wav")
shot_song = pg.mixer.Sound("music/shot_music.wav")

screen.blit(background, (0, 0))
enemy_ships.draw(screen)
my_ship.draw(screen)
meteors.draw(screen)
heart1.draw(screen)
heart2.draw(screen)
heart3.draw(screen)
pg.display.update()

cnt = 0
cnt1 = 0
flag_play = True
while flag_play:
    clock.tick(FPS)
    cnt += 1
    cnt1 += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    if cnt == 120:
        choices = ("meteor", "enemy ship")
        cur_choice = random.choice(choices)
        if cur_choice == "meteor":
            meteors.add(Meteors())
        else:
            enemy_ships.add(EnemyShips())
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
    if keys[pg.K_SPACE] and cnt1 >= 60:
        shots.add(Shot())
        shot_song.play()
        cnt1 = 0

    meteors.update()
    enemy_ships.update()
    shots.update()

    screen.blit(background, (0, 0))
    enemy_ships.draw(screen)
    shots.draw(screen)
    my_ship.draw(screen)
    meteors.draw(screen)
    if heart1.active:
        heart1.draw(screen)
    if heart2.active:
        heart2.draw(screen)
    if heart3.active:
        heart3.draw(screen)
    pg.display.update()


    if pg.sprite.spritecollideany(my_ship, meteors, collided=pg.sprite.collide_mask):
        if heart3.active:
            heart3.active = False
        elif heart2.active:
            heart2.active = False
        elif heart1.active:
            heart1.active = False
            s.play()
            my_ship.change_skin()
            miliseconds = math.ceil(s.get_length()) * 1000
            pg.time.wait(miliseconds)
            break
        meteors.empty()
    if pg.sprite.spritecollideany(my_ship, enemy_ships, collided=pg.sprite.collide_mask):
        if heart3.active:
            heart3.active = False
        elif heart2.active:
            heart2.active = False
        elif heart1.active:
            heart1.active = False
            s.play()
            my_ship.change_skin()
            miliseconds = math.ceil(s.get_length()) * 1000
            pg.time.wait(miliseconds)
            break
        enemy_ships.empty()
    if pg.sprite.groupcollide(shots, meteors, True, True, collided=pg.sprite.collide_mask):
        pass
    if pg.sprite.groupcollide(shots, enemy_ships, True, True, collided=pg.sprite.collide_mask):
        pass
