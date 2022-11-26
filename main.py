import operator
import random

import pygame
import math
import time
from pygame import mixer

from button import Button
from resolution import res, image_position

pygame.init()

width = 1920
height = 1080
flags = pygame.HWSURFACE | pygame.FULLSCREEN
game_screen = pygame.display.set_mode((width, height), flags, vsync=1)

first_map = res(pygame.image.load("images/first_map.png"), 0.75).convert_alpha()
first_map_border = res(pygame.image.load("images/first_map_border.png"), 0.75).convert_alpha()

second_map = res(pygame.image.load("images/second_map.png"), 0.75).convert_alpha()
second_map_border = res(pygame.image.load("images/second_map_border.png"), 0.75).convert_alpha()

blue_formula = res(pygame.image.load("images/formula_blue.png"), 1.05).convert_alpha()
red_formula = res(pygame.image.load("images/formula_red.png"), 1.05).convert_alpha()
purple_formula = res(pygame.image.load("images/formula_purple.png"), 1.05).convert_alpha()

blue_lambo = res(pygame.image.load("images/blue_lambo.png"), 0.85).convert_alpha()
pink_lambo = res(pygame.image.load("images/pink_lambo.png"), 0.85).convert_alpha()

menu_background = res(pygame.image.load("images/blue_grey_gradient.jpg"), 1).convert_alpha()
finish_line = res(pygame.image.load("images/finish_line.png"), 1.11).convert_alpha()
button_image = res(pygame.image.load("images/button.png"), 1).convert_alpha()

esc_menu = res(pygame.image.load("images/esc_menu.png"), 1).convert_alpha()
time_menu = res(pygame.image.load("images/time_menu.png"), 1).convert_alpha()
car_selection_menu = res(pygame.image.load("images/car_selection_background.png"), 1.5).convert_alpha()

formula_selection = res(pygame.image.load("images/blue_formula_selection.png"), 2).convert_alpha()
lambo_selection = res(pygame.image.load("images/blue_lambo_selection.png"), 2).convert_alpha()

icon_formula = pygame.image.load("images/icons/streaming.png").convert_alpha()
pygame.display.set_icon(icon_formula)

font = pygame.font.SysFont("impact", 60)
small_font = pygame.font.SysFont("impact", 20)
second_font = pygame.font.SysFont("impact", 100)


def draw_text(text, font, color, x, y):
    set_font = font.render(text, True, color)
    game_screen.blit(set_font, (x, y))


global car_type
global race_rounds
global started
global countdown
global last_count
global start_time


class Car:

    def __init__(self):
        self.car_image = self.car_image
        self.x = self.x_position
        self.y = self.y_position
        self.car_speed = 0
        self.car_acceleration = 0.2
        self.max_speed = 3
        self.min_speed = -1
        self.movement_speed = 2
        self.max_movement_speed = 2.5
        self.car_angle = self.car_angle
        self.car_nitro = 5

    def rotate_left(self):
        self.car_angle += self.movement_speed

    def rotate_right(self):
        self.car_angle -= self.movement_speed

    def render_position(self, game_window):
        image_position(game_window, self.car_image, (self.x, self.y), self.car_angle)

    def movement(self):

        plane_angle = self.car_angle * math.pi / 180

        self.x += -self.car_speed * math.sin(plane_angle)
        self.y += -self.car_speed * math.cos(plane_angle)

    def forward_control(self):

        while self.car_speed <= self.max_speed:
            self.car_speed = self.car_speed + self.car_acceleration

        else:
            self.car_speed = self.max_speed

        self.movement()

    def forward_slowdown(self):

        if self.car_speed > 0:
            self.car_speed = self.car_speed - self.car_acceleration / 6

        else:
            self.car_speed = 0

        self.movement()

    def backward_control(self):

        while self.car_speed <= self.min_speed:
            self.car_speed = -self.car_acceleration

        else:
            self.car_speed = self.min_speed

        self.movement()

    def nitro(self):
        self.car_speed = self.car_speed + self.car_nitro

        self.movement()

    def drift(self):

        while self.movement_speed <= self.max_movement_speed:
            self.movement_speed = self.movement_speed + (self.movement_speed / 8)

        else:
            self.movement_speed = self.movement_speed


