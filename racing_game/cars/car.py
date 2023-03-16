import random

import pygame
import math

from racing_game.config.settings import Settings
from racing_game.ui.loading_images import LoadingImages


class Car:

    FULL_DEGREES = 360
    HALF_DEGREES = 180

    PI = 3.14

    NULL = 0

    def __init__(self):
        self.car_image = self.car_image
        self.x = self.x_position
        self.y = self.y_position
        self.car_speed = 0
        self.car_acceleration = 0.2
        self.max_speed = 3
        self.min_speed = -1
        self.movement_speed = 2
        self.max_movement_speed = 5
        self.car_angle = self.car_angle
        self.car_nitro = 0

        self.car_width = self.car_image.get_width()
        self.car_height = self.car_image.get_height()

    def rotate_left(self):
        self.car_angle += self.movement_speed

    def rotate_right(self):
        self.car_angle -= self.movement_speed

    @staticmethod
    def image_position(game_window, car_image, car_left_corner, car_angle):
        angle_position = pygame.transform.rotate(car_image, car_angle)

        car_hitbox = angle_position.get_rect(center=car_image.get_rect(topleft=car_left_corner).center)

        game_window.blit(angle_position, car_hitbox.topleft)

    def render_position(self, game_window):
        self.image_position(game_window, self.car_image, (self.x, self.y), self.car_angle)

    def movement(self):

        plane_angle = self.car_angle * (self.PI / self.HALF_DEGREES)

        self.x += -self.car_speed * math.sin(plane_angle)
        self.y += -self.car_speed * math.cos(plane_angle)

    def forward_control(self):

        # while self.car_speed <= self.max_speed:
        # self.car_speed = self.car_speed + self.car_acceleration

        # else:
        # self.car_speed = self.max_speed

        self.car_speed = min(self.car_speed + self.car_acceleration, self.max_speed)

        self.movement()

    def forward_slowdown(self):

        if self.car_speed > 0:
            self.car_speed = self.car_speed - self.car_acceleration / 6

        else:
            self.car_speed = 0

        self.movement()

    def backward_control(self):

        self.car_speed = max(self.car_speed - self.car_acceleration, -6)

        self.movement()

    def add_nitro(self, stopwatch):

        if stopwatch % 2 == 0:
            self.car_nitro += 1

        if self.car_nitro >= 10:
            self.car_nitro = 10

    def use_nitro(self):

        self.car_speed = self.car_speed + self.car_nitro

        if self.car_nitro <= 10:
            self.car_nitro -= 1

            if self.car_nitro <= 0:
                self.car_nitro = 0

        self.movement()

    def drift(self):

        while self.movement_speed <= self.max_movement_speed:
            self.movement_speed = self.movement_speed + (self.movement_speed / 8)

        else:
            self.movement_speed = self.movement_speed

    def out_of_track(self):
        self.car_speed = 0
        self.max_speed = 0
        self.movement_speed = 0
        self.max_movement_speed = 0

        self.max_speed -= 40
        self.car_speed -= 40

        self.movement()

    def car_collide(self):
        self.car_speed = 0
        self.max_speed = 0
        self.max_speed = self.max_speed - 0.1
        self.car_speed = self.car_speed - 0.1

        self.movement()

    def border_collide(self, map_border):
        car = pygame.mask.from_surface(self.car_image)
        out_of_track_detection = map_border.overlap(car, (self.x, self.y))

        return out_of_track_detection

    def get_car_rect(self):
        rect_angle = pygame.transform.rotate(self.car_image, self.car_angle)
        car_rect = rect_angle.get_rect(topleft=(self.x, self.y), center=(self.x + 10.5, self.y + 28))
        return car_rect

    def respawn_map(self, x, y, car_angle):
        self.x = x
        self.y = y
        self.car_angle = car_angle

    def random_enemy_car(self):
        random_number = random.randint(1, 18)

        car_list = [LoadingImages.FORMULA[1]["CAR"], LoadingImages.FORMULA[2]["CAR"], LoadingImages.FORMULA[3]["CAR"],
                    LoadingImages.FORMULA[4]["CAR"], LoadingImages.FORMULA[5]["CAR"], LoadingImages.FORMULA[6]["CAR"],
                    LoadingImages.SPORTS_CAR_I[1]["CAR"], LoadingImages.SPORTS_CAR_I[2]["CAR"],
                    LoadingImages.SPORTS_CAR_I[3]["CAR"], LoadingImages.SPORTS_CAR_I[4]["CAR"],
                    LoadingImages.SPORTS_CAR_II[1]["CAR"], LoadingImages.SPORTS_CAR_II[2]["CAR"],
                    LoadingImages.SPORTS_CAR_II[3]["CAR"], LoadingImages.SPORTS_CAR_II[4]["CAR"],
                    LoadingImages.CABRIO[1]["CAR"], LoadingImages.CABRIO[2]["CAR"], LoadingImages.CABRIO[3]["CAR"],
                    LoadingImages.CABRIO[4]["CAR"]]

        LoadingImages.FORMULA.keys()

        for x in range(18):
            x += 1
            if random_number == x:
                Settings.enemy_car_type = x
                self.car_image = car_list[x - 1]

        return self.car_image
