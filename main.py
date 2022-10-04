import pygame
import math

pygame.init()


def res(image, amount):
    new_res = (image.get_width() * amount), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


game_screen = pygame.display.set_mode((1300, 900))

first_map = res(pygame.image.load("imgs/FirstTrack.png"), 0.75)

blue_formula = res(pygame.image.load("imgs/pixel_formula_blue.png"), 2)

transparent_formula = res(pygame.image.load("imgs/pixel_formula.png"), 2)

menu_background = res(pygame.image.load("imgs/blue_backscreen.jpg"), 1)

font = pygame.font.SysFont("impact", 60)


def image_angle_rotating(game_window, car_image, car_left_corner, car_angle):
    image_rotating = pygame.transform.rotate(car_image, car_angle)

    hitbox_rotating = image_rotating.get_rect(center=car_image.get_rect(topleft=car_left_corner).center)

    game_window.blit(image_rotating, hitbox_rotating.topleft)


class Car:

    def __init__(self):
        self.car_image = self.car_image
        self.x = self.x_position
        self.y = self.y_position
        self.car_speed = 0
        self.car_acceleration = 0.25
        self.max_speed = 3
        self.min_speed = -1
        self.speed_rotation = 2
        self.car_angle = self.car_angle

    def rotate_left(self):
        self.car_angle += self.speed_rotation

    def rotate_right(self):
        self.car_angle -= self.speed_rotation

    def render_position(self, game_window):
        image_angle_rotating(game_window, self.car_image, (self.x, self.y), self.car_angle)

    def forward_control(self):
        while self.car_speed <= self.max_speed:
            self.car_speed = self.car_speed + self.car_acceleration

        else:
            self.car_speed = self.max_speed

        self.x += self.car_speed

    def backward_control(self):

        while self.car_speed <= self.min_speed:
            self.car_speed = -self.car_acceleration

        else:
            self.car_speed = self.min_speed

        self.x += self.car_speed


class Player(Car):
    car_image = blue_formula
    x_position = 180
    y_position = 200
    car_angle = 270
    car_rotation = 2


class EnemyPlayer(Car):
    car_image = transparent_formula
    x_position = 100
    y_position = 520
    car_angle = 0


def game():
    game_loop = True

    pygame.display.set_caption("2D Racing Game - InGame")

    while True:

        car = Player()
        enemy_car = EnemyPlayer()

        while game_loop:

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (-350, -80))

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_w]:
                car.forward_control()

            if pressed_key[pygame.K_s]:
                car.backward_control()

            if pressed_key[pygame.K_d]:
                car.rotate_right()

            if pressed_key[pygame.K_a]:
                car.rotate_left()

            pygame.display.update()


game()

# def menu():
# pygame.display.set_caption("2D Racing Game - Menu")

# while True:

# game_screen.blit(menu_background, (0, 0))

# menu_font = font.render("Main Menu", True, "white")
# menu_hitbox = menu_font.get_rect(center=(620, 100))

# game_screen.blit(menu_font, menu_hitbox)

# for event in pygame.event.get():
# if event.type == pygame.QUIT:
# pygame.quit()

# pygame.display.update()


# menu()
