import pygame as pg
import random
import time

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
x, y = WIDTH / 2, HEIGHT / 2  # координаты центра круга
r = 30  # радиус круга
color = ORANGE
pg.draw.circle(screen, color, (x, y), r)  # рисуем круг
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

    # изменение состояний объектов:
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x - r > 0:
        x -= 3
    if keys[pg.K_RIGHT] and x < WIDTH - r:
        x += 3
    if keys[pg.K_UP] and y - r > 0:
        y -= 3
    if keys[pg.K_DOWN] and y < HEIGHT - r:
        y += 3
    if keys[pg.K_SPACE]:
        number1, number2, number3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random_color = (number1, number2, number3)
        color = random_color
        time.sleep(0.2)

    screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, color, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
