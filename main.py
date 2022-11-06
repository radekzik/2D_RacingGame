import pygame
import math
import time

from button import Button
from resolution import res, image_position

pygame.init()

width = 1792
height = 1008
game_screen = pygame.display.set_mode((width, height))

first_map = res(pygame.image.load("images/first_map_v4.png"), 0.7).convert_alpha()

first_map_border = res(pygame.image.load("images/first_map_border_v2.png"), 0.7).convert_alpha()

second_map = res(pygame.image.load("images/first_map_v2.png"), 0.7).convert_alpha()

second_map_border = res(pygame.image.load("images/first_map_border_v2.png"), 0.7).convert_alpha()

blue_formula = res(pygame.image.load("images/pixel_formula_blue_new.png"), 1.05).convert_alpha()

red_formula = res(pygame.image.load("images/pixel_formula_red_new.png"), 1.05).convert_alpha()

purple_formula = res(pygame.image.load("images/pixel_formula_purple_new.png"), 1.05).convert_alpha()

blue_lambo = res(pygame.image.load("images/blue_lambo_new.png"), 0.85).convert_alpha()

pink_lambo = res(pygame.image.load("images/pink_lambo_new.png"), 0.85).convert_alpha()

menu_background = res(pygame.image.load("images/blue_background.jpg"), 1).convert_alpha()

finish_line = res(pygame.image.load("images/finish_line.png"), 1.04).convert_alpha()

button_image = res(pygame.image.load("images/button.png"), 1).convert_alpha()

font = pygame.font.SysFont("impact", 60)
small_font = pygame.font.SysFont("impact", 20)
second_font = pygame.font.SysFont("impact", 100)


class Car:

    def __init__(self):
        self.car_image = self.car_image
        self.x = self.x_position
        self.y = self.y_position
        self.car_speed = 0
        self.car_acceleration = 0.3
        self.max_speed = 3
        self.min_speed = -1
        self.movement_speed = 3.2
        self.max_movement_speed = 6
        self.car_angle = self.car_angle
        self.car_nitro = 5
        self.car_width = 21
        self.car_height = 56

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
    car_image = blue_formula.convert_alpha()
    x_position = 665
    y_position = 872
    car_angle = 270

    def first_map_car(self):
        self.car_image = blue_formula.convert_alpha()

    def second_map_car(self):
        self.car_image = blue_lambo.convert_alpha()

    def respawn(self):
        self.x = self.x_position
        self.y = self.y_position
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
        # self.car_image = pink_lambo.convert_alpha()

        self.movement()

    def border_collide(self, car_hitbox):
        image_hitbox = pygame.mask.from_surface(self.car_image)
        car_position = self.x, self.y
        out_of_track = car_hitbox.overlap(image_hitbox, car_position)

        return out_of_track

    def game_info(self):
        text_y = small_font.render(f"Y - ( {round(self.y)} )", True, "white").convert_alpha()
        text_y_hitbox = text_y.get_rect(topleft=(1680, 970))

        text_x = small_font.render(f"X - ( {round(self.x)} )", True, "white").convert_alpha()
        text_x_hitbox = text_x.get_rect(topleft=(1680, 940))

        text_movement = small_font.render(f"MOVEMENT - ( {round(self.movement_speed)} )", True, "white").convert_alpha()
        text_movement_hitbox = text_movement.get_rect(topleft=(1530, 970))

        text_speed = small_font.render(f"SPEED - ( {round(self.car_speed)} )", True, "white").convert_alpha()
        text_speed_hitbox = text_speed.get_rect(topleft=(1560, 940))

        game_screen.blit(text_x, text_x_hitbox)
        game_screen.blit(text_y, text_y_hitbox)
        game_screen.blit(text_movement, text_movement_hitbox)
        game_screen.blit(text_speed, text_speed_hitbox)


class EnemyPlayer(Car):
    car_image = purple_formula.convert_alpha()
    x_position = 665
    y_position = 840
    car_angle = 270

    def first_map_car(self):
        self.car_image = purple_formula.convert_alpha()

    def second_map_car(self):
        self.car_image = pink_lambo.convert_alpha()

    def move(self):
        self.forward_control()

    def respawn(self):
        self.x = self.x_position
        self.y = self.y_position
        self.car_angle = 270

    def out_of_map(self):
        if self.x >= width or self.x <= 0:
            self.respawn()
        if self.y >= height or self.y <= 0:
            self.respawn()


def keys(car):
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
        car.movement_speed = 3.2

    if pressed_key[pygame.K_x]:
        menu()


def get_car_rect(car_image, car_angle, car_x, car_y):
    rect_angle = pygame.transform.rotate(car_image, car_angle)
    car_rect = rect_angle.get_rect(topleft=(car_x, car_y), center=(car_x + 10.5, car_y + 28))
    return car_rect


