# здесь подключаются модули:
import pygame as pg
import random

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 600, 700
GREY = (105, 105, 105)
WHITE = (255, 255, 255)


class Car(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\car.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH * 1 / 2, HEIGHT - 50))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed


class EnemyСar(pg.sprite.Sprite):

    speed = 5

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        images = [r'images/car1.png', r'images/car2.png', r'images/car3.png']
        random_image = random.choice(images)
        self.image = pg.image.load(random_image).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1.3, self.image.get_height() * 1.3))
        self.random_start = random.randint(20, 580)
        self.rect = self.image.get_rect(center=(self.random_start, 0))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += EnemyСar.speed


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(GREY)
pg.draw.rect(background, WHITE, (170, 0, 30, 700))
pg.draw.rect(background, WHITE, (400, 0, 30, 700))


my_car = Car()
enemy_cars = pg.sprite.Group()

screen.blit(background, (0, 0))
enemy_cars.draw(screen)
my_car.draw(screen)
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

    if cnt == 60:
        enemy_cars.add(EnemyСar())
        cnt = 0

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_car.update(dx=-1)
    if keys[pg.K_RIGHT]:
        my_car.update(dx=1)
    if keys[pg.K_UP]:
        my_car.update(dy=-1)
    if keys[pg.K_DOWN]:
        my_car.update(dy=1)

    enemy_cars.update()

    screen.blit(background, (0, 0))
    my_car.draw(screen)
    enemy_cars.draw(screen)
    pg.display.update()
