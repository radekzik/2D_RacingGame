import pygame


def res(image, amount):
    new_res = (image.get_width() * amount), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res).convert_alpha()


def res_width(image, amount):
    new_res = (image.get_width() * amount)

    return pygame.transform.scale(image, new_res).convert_alpha()


def res_height(image, amount):
    new_res = (image.get_height() * amount)

    return pygame.transform.scale(image, new_res).convert_alpha()


def image_position(game_window, car_image, car_left_corner, car_angle):
    angle_position = pygame.transform.rotate(car_image, car_angle).convert_alpha()

    car_hitbox = angle_position.get_rect(center=car_image.get_rect(topleft=car_left_corner).center)

    game_window.blit(angle_position, car_hitbox.topleft)
