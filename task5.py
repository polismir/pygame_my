# здесь подключаются модули:
import pygame as pg

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
BALL_WIDTH, BALL_HEIGHT = WIDTH * 1 / 8, HEIGHT * 1 / 4
BROWN = (66, 53, 51)
GREY = (184, 166, 163)
BLUE = (79, 120, 171)
RED = (130, 39, 30)

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

ball = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball.fill((0, 0, 0, 0))
pg.draw.circle(ball, (*BLUE, 100), (BALL_WIDTH / 2, BALL_HEIGHT / 2), 40)
x, y = 0, 135
speed = 5
flag = "вправо"


ball1 = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball1.fill((0, 0, 0, 0))
pg.draw.circle(ball1, (*RED, 100), (BALL_WIDTH / 2, BALL_HEIGHT / 2), 40)
x1, y1 = 880, 335
speed1 = 7
flag1 = "влево"


# если надо до игрового цикла (=на самом старте игры) отобразить объекты, то отрисовываем их здесь:
# ...
screen.blit(background, (0, 0))  # наносим первым слоем
screen.blit(ball, (x, y))
screen.blit(ball1, (x1, y1))
pg.display.update()  # затем обновляем экран, чтобы показать изменения

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

    if x >= WIDTH:
        flag = "влево"
    if x <= -120:
        flag = "вправо"

    if flag == "вправо":
        y = 135
        x += speed
    if flag == "влево":
        y = 335
        x -= speed

    if x1 >= WIDTH:
        flag1 = "влево"
    if x1 <= -120:
        flag1 = "вправо"

    if flag1 == "вправо":
        y1 = 135
        x1 += speed1
    if flag1 == "влево":
        y1 = 335
        x1 -= speed1

    # перерисовка экрана:
    # ...
    screen.blit(background, (0, 0))  # наносим первым слоем
    screen.blit(ball, (x, y))
    screen.blit(ball1, (x1, y1))
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
