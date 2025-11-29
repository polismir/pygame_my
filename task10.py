# здесь подключаются модули:
import pygame as pg
import random

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
BLUE = (135, 206, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLUE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(BLUE)


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

    screen.blit(background, (0, 0))
    pg.display.update()
