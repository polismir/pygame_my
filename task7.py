# здесь подключаются модули:
import pygame as pg
import random

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
BALL_WIDTH, BALL_HEIGHT = WIDTH * 1 / 8, HEIGHT * 1 / 4
BROWN = (66, 53, 51)
GREY = (184, 166, 163)
BLUE = (79, 120, 171)
RED = (130, 39, 30)


class Ball:
    SIZE = HEIGHT * 1 / 4

    def __init__(self):
        self.speed = random.randint(0, 25)
        number1, number2, number3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.random_color = (number1, number2, number3)
        self.random_size = random.randint(5, 55)

        self.ball_surf = pg.Surface((Ball.SIZE, Ball.SIZE), pg.SRCALPHA)
        self.ball_rect = self.ball_surf.get_rect(centerx=WIDTH * 1 / 15)
        self.ball_rect.top = HEIGHT * 1 / 4
        self.ball_surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.ball_surf, (*self.random_color, 100), (self.ball_rect.width / 2, self.ball_rect.height / 2 - 15), self.random_size)

    def draw(self, screen):  # отрисовка снаряда на экране слоем self.surf
        screen.blit(self.ball_surf, self.ball_rect)

    def move(self):
        if self.ball_rect.top == HEIGHT * 1 / 4:
            if self.ball_rect.left <= WIDTH:
                self.ball_rect.right += self.speed
            else:
                self.ball_rect.top = HEIGHT * 1 / 1.75
        else:
            if self.ball_rect.top == HEIGHT * 1 / 1.75:
                if self.ball_rect.right >= WIDTH:
                    self.ball_rect.left -= self.speed
                else:
                    self.ball_rect.top = HEIGHT * 1 / 4


# здесь происходит инициализация:
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))  # здесь можно указать и другие настройки экрана (битовые флаги)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# здесь происходит создание игровых объектов:
background = pg.Surface((WIDTH, HEIGHT))
background.fill(BROWN)
pg.draw.rect(background, GREY, (0, 150, WIDTH, 120))
pg.draw.rect(background, GREY, (0, 350, WIDTH, 120))

balls = [Ball(), Ball()]

screen.blit(background, (0, 0))
for elem in balls:
    elem.draw(screen)
pg.display.update()

# главный игровой цикл:
flag_play = True
while flag_play:
    clock.tick(FPS)  # настраиваем FPS (=частоту итераций в секунду)

    # цикл обработки событий:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    for elem in balls:
        elem.move()

    screen.blit(background, (0, 0))
    for elem in balls:
        elem.draw(screen)
    pg.display.update()
