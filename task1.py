# здесь подключаются модули
import pygame as pg

# здесь определяются константы, функции и классы
FPS = 60
WIDTH, HEIGHT = 1000, 600

BEIGE = (209, 196, 142)
BLUE = (142, 177, 209)
GREY = (181, 178, 168)
SKY = (165, 201, 217)
WHITE = (255, 255, 255)

# здесь происходит инициализация, создание объектов
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))  # также здесь можно указать битовые флаги
screen.fill(BLUE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.rect(screen, BEIGE, (250, 300, 500, 300))
pg.draw.rect(screen, GREY, (250, 300, 500, 300), 15)
pg.draw.polygon(screen, GREY, [[500, 150], [250, 300], [750, 300]])
pg.draw.rect(screen, SKY, (420, 350, 150, 150))
pg.draw.rect(screen, GREY, (420, 350, 150, 150), 10)
pg.draw.rect(screen, GREY, (485, 350, 20, 150))
pg.draw.rect(screen, GREY, (420, 415, 150, 20))
pg.draw.circle(screen, WHITE, (150, 150), 50)
pg.draw.circle(screen, WHITE, (200, 130), 50)
pg.draw.circle(screen, WHITE, (250, 150), 50)
pg.draw.circle(screen, WHITE, (200, 165), 50)
pg.draw.circle(screen, WHITE, (800, 200), 50)
pg.display.update()

# главный цикл
flag_play = True
while flag_play:
    # настраиваем частоту итераций в секунду
    clock.tick(FPS)

    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение объектов
    # ...

    # обновление экрана
    pg.display.update()
