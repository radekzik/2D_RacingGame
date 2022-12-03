import pygame
from load_image import finish_line

FINISH_LINE_X = 580
FINISH_LINE_Y = 849

FIRST_FINISH_LINE_X_RANGE = 650
SECOND_FINISH_LINE_X_RANGE = 680

FIRST_FINISH_LINE_Y_RANGE = 860
SECOND_FINISH_LINE_Y_RANGE = 1080


def get_car_rect(car_image, car_angle, car_x, car_y):
    rect_angle = pygame.transform.rotate(car_image, car_angle)
    car_rect = rect_angle.get_rect(topleft=(car_x, car_y), center=(car_x + 7.5, car_y + 25))

    return car_rect


def get_enemy_rect(enemy_car_image, enemy_car_angle, enemy_car_x, enemy_car_y):
    enemy_rect_angle = pygame.transform.rotate(enemy_car_image, enemy_car_angle)
    enemy_rect = enemy_rect_angle.get_rect(topleft=(enemy_car_x, enemy_car_y), center=(enemy_car_x + 10.5, enemy_car_y
                                                                                       + 28))
    return enemy_rect


def get_finish_line_rect():
    finish_line_rect = finish_line.get_rect(topleft=(FINISH_LINE_X, FINISH_LINE_Y))

    return finish_line_rect
