import pygame
from game.ui.load_image import finish_line

pygame.init()

FIRST_MAP_FINISH_LINE_X = 580
FIRST_MAP_FINISH_LINE_Y = 840

SECOND_MAP_FINISH_LINE_X = 580
SECOND_MAP_FINISH_LINE_Y = 788

THIRD_MAP_FINISH_LINE_X = 480
THIRD_MAP_FINISH_LINE_Y = 855

FIRST_FINISH_LINE_X_RANGE = 650
SECOND_FINISH_LINE_X_RANGE = 680

FIRST_FINISH_LINE_Y_RANGE = 860
SECOND_FINISH_LINE_Y_RANGE = 1080


def get_car_rect(car_image, car_angle, car_x, car_y):
    rect_angle = pygame.transform.rotate(car_image, car_angle)
    car_rect = rect_angle.get_rect(topleft=(car_x, car_y), center=(car_x + 10.5, car_y + 28))

    return car_rect


def get_enemy_rect(enemy_car_image, enemy_car_angle, enemy_car_x, enemy_car_y):
    enemy_rect_angle = pygame.transform.rotate(enemy_car_image, enemy_car_angle)
    enemy_rect = enemy_rect_angle.get_rect(topleft=(enemy_car_x, enemy_car_y), center=(enemy_car_x + 10.5, enemy_car_y
                                                                                       + 28))
    return enemy_rect


def get_finish_line_rect():
    finish_line_rect = finish_line.get_rect(topleft=(FIRST_MAP_FINISH_LINE_X, FIRST_MAP_FINISH_LINE_Y))

    return finish_line_rect


#def test_rect(car, car_image, car_angle, game_screen):
    #car_center = (car.x + 10.5, car.y + 28)

    #rect = car.car_image.get_rect(center=car_center)

    #pivot = pygame.math.Vector2(car.x + 10.5, car.y + 28)

    #p0 = (pygame.math.Vector2(rect.topleft) - pivot).rotate(-car_angle) + pivot
    #p1 = (pygame.math.Vector2(rect.topright) - pivot).rotate(-car_angle) + pivot
    # = (pygame.math.Vector2(rect.bottomright) - pivot).rotate(-car_angle) + pivot
    #p3 = (pygame.math.Vector2(rect.bottomleft) - pivot).rotate(-car_angle) + pivot

    #a = pygame.draw.lines(game_screen, "yellow", True, [p0, p1, p2, p3], 3)

    # a = pygame.draw.rect(game_screen, "blue", [p0[0], p0[1], 21, 56], 0)

    # rrr = pygame.Rect

    # a1 = p0[0]
    # a2 = p0[1]

    # pygame.Rect((a1, a2), p1, p2, p3)
    # pygame.draw.rect(game_screen, "red", [p0, p1, p2, p3], 4)

    # print(p0[0], p0[1])
    # print(p1)
    # print(p2)
    # print(p3)

    # car_rect = car_image.get_rect()

    # x = round(p0[0])
    # y = round(p0[1])

    # car_rect = pygame.Rect(x, y, 21, 56)

    # car_rect.topleft = (p0[0], p0[1])
    # car_rect.topright = (p1[0], p1[1])
    # car_rect.bottomleft = (p3[0], p3[1])
    # car_rect.bottomright = (p2[0], p2[1])

    # p_rect_angle = pygame.transform.rotate(car_image, car_angle)

    # r.topleft = (p0[0], p0[1])
    # r.topright = (p1[0], p1[1])
    # r.bottomleft = (p3[0], p3[1])
    # r.bottomright = (p2[0], p2[1])

    # pygame.draw.rect(game_screen, "green", r)

    # topleft = (round(p0[0]), round(p0[1])), topright = (p1[0], p1[1]),
    # bottomright = (p2[0], p2[1]), bottomleft = (p3[0], p3[1])

    #return a
