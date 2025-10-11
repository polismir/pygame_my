import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
# координаты центра круга
r = 30  # радиус круга
x, y = random.randint(0, 600), random.randint(0, 500)
pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно

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

    screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
