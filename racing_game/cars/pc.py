import math
import random

from racing_game.cars.car import Car
from racing_game.ui.loading_images import LoadingImages


class PCPlayer(Car):
    global difference_x, difference_y, angle, new_angle

    x_position = 700
    y_position = 900
    car_angle = 270
    car_image = LoadingImages.FORMULA[5]["CAR"]

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    FULL_DEGREES = 360
    HALF_DEGREES = 180

    PI = 3.14

    def __init__(self, pc_route=None):
        super().__init__()
        self.new_pc_route = None
        if pc_route is None:
            pc_route = []
        self.pc_route = pc_route
        self.next_route_position = 0

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

    def new_angle_pos(self):
        global difference_x, difference_y, angle, new_angle

        route_x, route_y = self.pc_route[self.next_route_position]

        difference_x, difference_y = (route_x - self.x, route_y - self.y)

        if difference_y == 0:
            angle = self.HALF_DEGREES
        else:
            xy_division = difference_x / difference_y

            angle = math.atan(xy_division)

        # print(angle)

        if route_y > self.y:
            angle += self.PI

        # print(angle)

        self.set_new_angle()

    def set_new_angle(self):
        global new_angle

        new_angle = self.car_angle - math.degrees(angle)

        if new_angle >= self.HALF_DEGREES:
            new_angle = new_angle - self.FULL_DEGREES

        if new_angle > 0:
            self.subtract_angle()

        else:
            self.add_angle()

    def add_angle(self):
        global new_angle

        # if self.car_angle > new_angle:
        # self.car_angle = self.car_angle + self.max_movement_speed
        # else:
        # self.car_angle = new_angle

        self.car_angle += min(self.max_movement_speed, abs(new_angle))

    def subtract_angle(self):
        global new_angle

        # if self.car_angle > new_angle:
        # self.car_angle = self.car_angle - self.max_movement_speed
        # else:
        # self.car_angle = new_angle

        self.car_angle -= min(self.max_movement_speed, abs(new_angle))

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
        # self.increase_speed()

    def increase_speed(self):

        if difference_x < 20 or difference_y < 20:
            self.max_speed = 0.5
            self.car_speed = 0.5

        else:
            self.max_speed = 3.3
            self.car_speed = 3.3

    def border_collision(self):
        self.car_speed = 0
        self.max_speed = 0

        self.max_speed -= 10
        self.car_speed -= 5

        self.movement()

    def first_map_route(self):

        self.pc_route = [(1121, 915), (1379, 637), (1655, 454), (1631, 119),
                         (980, 67), (813, 379), (353, 373), (200, 632), (340, 900), (754, 940)]

        # random_number = random.randint(1, 3)

        # route1 = [(1121, 915), (1379, 580), (1655, 420), (1631, 130), (1631, 130),
        # (1003, 30), (813, 350), (353, 350), (200, 600), (340, 900), (754, 990)]

        # route2 = [(1121, 915), (1379, 630), (1655, 470), (1631, 180), (1631, 180),
        # (1003, 80), (813, 400), (353, 400), (200, 650), (340, 900), (754, 1020)]

        # route3 = [(1121, 915), (1379, 680), (1655, 520), (1631, 230), (1631, 230),
        # (1003, 130), (813, 450), (353, 450), (200, 700), (340, 900), (754, 1050)]

        # route_list = [route1, route2, route3]

        # for x in range(3):
        # x += 1
        # if random_number == x:
        # self.pc_route = route_list[x - 1]

        return self.pc_route

    def second_map_route(self):
        self.pc_route = [(1390, 717), (1583, 493), (1576, 260), (1418, 123), (921, 217), (721, 233), (537, 94),
                         (274, 245), (192, 645), (409, 838), (769, 887), (910, 894)]

        # self.pc_route = [(1390, 750), (1583, 530), (1576, 260), (1418, 123), (921, 217), (721, 233), (537, 94),
        # (274, 245), (192, 645), (409, 838), (769, 887), (910, 894)]

        #self.pc_route = [(1044, 867), (1371, 720), (1604, 508), (1461, 150), (1038, 237), (890, 192), (611, 49),
                         #(188, 254), (157, 713), (524, 852), (910, 894)]

        self.pc_route = [(1044, 867), (1371, 720), (1634, 508), (1478, 123), (921, 217), (721, 233), (537, 94),
                         (274, 245), (192, 645), (409, 838), (769, 887), (910, 894)]

        return self.pc_route

    def third_map_route(self):
        self.pc_route = [(830, 792), (754, 371), (1102, 272), (1320, 475), (1251, 704), (1070, 780), (1370, 980),
                         (1635, 891), (1768, 606), (1740, 177), (1400, 85), (609, 106), (178, 99), (130, 503),
                         (200, 860), (778, 950)]

        return self.pc_route

    def fourth_map_route(self):
        self.pc_route = [(1121, 915), (1567, 823), (1756, 544), (1505, 186), (843, 130),
                         (337, 197), (140, 496), (282, 774), (630, 930), (887, 887)]

        return self.pc_route

    def fifth_map_route(self):
        #self.pc_route = [(1121, 915), (1567, 823), (1756, 544), (1505, 186), (843, 130),
                         #(337, 197), (140, 496), (282, 774), (630, 930), (887, 887)]

        #self.pc_route = [(1121, 900), (1585, 736), (1570, 262), (1037, 147), (374, 203),
                         #(110, 479), (131, 858), (493, 863), (693, 863)]

        #self.pc_route = [(1121, 915), (1567, 823), (1706, 544), (1505, 186), (843, 130),
                         #(280, 197), (140, 496), (182, 774), (600, 930), (887, 887)]

        self.pc_route = [(1121, 915), (1567, 823), (1679, 689), (1615, 250), (1357, 130),
                         (631, 148), (140, 231), (109, 667), (221, 859), (887, 887)]

        return self.pc_route

    def respawn_first_map(self):
        self.x = 700
        self.y = 950
        self.car_angle = 270

    def respawn_second_map(self):
        self.x = 700
        self.y = 900
        self.car_angle = 270

    def respawn_third_map(self):
        self.x = 630
        self.y = 900
        self.car_angle = 270

    def respawn_fourth_map(self):
        self.x = 700
        self.y = 900
        self.car_angle = 270

    def respawn_fifth_map(self):
        self.x = 680
        self.y = 950
        self.car_angle = 270
