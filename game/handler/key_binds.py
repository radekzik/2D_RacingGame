import pygame

import game.sounds
from game.ui import draw, menu
from game.config import settings


def player_key_binds(car, car_rect, enemy_rect, map_border):
    stopwatch = pygame.time.get_ticks() - settings.car_start_time
    stopwatch = stopwatch // 100 / 10
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_w]:
        car.forward_control()
        draw.car_animation(stopwatch, car)
        #game.sounds.engine_sound.play(-1)

    else:
        car.forward_slowdown()
        #game.sounds.engine_sound.stop()

    if pressed_key[pygame.K_s]:
        car.backward_control()
    else:
        car.forward_slowdown()

    if pressed_key[pygame.K_d]:
        car.rotate_right()

    if pressed_key[pygame.K_a]:
        car.rotate_left()

    if pressed_key[pygame.K_q]:
        car.drift()
    else:
        car.movement_speed = 2.5

    if pressed_key[pygame.K_x]:
        game.sounds.engine_sound.stop()
        game.sounds.starting_sound.stop()
        menu.mode_selection()


    if pressed_key[pygame.K_w]:
        if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(map_border)) \
                and not car_rect.colliderect(enemy_rect):
            car.nitro()


def enemy_key_binds(enemy_car, car_rect, enemy_rect, map_border):
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_i]:
        enemy_car.forward_control()
    else:
        enemy_car.forward_slowdown()

    if pressed_key[pygame.K_k]:
        enemy_car.backward_control()
    else:
        enemy_car.forward_slowdown()

    if pressed_key[pygame.K_l]:
        enemy_car.rotate_right()

    if pressed_key[pygame.K_j]:
        enemy_car.rotate_left()

    if pressed_key[pygame.K_u]:
        enemy_car.drift()
    else:
        enemy_car.movement_speed = 2.5

    if pressed_key[pygame.K_x]:
        menu.mode_selection()

    if pressed_key[pygame.K_i]:
        if pressed_key[pygame.K_o] and not enemy_car.border_collide(pygame.mask.from_surface(map_border)) \
                and not enemy_rect.colliderect(car_rect):
            enemy_car.nitro()
