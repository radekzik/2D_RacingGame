import pygame

from game.cars.pc import random_car
from game.config import settings
from game.handler.key_binds import player_key_binds, enemy_key_binds
from game.loop_methods import game_methods
from game.loop_methods.game_methods import check_show_fps
from game.ui import draw
from game.ui.load_image import GAME_SCREEN


class MapLoop:
    @staticmethod
    def loop(player, enemy, enemy_route, background, map_image, map_border, map_restart, map_respawn,
             finish_line, finish_line_xy, x_range1, x_range2, y_range1, y_range2,
             lap_times_file, match_times_file):

        pygame.event.set_allowed(pygame.KEYDOWN)

        global enemy_car, player_car
        settings.max_laps = 3
        settings.car_lap = 0
        settings.enemy_lap = 0

        settings.animation_value = 0
        settings.car_start_time = 0
        settings.enemy_start_time = 0
        settings.car_match_time = 0
        settings.enemy_match_time = 0

        settings.car_time_list = []
        settings.enemy_time_list = []

        game_loop = 1

        settings.countdown = 5
        settings.last_count = pygame.time.get_ticks()

        while 1:

            clock = pygame.time.Clock()

            if enemy is None and enemy_route is None:
                player_car = player()

            if enemy is not None and enemy_route is None:
                player_car = player()
                enemy_car = enemy()

            if enemy is not None and enemy_route is not None:
                player_car = player()
                enemy_car = enemy()
                enemy_car.car_image = random_car()

            settings.started = False

            while game_loop:

                clock.tick(settings.game_tick)

                car_stopwatch = pygame.time.get_ticks() - settings.car_start_time
                car_stopwatch = car_stopwatch // 100 / 10

                enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
                enemy_stopwatch = enemy_stopwatch // 100 / 10

                GAME_SCREEN.blit(background, (0, 0))
                GAME_SCREEN.blit(map_image, (0, 0))
                GAME_SCREEN.blit(finish_line, finish_line_xy)
                GAME_SCREEN.blit(map_border, (0, 0))

                if enemy is None and enemy_route is None:
                    game_methods.start_countdown(player_car, player_car)

                if enemy is not None and enemy_route is None:
                    game_methods.start_countdown(player_car, enemy_car)

                if enemy is not None and enemy_route is not None:
                    game_methods.start_countdown(player_car, enemy_car)

                    enemy_car.start_drive()
                    enemy_car.pc_route = enemy_route(enemy_car)

                if settings.show_ui == 1:
                    draw.game_info(settings.car_match_time, settings.car_lap, car_stopwatch)
                    player_car.car_info()
                    game_methods.speedometer(player_car)

                check_show_fps(draw.game_show_fps, clock)

                if enemy is not None:
                    draw.enemy_animation(car_stopwatch, enemy_car)

                game_methods.check_car_type(player_car)

                player_car.render_position(GAME_SCREEN)

                if enemy is not None:
                    enemy_car.render_position(GAME_SCREEN)

                game_methods.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                if enemy is not None and enemy_route is not None:
                    player_key_binds(player_car, player_car.get_car_rect(), enemy_car.get_car_rect(), map_border,
                                     map_restart)
                    game_methods.collision_vs_pc(player_car, enemy_car, player_car.get_car_rect(),
                                                 enemy_car.get_car_rect(),
                                                 map_border, enemy_stopwatch, settings.car_time_list,
                                                 settings.enemy_time_list, map_restart)

                    if x_range1 < player_car.x < x_range2:
                        if y_range1 < player_car.y < y_range2:
                            game_methods.check_laps(player_car, enemy_car, car_stopwatch, map_restart, map_respawn)
                            game_methods.end_game(player_car, enemy_car, map_restart, lap_times_file,
                                                  settings.fourth_map_match_times_file)

                if enemy is None and enemy_route is None:
                    player_key_binds(player_car, player_car.get_car_rect(), None, map_border, map_restart)
                    game_methods.collision_solo(player_car, map_border)

                    if x_range1 < player_car.x < x_range2:
                        if y_range1 < player_car.y < y_range2:
                            game_methods.check_laps(player_car, None, car_stopwatch, map_restart, map_respawn)
                            game_methods.end_game(player_car, None, map_restart, lap_times_file,
                                                  match_times_file)

                if enemy is not None and enemy_route is None:
                    player_key_binds(player_car, player_car.get_car_rect(), enemy_car.get_car_rect(),
                                     map_border, map_restart)
                    enemy_key_binds(enemy_car, player_car.get_car_rect(), enemy_car.get_car_rect(), map_border)

                    game_methods.collision_vs_player(player_car, enemy_car, player_car.get_car_rect(),
                                                     enemy_car.get_car_rect(), map_border, enemy_stopwatch,
                                                     settings.car_time_list, settings.enemy_time_list,
                                                     map_restart)

                    if x_range1 < player_car.x < x_range2:
                        if y_range1 < player_car.y < y_range2:
                            game_methods.check_laps(player_car, enemy_car, car_stopwatch, map_restart, map_respawn)
                            game_methods.end_game(player_car, enemy_car, map_restart, lap_times_file,
                                                  settings.fourth_map_match_times_file)

            pygame.display.update()
