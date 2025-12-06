# здесь подключаются модули:
import pygame as pg

# здесь определяются константы, функции и классы:
FPS = 60
WIDTH, HEIGHT = 1000, 600
GREY = (177, 171, 170)


class Car:

    def init(self):
        self.car_surf = pg.image.load(r"images\car.png").convert_alpha()
        self.car_rect = self.car_surf.get_rect(center=(WIDTH * 1 / 2, HEIGHT * 1 / 2))
        self.cur_direction = "up"

    def draw(self, screen):
        screen.blit(self.car_surf, self.car_rect)

    def rotate(self, new_direction):
        if new_direction == "left":
            if self.cur_direction == "up":
                self.car_surf = pg.transform.rotate(self.car_surf, 90)
                self.cur_direction = "left"
            if self.cur_direction == "right":
                self.car_surf = pg.transform.rotate(self.car_surf, 180)
                self.cur_direction = "left"
            if self.cur_direction == "down":
                self.car_surf = pg.transform.rotate(self.car_surf, 270)
                self.cur_direction = "left"

        if new_direction == "right":
            if self.cur_direction == "up":
                self.car_surf = pg.transform.rotate(self.car_surf, 270)
                self.cur_direction = "right"
            if self.cur_direction == "left":
                self.car_surf = pg.transform.rotate(self.car_surf, 180)
                self.cur_direction = "right"
            if self.cur_direction == "down":
                self.car_surf = pg.transform.rotate(self.car_surf, 90)
                self.cur_direction = "right"

        if new_direction == "up":
            if self.cur_direction == "right":
                self.car_surf = pg.transform.rotate(self.car_surf, 90)
                self.cur_direction = "up"
            if self.cur_direction == "left":
                self.car_surf = pg.transform.rotate(self.car_surf, 270)
                self.cur_direction = "up"
            if self.cur_direction == "down":
                self.car_surf = pg.transform.rotate(self.car_surf, 180)
                self.cur_direction = "up"

        if new_direction == "down":
            if self.cur_direction == "right":
                self.car_surf = pg.transform.rotate(self.car_surf, 270)
                self.cur_direction = "down"
            if self.cur_direction == "left":
                self.car_surf = pg.transform.rotate(self.car_surf, 90)
                self.cur_direction = "down"
            if self.cur_direction == "up":
                self.car_surf = pg.transform.rotate(self.car_surf, 180)
                self.cur_direction = "down"


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
my_car = Car()
background.fill(GREY)
my_car.draw(screen)
pg.display.update()

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

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_car.rotate(new_direction="left")
    if keys[pg.K_RIGHT]:
        my_car.rotate(new_direction="right")
    if keys[pg.K_UP]:
        my_car.rotate(new_direction="up")
    if keys[pg.K_DOWN]:
        my_car.rotate(new_direction="down")

    screen.blit(background, (0, 0))
    my_car.draw(screen)
    pg.display.update()
