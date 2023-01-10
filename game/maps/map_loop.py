import pygame

from game.cars.pc import random_car
from game.config import settings
from game.handler.key_binds import player_key_binds
from game.loop_methods import game_methods
from game.ui import draw
from game.ui.load_image import game_screen


# if settings.MAPS[1]['FINISH_LINE_RANGES'][0][0] < car.x < settings.MAPS[1]['FINISH_LINE_RANGES'][1][0]:
# if settings.MAPS[1]['FINISH_LINE_RANGES'][0][1] < car.y < settings.MAPS[1]['FINISH_LINE_RANGES'][1][1]:
class MapLoop:
    @staticmethod
    def loop(player, enemy, background, map_image, map_border, finish_line, finish_line_xy, x_range1,
             x_range2
             , y_range1, y_range2):
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

        settings.countdown = 5
        settings.last_count = pygame.time.get_ticks()

        while True:

            clock = pygame.time.Clock()

            car = player()
            pc_car = enemy()

            pc_car.car_image = random_car()

            settings.started = False

            while game_loop:

                clock.tick(settings.game_tick)

                car_stopwatch = pygame.time.get_ticks() - settings.car_start_time
                car_stopwatch = car_stopwatch // 100 / 10

                enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
                enemy_stopwatch = enemy_stopwatch // 100 / 10

                game_screen.blit(background, (0, 0))
                game_screen.blit(map_image, (0, 0))
                game_screen.blit(finish_line, finish_line_xy)
                game_screen.blit(map_border, (0, 0))

                game_methods.start_countdown(car, pc_car)
                if not None:
                    pc_car.start_drive()
                    #enemy_route()
                    pc_car.first_map_route()

                draw.game_info(settings.car_match_time, clock, settings.car_lap, car_stopwatch)
                car.car_info()

                draw.enemy_animation(car_stopwatch, pc_car)

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

                player_key_binds(car, car.get_car_rect(), pc_car.get_car_rect(), map_border)
                game_methods.collision_vs_pc(car, pc_car, car.get_car_rect(), pc_car.get_car_rect(),
                                             map_border, enemy_stopwatch, settings.car_time_list,
                                             settings.enemy_time_list)

                if x_range1 < car.x < x_range2:
                    if y_range1 < car.y < y_range2:
                        game_methods.check_laps(car, pc_car, car_stopwatch, car.respawn_first_map)
                        game_methods.end_game(car, pc_car, settings.f_map_lap_times,
                                              settings.f_map_match_times)

            pygame.display.update()
