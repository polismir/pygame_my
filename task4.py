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
x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)
pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно

while 1:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 4:
            pos = pg.mouse.get_pos()
            dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
            if dist <= r and r <= 150:
                r += 2
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 5:
            pos = pg.mouse.get_pos()
            dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
            if dist <= r and r >= 10:
                r -= 2

    pressed = pg.mouse.get_pressed()
    if pressed[1]:
        pos = pg.mouse.get_pos()
        dist = ((pos[0]-x)**2 + (pos[1]-y)**2) ** 0.5
        if dist <= r:
            x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)
    if pressed[0]:
        pos = pg.mouse.get_pos()
        dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
        if dist <= r and r <= 150:
            r += 1
    if pressed[2]:
        pos = pg.mouse.get_pos()
        dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
        if dist <= r and r >= 10:
            r -= 1


    screen.fill(MINT) # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
