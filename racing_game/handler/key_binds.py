import pygame

import racing_game.sounds.sounds
from racing_game.ui import menu
from racing_game.config import settings
from racing_game.ui.draw_ui import DrawUI


class KeyBinds:
    @staticmethod
    def player_key_binds(car, car_rect, enemy_rect, map_border, map_restart):
        stopwatch = pygame.time.get_ticks() - settings.car_start_time
        stopwatch = stopwatch // 100 / 10
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_w]:
            car.forward_control()
            DrawUI.car_animation(stopwatch, car)
            # check_audio(racing_game.sounds.sounds.car_engine.play)
            # check_audio_set_volume(racing_game.sounds.sounds.car_engine.set_volume, 0.05)

        else:
            car.forward_slowdown()
            # check_audio_set_volume(racing_game.sounds.sounds.car_engine.set_volume, 0.02)

            # if stopwatch % 2 == 0:
            # check_audio(racing_game.sounds.sounds.car_engine.stop)

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
            stop_sounds()
            menu.mode_selection()

        if pressed_key[pygame.K_r]:
            stop_sounds()
            # game_methods.restarting_game()
            map_restart()

        if pressed_key[pygame.K_w]:
            if enemy_rect is None:
                if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(map_border)):
                    car.use_nitro()
                    DrawUI.check_audio(racing_game.sounds.sounds.car_turbo.play)

            else:
                if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(map_border)) \
                        and not car_rect.colliderect(enemy_rect):
                    car.use_nitro()
                    DrawUI.check_audio(racing_game.sounds.sounds.car_turbo.play)

    @staticmethod
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
                enemy_car.use_nitro()
                DrawUI.check_audio(racing_game.sounds.sounds.car_turbo.play)


def stop_sounds():
    DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
    DrawUI.check_audio(racing_game.sounds.sounds.car_turbo.stop)
    DrawUI.check_audio(racing_game.sounds.sounds.crash_sound.stop)
    DrawUI.check_audio(racing_game.sounds.sounds.out_off_the_track_sound.stop)
    DrawUI.check_audio(racing_game.sounds.sounds.starting_sound.stop)
    DrawUI.check_audio(racing_game.sounds.sounds.countdown_sound.stop)