def get_enemy_rect(enemy_car_image, enemy_car_angle, enemy_car_x, enemy_car_y):
    enemy_rect_angle = pygame.transform.rotate(enemy_car_image, enemy_car_angle)
    enemy_rect = enemy_rect_angle.get_rect(topleft=(enemy_car_x, enemy_car_y),
                                           center=(enemy_car_x + 10.5, enemy_car_y + 28))

    return enemy_rect


def get_finish_line_rect(car_image, car_angle, car_x, car_y):
    rect_angle = pygame.transform.rotate(car_image, car_angle)
    car_rect = rect_angle.get_rect(topleft=(car_x, car_y), center=(car_x + 10.5, car_y + 28))
    return car_rect


def game_keybind():
    text_forward = small_font.render("W - Forward", True, "white").convert_alpha()
    text_forward_hitbox = text_forward.get_rect(topleft=(100, 40))

    text_backward = small_font.render("S - Backward", True, "white").convert_alpha()
    text_backward_hitbox = text_backward.get_rect(topleft=(100, 70))

    text_left = small_font.render("A - Left", True, "white").convert_alpha()
    text_left_hitbox = text_backward.get_rect(topleft=(100, 100))

    text_right = small_font.render("D - Right", True, "white").convert_alpha()
    text_right_hitbox = text_right.get_rect(topleft=(100, 130))

    text_exit = small_font.render("X - Exit", True, "white").convert_alpha()
    text_exit_hitbox = text_exit.get_rect(topleft=(220, 40))

    text_nitro = small_font.render("E - Nitro", True, "white").convert_alpha()
    text_nitro_hitbox = text_nitro.get_rect(topleft=(220, 70))

    text_drift = small_font.render("Q - Drift", True, "white").convert_alpha()
    text_drift_hitbox = text_drift.get_rect(topleft=(220, 100))

    game_screen.blit(text_exit, text_exit_hitbox)
    game_screen.blit(text_nitro, text_nitro_hitbox)
    game_screen.blit(text_drift, text_drift_hitbox)
    game_screen.blit(text_forward, text_forward_hitbox)
    game_screen.blit(text_backward, text_backward_hitbox)
    game_screen.blit(text_left, text_left_hitbox)
    game_screen.blit(text_right, text_right_hitbox)


def game_first_map(lap=0, start_time=pygame.time.get_ticks(), match_time=0):
    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap")

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10
            text_time = small_font.render(f"LAP TIME - {stopwatch}", True, "white").convert_alpha()
            text_timer = text_time.get_rect(topleft=(1620, 900))

            textt_time = small_font.render(f"RACE TIME - {match_time}", True, "white").convert_alpha()
            textt_timer = textt_time.get_rect(topleft=(1620, 850))

            text_fps = small_font.render(f"FPS - {round(clock.get_fps())}", True, "white").convert_alpha()
            text_fps_hitbox = text_fps.get_rect(topleft=(1690, 40))

            current_lap = small_font.render(f"LAP - {lap} / 3", True, "white").convert_alpha()
            current_lap_hitbox = current_lap.get_rect(topleft=(1560, 500))

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (550, 792))

            game_keybind()
            car.game_info()

            car.first_map_car()
            enemy_car.first_map_car()

            enemy_car.move()

            game_screen.blit(text_time, text_timer)
            game_screen.blit(text_fps, text_fps_hitbox)
            game_screen.blit(current_lap, current_lap_hitbox)
            game_screen.blit(textt_time, textt_timer)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            pressed_key = pygame.key.get_pressed()

            keys(car)

            car_rect = get_finish_line_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle,
                                        enemy_car.x, enemy_car.y)

            if car_rect.colliderect(enemy_rect):
                car.car_collide()
                pygame.draw.rect(game_screen, (255, 0, 0), enemy_rect)
                pygame.draw.rect(game_screen, (255, 0, 0), car_rect)
            else:
                car.car_image = car.car_image
                car.max_speed = 3

            if car.border_collide(pygame.mask.from_surface(first_map_border)):
                car.out_of_track()

            if pressed_key[pygame.K_w]:
                if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(first_map_border)) \
                        and not car_rect.colliderect(enemy_rect):
                    car.nitro()

            car.out_of_map()
            enemy_car.out_of_map()

            if 640 < car.x < 660:
                if 650 < car.y < 950:

                    if stopwatch > 5:

                        lap += 1
                        round_time = font.render(f"Lap Time - {stopwatch}", True, "white").convert_alpha()
                        round_time_hitbox = round_time.get_rect(topleft=(800, 450))

                        match_time = match_time + stopwatch

                        game_screen.blit(round_time, round_time_hitbox)
                        pygame.display.update()
                        pygame.time.wait(100)

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    else:
                        round_time = font.render(f"Wrong Way", True, "white").convert_alpha()
                        round_time_hitbox = round_time.get_rect(topleft=(800, 450))

                        game_screen.blit(round_time, round_time_hitbox)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        lap = 0
                        match_time = 0
                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    if lap == 3:
                        round_time = font.render(f"Match Time - {match_time}", True, "white").convert_alpha()
                        round_time_hitbox = round_time.get_rect(topleft=(800, 350))

                        game_screen.blit(round_time, round_time_hitbox)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        lap = 0
                        match_time = 0
                        car.respawn()
                        start_time = pygame.time.get_ticks()

            pygame.display.update()


