import pygame

from racing_game.config.settings import Settings
from racing_game.handler.key_binds import KeyBinds
from racing_game.loop_functions.functions import LoopFunctions, Collisions
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import LoadingImages


class MapLoop:
    @staticmethod
    def loop(player, enemy, enemy_route, background, map_image, map_border, map_restart, map_respawn, enemy_respawn,
             finish_line, finish_line_xy, x_range1, x_range2, y_range1, y_range2,
             lap_times_file, match_times_file):

        pygame.event.set_allowed(pygame.KEYDOWN)

        global enemy_car, player_car

        Settings.car_lap = 0
        Settings.enemy_lap = 0

        Settings.car_start_time = 0
        Settings.enemy_start_time = 0
        Settings.car_match_time = 0
        Settings.enemy_match_time = 0

        Settings.car_time_list = []
        Settings.enemy_time_list = []

        game_loop = 1

        Settings.countdown = 5
        Settings.last_count = pygame.time.get_ticks()

        while 1:

            clock = pygame.time.Clock()

            if enemy is None and enemy_route is None:
                player_car = player()

            if enemy is not None and enemy_route is None:
                player_car = player()
                enemy_car = enemy()
                enemy_car.car_image = enemy_car.random_enemy_car()

            if enemy is not None and enemy_route is not None:
                player_car = player()
                enemy_car = enemy()
                enemy_car.car_image = enemy_car.random_enemy_car()

            Settings.started = False

            while game_loop:

                clock.tick(Settings.game_tick)

                car_stopwatch = pygame.time.get_ticks() - Settings.car_start_time
                car_stopwatch = car_stopwatch // 100 / 10

                enemy_stopwatch = pygame.time.get_ticks() - Settings.enemy_start_time
                enemy_stopwatch = enemy_stopwatch // 100 / 10

                LoadingImages.GAME_SCREEN.blit(background, (0, 0))
                LoadingImages.GAME_SCREEN.blit(map_image, (0, 0))
                LoadingImages.GAME_SCREEN.blit(finish_line, finish_line_xy)
                LoadingImages.GAME_SCREEN.blit(map_border, (0, 0))

                # SOLO
                if enemy is None and enemy_route is None:
                    LoopFunctions.start_countdown(player_car, player_car)
                    # DrawUI.check_show_fps(DrawUI.game_show_fps, clock)

                # 1v1
                if enemy is not None and enemy_route is None:
                    LoopFunctions.start_countdown(player_car, enemy_car)
                    Settings.show_xy = 2
                    Settings.show_fps = 2

                    if Settings.show_ui == 1:
                        DrawUI.player_title()

                # VS PC
                if enemy is not None and enemy_route is not None:
                    LoopFunctions.start_countdown(player_car, enemy_car)
                    # DrawUI.check_show_fps(DrawUI.game_show_fps, clock)

                    enemy_car.start_drive()
                    enemy_car.pc_route = enemy_route(enemy_car)

                if Settings.show_ui == 1:
                    DrawUI.ui(player_car, car_stopwatch)

                    if enemy is not None and enemy_route is None:
                        DrawUI.enemy_ui(enemy_car, enemy_stopwatch)

                DrawUI.check_show_ui(DrawUI.ui, player_car, car_stopwatch)
                DrawUI.check_show_xy(player_car.car_position)
                DrawUI.check_show_fps(DrawUI.game_show_fps, clock)

                if enemy is not None:
                    DrawUI.enemy_animation(car_stopwatch, enemy_car)

                DrawUI.check_car_type(player_car)

                player_car.render_position(LoadingImages.GAME_SCREEN)
                player_car.add_nitro(car_stopwatch)

                if enemy is not None:
                    enemy_car.render_position(LoadingImages.GAME_SCREEN)
                    enemy_car.add_nitro(enemy_stopwatch)

                LoopFunctions.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                if enemy is not None and enemy_route is not None:
                    KeyBinds.player_key_binds(player_car, player_car.get_car_rect(), enemy_car.get_car_rect(),
                                              map_border, map_restart)
                    Collisions.collision_vs_pc(player_car, enemy_car, player_car.get_car_rect(),
                                               enemy_car.get_car_rect(),
                                               map_border, enemy_stopwatch, Settings.car_time_list,
                                               Settings.enemy_time_list, map_restart, map_respawn, enemy_respawn,
                                               x_range1, x_range2, y_range1, y_range2)

                    if x_range1 < player_car.x < x_range2:
                        if y_range1 < player_car.y < y_range2:
                            LoopFunctions.check_laps(player_car, enemy_car, car_stopwatch, map_restart,
                                                     map_respawn, enemy_respawn)
                            LoopFunctions.end_game(player_car, enemy_car, map_restart, lap_times_file,
                                                   match_times_file, map_respawn, enemy_respawn)

                if enemy is None and enemy_route is None:
                    KeyBinds.player_key_binds(player_car, player_car.get_car_rect(), None, map_border, map_restart)
                    Collisions.collision_solo(player_car, map_border, map_restart)

                    if x_range1 < player_car.x < x_range2:
                        if y_range1 < player_car.y < y_range2:
                            LoopFunctions.check_laps(player_car, None, car_stopwatch, map_restart,
                                                     map_respawn, enemy_respawn)
                            LoopFunctions.end_game(player_car, None, map_restart, lap_times_file,
                                                   match_times_file, map_respawn, enemy_respawn)

                if enemy is not None and enemy_route is None:
                    KeyBinds.player_key_binds(player_car, player_car.get_car_rect(), enemy_car.get_car_rect(),
                                              map_border, map_restart)
                    KeyBinds.enemy_key_binds(enemy_car, player_car.get_car_rect(), enemy_car.get_car_rect(), map_border)

                    Collisions.collision_vs_player(player_car, enemy_car, player_car.get_car_rect(),
                                                   enemy_car.get_car_rect(), map_border)

                    if x_range1 < player_car.x < x_range2:
                        if y_range1 < player_car.y < y_range2:
                            LoopFunctions.check_laps(player_car, enemy_car, car_stopwatch, map_restart,
                                                     map_respawn, enemy_respawn)
                            LoopFunctions.end_game(player_car, enemy_car, map_restart, lap_times_file,
                                                   match_times_file, map_respawn, enemy_respawn)

                    if x_range1 < enemy_car.x < x_range2:
                        if y_range1 < enemy_car.y < y_range2:
                            LoopFunctions.enemy_check_laps(enemy_car, enemy_stopwatch, map_restart, enemy_respawn)
                            LoopFunctions.enemy_end_game(map_restart)

            pygame.display.update()
