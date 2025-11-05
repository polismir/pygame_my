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
        self.ball_rect = self.ball_surf.get_rect(centerx=WIDTH * 1 / 8)
        self.ball_rect.top = HEIGHT * 1 / 4
        self.ball_surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.ball_surf, (*self.random_color, 100), (self.ball_rect.width / 2, self.ball_rect.height / 2 - 15), self.random_size)

    def draw(self, screen):  # отрисовка снаряда на экране слоем self.surf
        screen.blit(self.ball_surf, self.ball_rect)

    def move_left(self):
        if self.ball_rect.left > self.speed:
            self.ball_rect.left -= self.speed

    def move_right(self):
        if self.ball_rect.right < BALL_WIDTH - self.speed:
            self.ball_rect.right += self.speed

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

my_ball = Ball()
screen.blit(background, (0, 0))
my_ball.draw(screen)
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

    # if ball_rect.left >= WIDTH:
    #     flag = "влево"
    #     ball_rect.top = HEIGHT * 1 / 1.75
    # if ball_rect.left <= -120:
    #     flag = "вправо"
    #     ball_rect.top = HEIGHT * 1 / 4
    #
    # if flag == "вправо":
    #     ball_rect.right += speed
    # if flag == "влево":
    #     ball_rect.left -= speed
    #
    # if ball1_rect.left >= WIDTH:
    #     flag1 = "влево"
    #     ball1_rect.top = HEIGHT * 1 / 1.75
    # if ball1_rect.left <= -120:
    #     flag1 = "вправо"
    #     ball1_rect.top = HEIGHT * 1 / 4
    #
    # if flag1 == "вправо":
    #     ball1_rect.right += speed1
    # if flag1 == "влево":
    #     ball1_rect.left -= speed1
    #
    # # перерисовка экрана:
    # # ...
    # screen.blit(background, (0, 0))  # наносим первым слоем
    # screen.blit(ball, ball_rect)
    # screen.blit(ball1, ball1_rect)
    # pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
