import pygame

from game.ui import draw
from game.loop_methods import game_methods
from game.config import settings
from game.cars.enemy import EnemyPlayer
from game.handler.key_binds import player_key_binds
from game.ui.load_image import game_screen, finish_line, second_map_border, \
    second_map, green_forest
from game.cars.pc import PCPlayer, random_car
from game.cars.player import Player
from game.config.settings import FIRST_FINISH_LINE_X_RANGE, FIRST_FINISH_LINE_Y_RANGE, \
    SECOND_FINISH_LINE_X_RANGE, SECOND_FINISH_LINE_Y_RANGE, SECOND_MAP_FINISH_LINE_X, SECOND_MAP_FINISH_LINE_Y


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

        pc_car.car_image = random_car()

        settings.started = False

        while game_loop:

            clock.tick(settings.game_tick)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(green_forest, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (SECOND_MAP_FINISH_LINE_X, SECOND_MAP_FINISH_LINE_Y))
            game_screen.blit(second_map_border, (0, 0))

            game_methods.start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.second_map_route()

            draw.game_info(settings.car_match_time, clock, settings.car_lap, stopwatch)

            car.car_info()

            draw.enemy_animation(stopwatch, pc_car)

            game_methods.check_car_type(car)
            game_methods.speedometer(car)

            car.render_position(game_screen)
            pc_car.render_position(game_screen)

            pygame.display.update()
            game_methods.start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            player_key_binds(car, car.get_car_rect(), pc_car.get_car_rect(), second_map_border, game_second_map)

            game_methods.collision_vs_pc(car, pc_car, car.get_car_rect(), pc_car.get_car_rect(), second_map_border,
                                         enemy_stopwatch,
                                         settings.car_time_list,
                                         settings.enemy_time_list, game_second_map)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    game_methods.check_laps(car, pc_car, stopwatch, game_second_map, car.respawn_first_map)
                    game_methods.end_game(car, pc_car, game_second_map, settings.s_map_lap_times,
                                          settings.s_map_match_times)

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

            game_screen.blit(green_forest, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (SECOND_MAP_FINISH_LINE_X, SECOND_MAP_FINISH_LINE_Y))
            game_screen.blit(second_map_border, (0, 0))

            game_methods.start_countdown(car, enemy_car)

            draw.game_info(settings.car_match_time, clock, settings.car_lap, stopwatch)

            car.car_info()

            game_methods.check_car_type(car)
            game_methods.speedometer(car)

            car.render_position(game_screen)

            pygame.display.update()
            game_methods.start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            player_key_binds(car, car.get_car_rect(), enemy_car.get_car_rect(), second_map_border, game_second_map_solo)

            game_methods.collision_solo(car, second_map_border)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    game_methods.check_laps(car, enemy_car, stopwatch, game_second_map_solo, car.respawn_first_map)
                    game_methods.end_game(car, enemy_car, game_second_map_solo, settings.s_map_lap_times,
                                          settings.s_map_match_times)

            pygame.display.update()
