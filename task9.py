# здесь подключаются модули:
import pygame as pg
import random

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (52, 52, 153)
RED = (178, 34, 34)
DARK_RED = (139, 0, 0)
GREEN = (0, 128, 0)

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

    def start_radius(self):
        self.r = 20
        pg.draw.circle(self.player_surf, (*BLACK, 255),
                       (self.player_rect.width / 2, self.player_rect.height / 2), self.r)

def check_collisions(player, foods):
    for food in foods:
        if food.active == True:
            offset = (food.food_rect.x - player.player_rect.x, food.food_rect.y - player.player_rect.y)
            if player.mask.overlap(food.mask, offset) is not None:
                food.active = False
                foods.append(Food())
                player.eat(food.random_size)


class Text:
    def __init__(self, text_size, text, text_color, text_pos):
        self.font = pg.font.SysFont(None, text_size)
        self.surf = self.font.render(text, True, text_color)
        self.rect = self.surf.get_rect(center=text_pos)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


class Button:
    def __init__(self, text_size, text, text_color, button_color, button_cover_color, button_pos):
        self.button_color = button_color
        self.button_cover_color = button_cover_color
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        self.button_surf = pg.Surface((self.text_surf.get_width() + 50, self.text_surf.get_height() + 50))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def redraw(self, state):
        if state:
            self.button_surf.fill(self.button_cover_color)
            pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)
        else:
            self.button_surf.fill(self.button_color)
            pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        screen.blit(self.button_surf, self.button_rect)
        screen.blit(self.text_surf, self.text_rect)


def check_click_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        player.start_radius()


def check_mouse_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        button.redraw(state=True)
    else:
        button.redraw(state=False)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

my_text = Text(32, "Это просто текст", GREEN, (WIDTH / 2, HEIGHT * 1 / 8))
my_button = Button(64, "Кнопка", BLACK, RED, DARK_RED, (WIDTH / 2, HEIGHT * 2 / 2.5))

foods = [Food(), Food(), Food(), Food(), Food()]
player = Player()

screen.fill(WHITE)
for elem in foods:
    elem.draw(screen)
player.draw(screen)
my_text.draw(screen)
my_button.draw(screen)
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            check_click_on_button(my_button)
    if not flag_play:
        break

    check_mouse_on_button(my_button)

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
    my_text.draw(screen)
    my_button.draw(screen)
    pg.display.update()