def game_second_map(lap=0, match_time=0):
    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap")

    while True:

        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()

        car = Player()
        enemy_car = EnemyPlayer()

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10
            text_time = small_font.render(f"LAP TIME - {stopwatch}", True, "white").convert_alpha()
            text_timer = text_time.get_rect(topleft=(1620, 900))

            textt_time = small_font.render(f"RACE TIME - {match_time}", True, "white").convert_alpha()
            textt_timer = textt_time.get_rect(topleft=(1620, 850))

            text_fps = small_font.render(f"FPS - {round(clock.get_fps())}", True, "white").convert_alpha()
            text_fps_hitbox = text_fps.get_rect(topleft=(1690, 40))

            current_lap = small_font.render(f"LAP - {lap} / 3", True, "white").convert_alpha()
            current_lap_hitbox = current_lap.get_rect(topleft=(1560, 500))

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (550, 792))

            game_keybind()
            car.game_info()

            car.second_map_car()
            enemy_car.second_map_car()

            game_screen.blit(text_time, text_timer)
            game_screen.blit(text_fps, text_fps_hitbox)
            game_screen.blit(current_lap, current_lap_hitbox)
            game_screen.blit(textt_time, textt_timer)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

            pressed_key = pygame.key.get_pressed()

            keys(car)

            car_rect = get_finish_line_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle,
                                        enemy_car.x_position, enemy_car.y_position)

            if car_rect.colliderect(enemy_rect):
                car.car_collide()
                pygame.draw.rect(game_screen, (255, 0, 0), enemy_rect)
                pygame.draw.rect(game_screen, (255, 0, 0), car_rect)
            else:
                car.car_image = blue_formula.convert_alpha()
                car.max_speed = 3

            if car.border_collide(pygame.mask.from_surface(second_map_border)):
                border_alert = font.render(f"You Went Off The Track", True, "white").convert_alpha()
                border_alert_hitbox = border_alert.get_rect(topleft=(700, 450))
                game_screen.blit(border_alert, border_alert_hitbox)

                lap = 0
                pygame.display.update()
                pygame.time.wait(1000)

                car.respawn()
                start_time = pygame.time.get_ticks()

            if pressed_key[pygame.K_w]:
                if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(second_map_border)) \
                        and not car_rect.colliderect(enemy_rect):
                    car.nitro()

            if 640 < car.x < 660:
                if 650 < car.y < 950:

                    if stopwatch > 5:

                        lap += 1
                        round_time = font.render(f"Lap Time - {stopwatch}", True, "white").convert_alpha()
                        round_time_hitbox = round_time.get_rect(topleft=(800, 450))

                        match_time = match_time + stopwatch

                        game_screen.blit(round_time, round_time_hitbox)
                        pygame.display.update()
                        pygame.time.wait(100)

                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    else:
                        round_time = font.render(f"Wrong Way", True, "white").convert_alpha()
                        round_time_hitbox = round_time.get_rect(topleft=(800, 450))

                        game_screen.blit(round_time, round_time_hitbox)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        lap = 0
                        match_time = 0
                        car.respawn()
                        start_time = pygame.time.get_ticks()

                    if lap == 3:
                        round_time = font.render(f"Match Time - {match_time}", True, "white").convert_alpha()
                        round_time_hitbox = round_time.get_rect(topleft=(800, 350))

                        game_screen.blit(round_time, round_time_hitbox)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        lap = 0
                        match_time = 0
                        car.respawn()
                        start_time = pygame.time.get_ticks()

            pygame.display.update()


def map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        menu_font = second_font.render("Map Selection", True, "white").convert_alpha()
        menu_hitbox = menu_font.get_rect(center=(890, 100))

        first_map_button = Button(button_image=button_image, x_y=(890, 300),
                                  button_text="First Map", font=font, font_color="white")

        second_map_button = Button(button_image=button_image, x_y=(890, 450),
                                   button_text="Second Map", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(890, 600),
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


def menu():
    pygame.display.set_caption("2D Racing Game - Menu")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        menu_font = second_font.render("Main Menu", True, "white").convert_alpha()
        menu_hitbox = menu_font.get_rect(center=(890, 100))

        play_button = Button(button_image=button_image, x_y=(890, 300), button_text="PLAY", font=font,
                             font_color="white")

        quit_button = Button(button_image=button_image, x_y=(890, 450), button_text="QUIT", font=font,
                             font_color="white")

        game_screen.blit(menu_font, menu_hitbox)

        play_button.button_render(game_screen)
        quit_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.on_click(mouse_coordinates):
                    map_selection()

                if quit_button.on_click(mouse_coordinates):
                    pygame.quit()

            pygame.display.update()


menu()