class Player(Car):
    x_position = 700
    y_position = 950
    car_image = blue_formula
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def first_map_car(self):
        self.car_image = blue_formula

    def second_map_car(self):
        self.car_image = blue_lambo

    def respawn(self):
        self.x = 700
        self.y = 950
        self.car_angle = 270

    def respawn_second_map(self):
        self.x = 1000
        self.y = 850
        self.car_angle = 270

    def out_of_map(self):
        if self.x >= width or self.x <= 0:
            self.respawn()
        if self.y >= height or self.y <= 0:
            self.respawn()

    def out_of_track(self):
        self.car_speed = 0
        self.car_speed = self.car_speed - 5.6

        self.movement()

    def car_collide(self):
        self.max_speed = 0.1
        # self.car_image = pink_lambo

        self.movement()

    def border_collide(self, car_hitbox):
        image_hitbox = pygame.mask.from_surface(self.car_image)
        car_position = self.x, self.y
        out_of_track = car_hitbox.overlap(image_hitbox, car_position)

        return out_of_track

    def car_info(self):

        draw_text(f"Y - ( {round(self.y)} )", small_font, "white", 1740, 970)
        draw_text(f"X - ( {round(self.x)} )", small_font, "white", 1740, 940)
        draw_text(f"MOVEMENT - ( {round(self.movement_speed)} )", small_font, "white", 1590, 970)
        draw_text(f"SPEED - ( {round(self.car_speed)} )", small_font, "white", 1620, 940)


class EnemyPlayer(Car):
    x_position = 700
    y_position = 920
    car_angle = 270
    car_image = purple_formula.convert_alpha()

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def respawn(self):
        self.x = self.x_position
        self.y = self.y_position

        self.car_angle = 270

    def second_map_respawn(self):
        self.x = 1050
        self.y = 840
        self.car_angle = 270

    def out_of_track(self):
        self.car_speed = 0
        self.car_speed = self.car_speed - 5.6

        self.movement()

    def car_collide(self):
        self.max_speed = 0.1
        # self.car_image = pink_lambo

        self.movement()

    def border_collide(self, car_hitbox):
        image_hitbox = pygame.mask.from_surface(self.car_image)
        car_position = self.x, self.y
        out_of_track = car_hitbox.overlap(image_hitbox, car_position)

        return out_of_track

    def first_map_car(self):
        self.car_image = purple_formula

    def second_map_car(self):
        self.car_image = pink_lambo

    def out_of_map(self):
        if self.x >= width or self.x <= 0:
            self.respawn()
        if self.y >= height or self.y <= 0:
            self.respawn()


def key_binds(car, car_rect, enemy_rect, map_border):
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_w]:
        car.forward_control()
    else:
        car.forward_slowdown()

    if pressed_key[pygame.K_s]:
        car.backward_control()
    else:
        car.forward_slowdown()

    if pressed_key[pygame.K_d]:
        car.rotate_right()

    if pressed_key[pygame.K_a]:
        car.rotate_left()

    if pressed_key[pygame.K_q]:
        car.drift()
    else:
        car.movement_speed = 2.5

    if pressed_key[pygame.K_x]:
        mode_selection()

    if pressed_key[pygame.K_w]:
        if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(map_border)) \
                and not car_rect.colliderect(enemy_rect):
            car.nitro()


def get_car_rect(car_image, car_angle, car_x, car_y):
    rect_angle = pygame.transform.rotate(car_image, car_angle)
    car_rect = rect_angle.get_rect(topleft=(car_x, car_y), center=(car_x + 10.5, car_y + 28))

    return car_rect


def get_enemy_rect(enemy_car_image, enemy_car_angle, enemy_car_x, enemy_car_y):
    enemy_rect_angle = pygame.transform.rotate(enemy_car_image, enemy_car_angle)
    enemy_rect = enemy_rect_angle.get_rect(topleft=(enemy_car_x, enemy_car_y), center=(enemy_car_x + 10.5, enemy_car_y
                                                                                       + 28))
    return enemy_rect


