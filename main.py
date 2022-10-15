import pygame
import math

pygame.init()


def res(image, amount):
    new_res = (image.get_width() * amount), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


width = 1792
height = 1008
game_screen = pygame.display.set_mode((width, height))

first_map = res(pygame.image.load("images/first_map.png"), 0.7).convert_alpha()

blue_formula = res(pygame.image.load("images/pixel_formula_blue.png"), 1.2).convert_alpha()

red_formula = res(pygame.image.load("images/pixel_formula_red.png"), 1.7).convert_alpha()

purple_formula = res(pygame.image.load("images/pixel_formula_purple.png"), 2).convert_alpha()

menu_background = res(pygame.image.load("images/blue_backscreen.jpg"), 1).convert_alpha()

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
        self.max_speed = 2.5
        self.min_speed = -1
        self.movement_speed = 1.8
        self.max_movement_speed = 3
        self.car_angle = self.car_angle
        self.car_nitro = 0.5

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

    def slowdown(self):

        self.car_speed = self.car_speed - self.car_acceleration / 3

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
    x_position = 480
    y_position = 700
    car_angle = 270


class EnemyPlayer(Car):
    car_image = purple_formula
    x_position = 100
    y_position = 520
    car_angle = 0


def game():
    game_loop = True

    pygame.display.set_caption("2D Racing Game - InGame")

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        while game_loop:

            clock.tick(240)

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))

            text_exit = small_font.render("X - Exit", True, "white")
            text_exit_hitbox = text_exit.get_rect(center=(120, 40))

            text_nitro = small_font.render("E - Nitro", True, "white")
            text_nitro_hitbox = text_nitro.get_rect(center=(120, 70))

            text_drift = small_font.render("Q - Drift", True, "white")
            text_drift_hitbox = text_drift.get_rect(center=(120, 100))

            game_screen.blit(text_exit, text_exit_hitbox)
            game_screen.blit(text_nitro, text_nitro_hitbox)
            game_screen.blit(text_drift, text_drift_hitbox)

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
                car.slowdown()

            if pressed_key[pygame.K_s]:
                car.backward_control()
            else:
                car.slowdown()

            if pressed_key[pygame.K_d]:
                car.rotate_right()

            if pressed_key[pygame.K_a]:
                car.rotate_left()

            if pressed_key[pygame.K_e]:
                car.nitro()

            if pressed_key[pygame.K_q]:
                car.drift()
            else:
                car.movement_speed = 1.8

            if pressed_key[pygame.K_x]:
                menu()

            pygame.display.update()


def menu():
    pygame.display.set_caption("2D Racing Game - Menu")

    while True:

        game_screen.blit(menu_background, (0, 0))

        menu_font = font.render("Main Menu", True, "white")
        menu_hitbox = menu_font.get_rect(center=(890, 100))

        text = second_font.render("Press SPACE to play", True, "white")
        text_hitbox = text.get_rect(center=(890, 400))

        game_screen.blit(menu_font, menu_hitbox)
        game_screen.blit(text, text_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_SPACE]:
                game()

            pygame.display.update()


menu()
