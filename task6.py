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
ball_rect = ball.get_rect(centerx=WIDTH * 1 / 8)
ball_rect.top = HEIGHT * 1 / 4
ball.fill((0, 0, 0, 0))
pg.draw.circle(ball, (*BLUE, 100),(ball_rect.width / 2, ball_rect.height / 2 - 10), 40)
speed = 5
flag = "вправо"


ball1 = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball1_rect = ball.get_rect(centerx=WIDTH * 1 / 8)
ball1_rect.top = HEIGHT * 1 / 4
ball1.fill((0, 0, 0, 0))
pg.draw.circle(ball1, (*RED, 100),(ball1_rect.width / 2, ball1_rect.height / 2 - 10), 40)
speed1 = 7
flag1 = "вправо"


# если надо до игрового цикла (=на самом старте игры) отобразить объекты, то отрисовываем их здесь:
# ...
screen.blit(background, (0, 0))  # наносим первым слоем
screen.blit(ball, ball_rect)
screen.blit(ball1, ball1_rect)
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

    if ball_rect.left >= WIDTH:
        flag = "влево"
        ball_rect.top = HEIGHT * 1 / 1.75
    if ball_rect.left <= -120:
        flag = "вправо"
        ball_rect.top = HEIGHT * 1 / 4

    if flag == "вправо":
        ball_rect.right += speed
    if flag == "влево":
        ball_rect.left -= speed

    if ball1_rect.left >= WIDTH:
        flag1 = "влево"
        ball1_rect.top = HEIGHT * 1 / 1.75
    if ball1_rect.left <= -120:
        flag1 = "вправо"
        ball1_rect.top = HEIGHT * 1 / 4

    if flag1 == "вправо":
        ball1_rect.right += speed1
    if flag1 == "влево":
        ball1_rect.left -= speed1

    # перерисовка экрана:
    # ...
    screen.blit(background, (0, 0))  # наносим первым слоем
    screen.blit(ball, ball_rect)
    screen.blit(ball1, ball1_rect)
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