def get_enemy_center_rect(enemy_car_image, enemy_car_angle, enemy_car_x, enemy_car_y):
    enemy_rect_angle = pygame.transform.rotate(enemy_car_image, enemy_car_angle)
    enemy_rect = enemy_rect_angle.get_rect(center=(enemy_car_x, enemy_car_y))

    return enemy_rect


def game_info(match_time, clock, lap, stopwatch):
    draw_text("W - Forward", small_font, "white", 70, 40)
    draw_text("S - Backward", small_font, "white", 70, 70)
    draw_text("A - Left", small_font, "white", 70, 100)
    draw_text("D - Right", small_font, "white", 70, 130)
    draw_text("X - Exit", small_font, "white", 190, 40)
    draw_text("E - Nitro", small_font, "white", 190, 70)
    draw_text("Q - Drift", small_font, "white", 190, 100)
    draw_text(f"LAP TIME - {stopwatch}", small_font, "white", 1670, 900)
    draw_text(f"MATCH TIME - {match_time}", small_font, "white", 1670, 850)
    draw_text(f"FPS - {round(clock.get_fps())}", small_font, "white", 1780, 40)
    draw_text(f"LAP - {lap} / 3", small_font, "white", 1690, 800)


def player_time_table(fastest_time, slowest_time, match_time):
    game_screen.blit(time_menu, (650, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", font, "white", 740, 250)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", font, "white", 740, 350)
    draw_text(f"MATCH TIME : {round(match_time)}", font, "white", 740, 450)


def enemy_time_table(fastest_time, slowest_time, match_time):
    game_screen.blit(time_menu, (1050, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", font, "white", 1150, 250)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", font, "white", 1150, 350)
    draw_text(f"MATCH TIME : {round(match_time)}", font, "white", 1150, 450)


def check_colision(car, enemy_car, car_rect, enemy_rect, finish_line_rect, map_border):
    if car_rect.colliderect(enemy_rect):
        car.car_collide()
        # pygame.draw.rect(game_screen, (255, 0, 0), enemy_rect)
        # pygame.draw.rect(game_screen, (255, 0, 0), car_rect)
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()

    car.out_of_map()


def check_new_game():
    global started
    global start_time

    started = False

    while not started:
        game_screen.blit(time_menu, (700, 200))
        draw_text("PLAY AGAIN - SPACE", font, "white", 740, 250)
        draw_text("EXIT TO MENU - X", font, "white", 740, 350)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                started = True
                start_time = pygame.time.get_ticks()


def check_car_type(car):
    if car_type == 1:
        car.first_map_car()
    if car_type == 2:
        car.second_map_car()


def start_game():
    global started
    global start_time

    while not started:
        draw_text("PRESS SPACE TO PLAY", font, "white", 750, 620)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                started = True
                start_time = pygame.time.get_ticks()


def start_countdown(car, enemy_car):
    global countdown
    global last_count

    if countdown > 0:
        draw_text(str(countdown), font, "white", 900, 500)
        count_timer = pygame.time.get_ticks()
        car.max_speed = 0
        car.car_nitro = 0

        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer

    if countdown == 3:
        draw_text(f"{str(countdown)} - READY", font, "white", 900, 500)

    if countdown == 2:
        draw_text(f"{str(countdown)} - STEADY", font, "white", 900, 500)

    if countdown == 1:
        draw_text(f"{str(countdown)} - GO!", font, "white", 900, 500)

    if countdown == 0:
        draw_text(f"", font, "white", 900, 500)
        car.max_speed = car.max_speed
        car.car_nitro = 5


def game_first_map(lap=0, match_time=0, enemy_match_time=0, enemy_lap=0):
    global car_type
    global race_rounds
    global started
    global countdown
    global last_count
    global start_time

    race_rounds = 3
    start_time = 0

    car_time_list = []
    enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (580, 849))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)

            car.car_info()

            enemy_car.first_map_car()
            check_car_type(car)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            finish_line_rect = finish_line.get_rect(topleft=(580, 849))

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            key_binds(car, car_rect, enemy_rect, first_map_border)

            check_colision(car, enemy_car, car_rect, enemy_rect, finish_line_rect, first_map_border)

            if 650 < car.x < 680:
                if 860 < car.y < 1080:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map()

                    if lap == race_rounds:
                        car_time_list.sort()
                        enemy_time_list.sort()
                        player_time_table(car_time_list[0], car_time_list[2], match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0

                        pygame.display.update()
                        match_time = 0

                        car.respawn()

                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map()

            pygame.display.update()


def game_first_map_solo(lap=0, match_time=0):
    global car_type
    global race_rounds
    global started
    global countdown
    global last_count
    global start_time

    race_rounds = 3
    start_time = 0

    car_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (580, 849))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)

            car.car_info()

            enemy_car.first_map_car()
            check_car_type(car)

            car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            finish_line_rect = finish_line.get_rect(topleft=(580, 849))

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            key_binds(car, car_rect, enemy_rect, first_map_border)

            check_colision(car, enemy_car, car_rect, enemy_rect, finish_line_rect, first_map_border)

            if 650 < car.x < 680:
                if 860 < car.y < 1080:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0

                        car.respawn()

                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map_solo()

                    if lap == race_rounds:
                        car_time_list.sort()

                        player_time_table(car_time_list[0], car_time_list[2], match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn()

                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map_solo()

            pygame.display.update()


def game_second_map(lap=0, match_time=0):
    global car_type
    global race_rounds
    global started
    global countdown
    global last_count
    global start_time

    race_rounds = 3
    start_time = 0

    car_time_list = []
    enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (580, 795))
            game_screen.blit(second_map_border, (0, 0))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)

            car.car_info()

            enemy_car.second_map_car()
            check_car_type(car)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            finish_line_rect = finish_line.get_rect(topleft=(580, 795))

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            key_binds(car, car_rect, enemy_rect, second_map_border)

            check_colision(car, enemy_car, car_rect, enemy_rect, finish_line_rect, second_map_border)

            if 650 < car.x < 680:
                if 860 < car.y < 1080:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0

                        car.respawn()

                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_second_map()

                    if lap == race_rounds:
                        car_time_list.sort()
                        enemy_time_list.sort()
                        player_time_table(car_time_list[0], car_time_list[2], match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0

                        pygame.display.update()
                        match_time = 0

                        car.respawn()

                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_second_map()

            pygame.display.update()


def game_second_map_solo(lap=0, match_time=0):
    global car_type
    global race_rounds
    global started
    global countdown
    global last_count
    global start_time

    race_rounds = 3
    start_time = 0

    car_time_list = []
    enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (580, 795))
            game_screen.blit(second_map_border, (0, 0))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)

            car.car_info()

            check_car_type(car)

            car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            finish_line_rect = finish_line.get_rect(topleft=(580, 795))

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            key_binds(car, car_rect, enemy_rect, second_map_border)

            check_colision(car, enemy_car, car_rect, enemy_rect, finish_line_rect, second_map_border)

            if 650 < car.x < 680:
                if 860 < car.y < 1080:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_second_map_solo()

                    if lap == race_rounds:
                        car_time_list.sort()

                        player_time_table(car_time_list[0], car_time_list[2], match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn()

                        start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_second_map_solo()

            pygame.display.update()


def mode_selection():
    pygame.display.set_caption("2D Racing Game - Mode Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        menu_font = second_font.render("Mode Selection", True, "white").convert_alpha()
        menu_hitbox = menu_font.get_rect(center=(960, 100))

        solo = Button(button_image=button_image, x_y=(960, 350),
                      button_text="Solo", font=font, font_color="white")

        you_vs_pc = Button(button_image=button_image, x_y=(960, 500),
                           button_text="Versus PC", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(960, 650),
                             button_text="Back", font=font, font_color="white")

        game_screen.blit(menu_font, menu_hitbox)

        solo.button_render(game_screen)
        you_vs_pc.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo.on_click(mouse_coordinates):
                    solo_map_selection()

                if you_vs_pc.on_click(mouse_coordinates):
                    vs_map_selection()

                if back_button.on_click(mouse_coordinates):
                    menu()

            pygame.display.update()


def solo_map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        menu_font = second_font.render("Map Selection", True, "white").convert_alpha()
        menu_hitbox = menu_font.get_rect(center=(960, 100))

        first_map_button = Button(button_image=button_image, x_y=(960, 350),
                                  button_text="First Map", font=font, font_color="white")

        second_map_button = Button(button_image=button_image, x_y=(960, 500),
                                   button_text="Second Map", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(960, 650),
                             button_text="Back", font=font, font_color="white")

        game_screen.blit(menu_font, menu_hitbox)

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map_solo()

                if second_map_button.on_click(mouse_coordinates):
                    game_second_map_solo()

                if back_button.on_click(mouse_coordinates):
                    menu()

            pygame.display.update()


def vs_map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        menu_font = second_font.render("Map Selection", True, "white").convert_alpha()
        menu_hitbox = menu_font.get_rect(center=(960, 100))

        first_map_button = Button(button_image=button_image, x_y=(960, 350),
                                  button_text="First Map", font=font, font_color="white")

        second_map_button = Button(button_image=button_image, x_y=(960, 500),
                                   button_text="Second Map", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(960, 650),
                             button_text="Back", font=font, font_color="white")

        game_screen.blit(menu_font, menu_hitbox)

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map()

                if second_map_button.on_click(mouse_coordinates):
                    game_second_map()

                if back_button.on_click(mouse_coordinates):
                    menu()

            pygame.display.update()


def car_selection():
    global car_type

    pygame.display.set_caption("2D Racing Game - Car Selection")

    while True:
        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("Car Selection", second_font, "white", 720, 100)
        draw_text("Formula", small_font, "white", 770, 330)
        draw_text("Lamborghini", small_font, "white", 1150, 330)

        formula_button = Button(x_y=(800, 550), button_image=formula_selection, button_text="", font=small_font,
                                font_color="white")
        lambo_button = Button(x_y=(1200, 550), button_image=lambo_selection, button_text="", font=small_font,
                              font_color="white")

        back_button = Button(button_image=button_image, x_y=(1000, 900),
                             button_text="Back", font=font, font_color="white")

        formula_button.button_render(game_screen)
        lambo_button.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if formula_button.on_click(mouse_coordinates):
                    car_type = 0
                    car_type = 1
                    draw_text("Car Choosen!", font, "white", 830, 230)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if lambo_button.on_click(mouse_coordinates):
                    car_type = 0
                    car_type = 2
                    draw_text("Car Choosen!", font, "white", 830, 230)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if back_button.on_click(mouse_coordinates):
                    menu()

            pygame.display.update()


def menu():
    global car_type
    car_type = 1
    pygame.display.set_caption("2D Racing Game - Menu")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        # menu_font = second_font.render("Main Menu", True, "white").convert_alpha()
        # menu_hitbox = menu_font.get_rect(center=(960, 100))
        draw_text("Main Menu", second_font, "white", 750, 100)

        play_button = Button(button_image=button_image, x_y=(960, 350), button_text="Play", font=font,
                             font_color="white")

        car_selection_button = Button(button_image=button_image, x_y=(960, 500), button_text="Choose Car", font=font,
                                      font_color="white")

        quit_button = Button(button_image=button_image, x_y=(960, 650), button_text="Quit", font=font,
                             font_color="white")

        # game_screen.blit(menu_font, menu_hitbox)

        play_button.button_render(game_screen)
        car_selection_button.button_render(game_screen)
        quit_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.on_click(mouse_coordinates):
                    mode_selection()

                if car_selection_button.on_click(mouse_coordinates):
                    car_selection()

                if quit_button.on_click(mouse_coordinates):
                    pygame.quit()

        pygame.display.update()


if __name__ == '__main__':
    menu()
