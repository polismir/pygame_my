# здесь подключаются модули:
import pygame as pg

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
BALL_WIDTH, BALL_HEIGHT = WIDTH * 1 / 4, HEIGHT * 1 / 4
BROWN = (66, 53, 51)
GREY = (184, 166, 163)

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
pg.draw.circle(ball, )

# если надо до игрового цикла (=на самом старте игры) отобразить объекты, то отрисовываем их здесь:
# ...
screen.blit(background, (0, 0))  # наносим первым слоем
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

    # изменение характеристик объектов:
    # ...

    # перерисовка экрана:
    # ...
    screen.blit(background, (0, 0))  # наносим первым слоем
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
