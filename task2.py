import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
r = 30  # радиус круга
# координаты центра круга:
x = 10  # скрываем за левой границей
speed = 2
y = WIN_HEIGHT // 2 - 25 # выравниваем по центру по вертикали
pg.draw.rect(screen, ORANGE, [x, y, 40, 40])  # рисуем круг
pg.display.update()  # обновляем окно

flag_play = True
flag1 = "вправо"
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
    # если круг полностью скрылся за правой границей
    if x >= WIN_WIDTH - r:
        flag1 = "влево"
        speed += 1
    if x <= 0:
        flag1 = "вправо"
        speed += 1

    if flag1 == "вправо":
        x += speed
    if flag1 == "влево":
        x -= speed

    screen.fill(WHITE)  # заливаем фон, стирая предыдущий круг
    pg.draw.rect(screen, ORANGE, [x, y, 40, 40])  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
