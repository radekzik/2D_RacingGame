import pygame
import math

pygame.init()


def res(image, amount):
    new_res = (image.get_width() * amount), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


width = 1792
height = 1008
game_screen = pygame.display.set_mode((width, height))

first_map = res(pygame.image.load("images/first_map_v2_green.png"), 0.7).convert_alpha()

first_map_border = res(pygame.image.load("images/first_map_border_v2.png"), 0.7).convert_alpha()

second_map = res(pygame.image.load("images/first_map_v2.png"), 0.7).convert_alpha()

second_map_border = res(pygame.image.load("images/first_map_border_v2.png"), 0.7).convert_alpha()

blue_formula = res(pygame.image.load("images/pixel_formula_blue.png"), 1.05).convert_alpha()

red_formula = res(pygame.image.load("images/pixel_formula_red.png"), 1.05).convert_alpha()

purple_formula = res(pygame.image.load("images/pixel_formula_purple.png"), 1.05).convert_alpha()

menu_background = res(pygame.image.load("images/blue_background.jpg"), 1).convert_alpha()

font = pygame.font.SysFont("impact", 60)
small_font = pygame.font.SysFont("impact", 20)
second_font = pygame.font.SysFont("impact", 100)


def image_position(game_window, car_image, car_left_corner, car_angle):
    angle_position = pygame.transform.rotate(car_image, car_angle)

    car_hitbox = angle_position.get_rect(center=car_image.get_rect(topleft=car_left_corner).center)

    game_window.blit(angle_position, car_hitbox.topleft)


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
    car_image = blue_formula
    x_position = 630
    y_position = 850
    car_angle = 270

    def respawn(self):
        self.x = self.x_position
        self.y = self.y_position
        self.car_angle = 270

    def border_collide(self, map_hitbox):
        image_hitbox = pygame.mask.from_surface(self.car_image)
        car_position = self.x, self.y
        out_of_track = map_hitbox.overlap(image_hitbox, car_position)

        return out_of_track

    def game_info(self):
        text_y = small_font.render(f"Y - ( {round(self.y)} )", True, "white")
        text_y_hitbox = text_y.get_rect(topleft=(1680, 970))

        text_x = small_font.render(f"X - ( {round(self.x)} )", True, "white")
        text_x_hitbox = text_x.get_rect(topleft=(1680, 940))

        text_movement = small_font.render(f"MOVEMENT - ( {round(self.movement_speed)} )", True, "white")
        text_movement_hitbox = text_movement.get_rect(topleft=(1530, 970))

        text_speed = small_font.render(f"SPEED - ( {round(self.car_speed)} )", True, "white")
        text_speed_hitbox = text_speed.get_rect(topleft=(1560, 940))

        game_screen.blit(text_x, text_x_hitbox)
        game_screen.blit(text_y, text_y_hitbox)
        game_screen.blit(text_movement, text_movement_hitbox)
        game_screen.blit(text_speed, text_speed_hitbox)


class EnemyPlayer(Car):
    car_image = purple_formula
    x_position = 100
    y_position = 520
    car_angle = 0


def game_keybind():
    text_forward = small_font.render("W - Forward", True, "white")
    text_forward_hitbox = text_forward.get_rect(topleft=(100, 40))

    text_backward = small_font.render("S - Backward", True, "white")
    text_backward_hitbox = text_backward.get_rect(topleft=(100, 70))

    text_left = small_font.render("A - Left", True, "white")
    text_left_hitbox = text_backward.get_rect(topleft=(100, 100))

    text_right = small_font.render("D - Right", True, "white")
    text_right_hitbox = text_right.get_rect(topleft=(100, 130))

    text_exit = small_font.render("X - Exit", True, "white")
    text_exit_hitbox = text_exit.get_rect(topleft=(220, 40))

    text_nitro = small_font.render("E - Nitro", True, "white")
    text_nitro_hitbox = text_nitro.get_rect(topleft=(220, 70))

    text_drift = small_font.render("Q - Drift", True, "white")
    text_drift_hitbox = text_drift.get_rect(topleft=(220, 100))

    game_screen.blit(text_exit, text_exit_hitbox)
    game_screen.blit(text_nitro, text_nitro_hitbox)
    game_screen.blit(text_drift, text_drift_hitbox)
    game_screen.blit(text_forward, text_forward_hitbox)
    game_screen.blit(text_backward, text_backward_hitbox)
    game_screen.blit(text_left, text_left_hitbox)
    game_screen.blit(text_right, text_right_hitbox)


def game_first_map():
    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap")

    while True:

        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()

        car = Player()
        enemy_car = EnemyPlayer()

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - start_time
            stopwatch = stopwatch // 100 / 10
            text_time = small_font.render(f"TIMER - {stopwatch}", True, "white")
            text_timer = text_time.get_rect(topleft=(1620, 900))

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))

            game_keybind()
            car.game_info()
            game_screen.blit(text_time, text_timer)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

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

            if car.border_collide(pygame.mask.from_surface(first_map_border)):
                car.respawn()
                start_time = pygame.time.get_ticks()

            if pressed_key[pygame.K_w]:
                if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(first_map_border)):
                    car.nitro()

            if pressed_key[pygame.K_q]:
                car.drift()
            else:
                car.movement_speed = 3.2

            if pressed_key[pygame.K_x]:
                menu()

            pygame.display.update()


def game_second_map():
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
            text_time = small_font.render(f"TIMER - {stopwatch}", True, "white")
            text_timer = text_time.get_rect(topleft=(1620, 900))

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))

            game_keybind()
            car.game_info()
            game_screen.blit(text_time, text_timer)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

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

            if car.border_collide(pygame.mask.from_surface(second_map_border)):
                car.respawn()
                start_time = pygame.time.get_ticks()

            if pressed_key[pygame.K_w]:
                if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(second_map_border)):
                    car.nitro()

            if pressed_key[pygame.K_q]:
                car.drift()
            else:
                car.movement_speed = 3.2

            if pressed_key[pygame.K_x]:
                menu()

            pygame.display.update()


def menu():
    pygame.display.set_caption("2D Racing Game - Menu")

    while True:

        game_screen.blit(menu_background, (0, 0))

        menu_font = font.render("Main Menu", True, "white")
        menu_hitbox = menu_font.get_rect(center=(890, 100))

        text = second_font.render("Press SPACE to play - First Map", True, "white")
        text_hitbox = text.get_rect(center=(890, 400))

        second_text = second_font.render("Press R_ALT to play - Second Map", True, "white")
        second_text_hitbox = text.get_rect(center=(890, 650))

        game_screen.blit(menu_font, menu_hitbox)
        game_screen.blit(text, text_hitbox)
        game_screen.blit(second_text, second_text_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_SPACE]:
                game_first_map()

            if pressed_key[pygame.K_RALT]:
                game_second_map()

            pygame.display.update()


menu()
