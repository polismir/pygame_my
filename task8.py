# здесь подключаются модули:
import pygame as pg
import random

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (52, 52, 153)


class Food:
    SIZE = 75

    def __init__(self):
        self.random_size = random.randint(5, 35)
        random_x = random.randint(self.random_size, WIDTH - self.random_size)
        random_y = random.randint(self.random_size, HEIGHT - self.random_size)

        self.food_surf = pg.Surface((Food.SIZE, Food.SIZE), pg.SRCALPHA)
        self.food_rect = self.food_surf.get_rect(center=(random_x, random_y))
        self.food_surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.food_surf, (*BLUE, 255),
                       (self.food_rect.width / 2, self.food_rect.height / 2), self.random_size)
        self.active = True
        self.mask = pg.mask.from_surface(self.food_surf)

    def draw(self, screen):
        screen.blit(self.food_surf, self.food_rect)


class Player:
    SPEED = 3
    SIZE = 200

    def __init__(self):
        self.player_surf = pg.Surface((Player.SIZE, Player.SIZE), pg.SRCALPHA)
        self.player_rect = self.player_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.player_surf.fill((0, 0, 0, 0))
        self.r = 20
        pg.draw.circle(self.player_surf, (*BLACK, 255),
                       (self.player_rect.width / 2, self.player_rect.height / 2), self.r)
        self.speed = Player.SPEED
        self.mask = pg.mask.from_surface(self.player_surf)

    def move(self, dx=0, dy=0):
        if (self.player_rect.left + dx * self.speed) > 0 and (self.player_rect.right + dx * self.speed) < WIDTH:
            self.player_rect.x += dx * self.speed
        if (self.player_rect.top + dy * self.speed) > 0 and (self.player_rect.bottom + dy * self.speed) < HEIGHT:
            self.player_rect.y += dy * self.speed

    def eat(self, r):
        if self.r <= 90:
            self.r += r / 5
            self.player_surf.fill((0, 0, 0, 0))
            pg.draw.circle(self.player_surf, (*BLACK, 255),
                    (self.player_rect.width / 2, self.player_rect.height / 2), self.r)
            self.mask = pg.mask.from_surface(self.player_surf)
    def draw(self, screen):
        screen.blit(self.player_surf, self.player_rect)


def check_collisions(player, foods):
    for food in foods:
        if food.active == True:
            offset = (food.food_rect.x - player.player_rect.x, food.food_rect.y - player.player_rect.y)
            if player.mask.overlap(food.mask, offset) is not None:
                food.active = False
                foods.append(Food())
                player.eat(food.random_size)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

foods = [Food(), Food(), Food(), Food(), Food()]
player = Player()

screen.fill(WHITE)
for elem in foods:
    elem.draw(screen)
player.draw(screen)
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
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    check_collisions(player, foods)

    screen.fill(WHITE)
    for elem in foods:
        if elem.active == True:
            elem.draw(screen)
    player.draw(screen)
    pg.display.update()
