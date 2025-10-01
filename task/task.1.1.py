# здесь подключаются модули
import pygame as pg

# здесь определяются константы, функции и классы
FPS = 60
WIDTH, HEIGHT = 1000, 600

GREEN = (92, 153, 86)
BROWN = (122, 99, 67)
SKY = (165, 201, 217)
WHITE = (255, 255, 255)
YELLOW = (240, 245, 127)

# здесь происходит инициализация, создание объектов
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))  # также здесь можно указать битовые флаги
screen.fill(SKY)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.rect(screen, WHITE, (0, 450, 1000, 250))
pg.draw.rect(screen, BROWN, (300, 420, 50, 80))
pg.draw.polygon(screen, GREEN, [[200, 420], [320, 250], [440, 420]])
pg.draw.polygon(screen, GREEN, [[220, 320], [320, 150], [420, 320]])
pg.draw.polygon(screen, GREEN, [[240, 220], [320, 80], [400, 220]])
pg.draw.polygon(screen, YELLOW, [[270, 120], [270, 50], [320, 10], [370, 50], [370, 120], [320, 100]])
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
