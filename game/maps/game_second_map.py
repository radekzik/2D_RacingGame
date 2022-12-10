import pygame

from game.storage.storing_data import save_lap_time, save_match_time
from game.ui import draw
from game.loop_methods import game_methods
from game.config import settings
from game.cars.enemy import EnemyPlayer
from game.handler.key_binds import player_key_binds
from game.ui.load_image import game_screen, menu_background, finish_line, normal_font, second_map_border, \
    second_map
from game.cars.pc import PCPlayer
from game.cars.player import Player
from game.cars.rects import get_car_rect, get_enemy_rect, FIRST_FINISH_LINE_X_RANGE, FIRST_FINISH_LINE_Y_RANGE, \
    SECOND_FINISH_LINE_X_RANGE, SECOND_FINISH_LINE_Y_RANGE, SECOND_MAP_FINISH_LINE_X, SECOND_MAP_FINISH_LINE_Y
from game.ui.resolution import draw_text


def game_second_map():
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

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap - VS PC")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        pc_car = PCPlayer()

        settings.started = False

        while game_loop:

            clock.tick(settings.game_tick)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (SECOND_MAP_FINISH_LINE_X, SECOND_MAP_FINISH_LINE_Y))
            game_screen.blit(second_map_border, (0, 0))

            game_methods.start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.second_map_route()

            draw.game_info(settings.car_match_time, clock, settings.car_lap, stopwatch)

            car.car_info()

            pc_car.first_map_car()
            draw.enemy_animation(stopwatch, pc_car)

            game_methods.check_car_type(car)

            car.render_position(game_screen)
            pc_car.render_position(game_screen)

            pygame.display.update()
            game_methods.start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(pc_car.car_image, pc_car.car_angle, pc_car.x, pc_car.y)

            player_key_binds(car, car_rect, enemy_rect, second_map_border)

            game_methods.collision_vs_pc(car, pc_car,  car_rect, enemy_rect, second_map_border, enemy_stopwatch,
                                         settings.car_time_list,
                                         settings.enemy_time_list)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        settings.car_lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, stopwatch)
                        settings.car_match_time = settings.car_match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", normal_font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", normal_font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        game_methods.stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)

                        game_methods.check_new_game()
                        game_second_map()

                    if settings.car_lap == settings.max_laps:

                        if settings.car_lap > settings.enemy_lap:
                            draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        if settings.car_lap < settings.enemy_lap:
                            draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        settings.car_time_list.sort()
                        settings.enemy_time_list.sort()
                        draw.player_time_table(settings.car_time_list[0], settings.car_time_list[2],
                                               settings.car_match_time)

                        save_lap_time(settings.car_time_list[0])
                        save_match_time(settings.car_match_time)

                        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        game_methods.stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)
                        game_methods.check_new_game()
                        game_second_map()

            settings.animation_value += 1
            pygame.display.update()


def game_second_map_solo():
    settings.max_laps = 3
    settings.car_start_time = 0

    settings.car_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap - Solo")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        settings.started = False

        while game_loop:

            clock.tick(settings.game_tick)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (SECOND_MAP_FINISH_LINE_X, SECOND_MAP_FINISH_LINE_Y))
            game_screen.blit(second_map_border, (0, 0))

            game_methods.start_countdown(car, enemy_car)

            draw.game_info(settings.car_match_time, clock, settings.car_lap, stopwatch)

            car.car_info()

            game_methods.check_car_type(car)

            car.render_position(game_screen)

            pygame.display.update()
            game_methods.start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            player_key_binds(car, car_rect, enemy_rect, second_map_border)

            game_methods.collision_solo(car, second_map_border)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        settings.car_lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, stopwatch)

                        settings.car_match_time = settings.car_match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", normal_font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", normal_font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)
                        settings.car_time_list.clear()

                        settings.car_lap = 0
                        pygame.display.update()
                        settings.car_match_time = 0
                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                        game_methods.check_new_game()
                        game_second_map_solo()

                    if settings.car_lap == settings.max_laps:
                        settings.car_time_list.sort()

                        draw.player_time_table(settings.car_time_list[0], settings.car_time_list[2],
                                               settings.car_match_time)

                        save_lap_time(settings.car_time_list[0])
                        save_match_time(settings.car_match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        settings.car_time_list.clear()
                        settings.car_lap = 0
                        pygame.display.update()
                        settings.car_match_time = 0
                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()
                        game_methods.check_new_game()
                        game_second_map_solo()

            pygame.display.update()
