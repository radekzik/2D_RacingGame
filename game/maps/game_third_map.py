import pygame

from game.storage.storing_data import save_lap_time, save_match_time
from game.ui import draw
from game.loop_methods import game_methods
from game.config import settings
from game.handler.key_binds import player_key_binds
from game.ui.load_image import game_screen, menu_background, finish_line, normal_font, \
    third_map, third_map_border, green_background
from game.cars.pc import PCPlayer
from game.cars.player import Player
from game.cars.rects import get_car_rect, get_enemy_rect, FIRST_FINISH_LINE_X_RANGE, FIRST_FINISH_LINE_Y_RANGE, \
    SECOND_FINISH_LINE_X_RANGE, SECOND_FINISH_LINE_Y_RANGE, THIRD_MAP_FINISH_LINE_X, THIRD_MAP_FINISH_LINE_Y
from game.ui.resolution import draw_text


def game_third_map():
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

    pygame.display.set_caption("2D Racing Game - FirstMap - VS PC")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        pc_car = PCPlayer()

        settings.started = False

        while game_loop:

            clock.tick(settings.game_tick)

            car_stopwatch = pygame.time.get_ticks() - settings.car_start_time
            car_stopwatch = car_stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(green_background, (0, 0))
            game_screen.blit(third_map, (0, 0))
            game_screen.blit(finish_line, (THIRD_MAP_FINISH_LINE_X, THIRD_MAP_FINISH_LINE_Y))
            game_screen.blit(third_map_border, (0, 0))

            game_methods.start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.first_map_route()

            draw.game_info(settings.car_match_time, clock, settings.car_lap, car_stopwatch)

            car.car_info()

            #pc_car.first_map_car()
            draw.enemy_animation(car_stopwatch, pc_car)

            game_methods.check_car_type(car)

            car.render_position(game_screen)
            pc_car.render_position(game_screen)

            pygame.display.update()
            game_methods.start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # finish_line_rect = get_finish_line_rect()
            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(pc_car.car_image, pc_car.car_angle, pc_car.x, pc_car.y)

            player_key_binds(car, car_rect, enemy_rect, third_map_border)
            game_methods.collision_vs_pc(car, pc_car, car_rect, enemy_rect, third_map_border, enemy_stopwatch,
                                         settings.car_time_list,
                                         settings.enemy_time_list, game_third_map)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    game_methods.check_laps(car, pc_car, car_stopwatch, game_third_map, car.respawn_first_map)
                    game_methods.end_game(car, pc_car, game_third_map)
        pygame.display.update()
