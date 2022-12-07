import pygame


def res(image, amount):
    new_res = (image.get_width() * amount), (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


def res_width(image, amount):
    new_res = (image.get_width() * amount)

    return pygame.transform.scale(image, new_res)


def res_height(image, amount):
    new_res = (image.get_height() * amount)

    return pygame.transform.scale(image, new_res)


def image_position(game_window, car_image, car_left_corner, car_angle):
    angle_position = pygame.transform.rotate(car_image, car_angle)

    car_hitbox = angle_position.get_rect(center=car_image.get_rect(topleft=car_left_corner).center)

    game_window.blit(angle_position, car_hitbox.topleft)


def draw_text(text, font, color, x, y, game_window):
    set_font = font.render(text, True, color)
    game_window.blit(set_font, (x, y))
