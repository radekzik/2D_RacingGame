import math
import random

from racing_game.cars.car import Car
from racing_game.ui.loading_images import LoadingImages


class PCPlayer(Car):
    x_position = 700
    y_position = 900
    car_angle = 270
    car_image = LoadingImages.FORMULA[5]["CAR"]

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    FULL_DEGREES = 360
    HALF_DEGREES = 180

    PI = 3.14

    NULL = 0

    def __init__(self, pc_route=None):
        super().__init__()
        self.new_pc_route = None
        if pc_route is None:
            pc_route = []
        self.pc_route = pc_route
        self.next_route_position = 0

        self.map_routes = [
            [(1121, 915), (1379, 637), (1655, 454), (1631, 119),
             (980, 67), (813, 379), (353, 373), (200, 632), (340, 900), (754, 940)],

            [(1044, 867), (1371, 720), (1634, 508), (1478, 123), (921, 217), (721, 233), (537, 94),
             (274, 245), (192, 645), (409, 838), (769, 887), (910, 894)],

            [(830, 792), (754, 371), (1102, 272), (1320, 475), (1251, 704), (1070, 780), (1370, 980),
             (1635, 891), (1768, 606), (1740, 177), (1400, 85), (609, 106), (178, 99), (130, 503),
             (200, 860), (778, 950)],

            [(1121, 915), (1567, 823), (1756, 544), (1505, 186), (843, 130),
             (337, 197), (140, 496), (282, 774), (630, 930), (887, 887)],

            [(1121, 915), (1567, 823), (1679, 689), (1615, 250), (1357, 130),
             (631, 148), (140, 231), (109, 667), (221, 859), (887, 887)]
        ]

    @staticmethod
    def get_route(route_number):
        return PCPlayer().map_routes[route_number - 1]

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

    def pos_difference(self):

        route_x, route_y = self.pc_route[self.next_route_position]

        difference_x, difference_y = (route_x - self.x, route_y - self.y)

        return difference_x, difference_y

    def new_angle_pos(self):

        difference_x, difference_y = self.pos_difference()

        xy_division = difference_x / difference_y
        angle = math.atan(xy_division)

        if self.pc_route[self.next_route_position][1] > self.y:
            angle = angle + self.PI

        self.set_new_angle(angle)

    def set_new_angle(self, angle):

        new_angle = self.car_angle - math.degrees(angle)

        if new_angle >= self.HALF_DEGREES:
            new_angle -= self.FULL_DEGREES

        if new_angle > self.NULL:
            self.subtract_angle(new_angle)

        else:
            self.add_angle(new_angle)

    def add_angle(self, angle):

        # if self.car_angle > new_angle:
        # self.car_angle = self.car_angle + self.max_movement_speed
        # else:
        # self.car_angle = new_angle

        self.car_angle += min(self.max_movement_speed, abs(angle))

    def subtract_angle(self, angle):

        # if self.car_angle > new_angle:
        # self.car_angle = self.car_angle - self.max_movement_speed
        # else:
        # self.car_angle = new_angle

        self.car_angle -= min(self.max_movement_speed, abs(angle))

    def car_route(self):

        self.route_random()

        new_position = 1

        if self.get_car_rect().collidepoint(self.new_pc_route):
            self.next_route_position = self.next_route_position + new_position

    def route_random(self):

        random_x_y = (random.randint(25, 25), random.randint(25, 25))

        self.new_pc_route = [sum(tup) for tup in zip(self.pc_route[self.next_route_position], random_x_y)]
        self.pc_route[self.next_route_position] = self.new_pc_route

        # print(self.enemy_car_route[self.next_position])

    def get_route_length(self):
        length = len(self.pc_route)

        return length

    def start_drive(self):
        route_exist = False

        if self.next_route_position >= self.get_route_length():
            route_exist = True

            return route_exist

        self.new_angle_pos()
        self.car_route()
        self.movement()
        self.forward_control()

    def increase_speed(self):

        # if difference_x < 20 or difference_y < 20:
        self.max_speed = 0.5
        self.car_speed = 0.5

        # else:
        self.max_speed = 3.3
        self.car_speed = 3.3

    def border_collision(self):
        self.car_speed = 0
        self.max_speed = 0

        self.max_speed -= 10
        self.car_speed -= 5

        self.movement()

    def respawn_map(self, x, y, angle):
        self.x = x
        self.y = y
        self.car_angle = angle

    def respawn_first_map(self):
        self.respawn_map(700, 950, 270)

    def respawn_second_map(self):
        self.respawn_map(700, 900, 270)

    def respawn_third_map(self):
        self.respawn_map(630, 900, 270)

    def respawn_fourth_map(self):
        self.respawn_map(700, 900, 270)

    def respawn_fifth_map(self):
        self.respawn_map(680, 950, 270)
