import pygame.display

from game.cars.pc import PCPlayer, random_car
from game.cars.rects import get_car_rect, get_enemy_rect
from game.config import settings
from game.config.settings import Settings
from game.handler.key_binds import player_key_binds
from game.loop_methods import game_methods
from game.ui import draw
from game.cars.player import Player

game_settings = Settings()


class Map:

    def __init__(self):
        self.title = self.title
        self.tick = game_settings.GAME_TICK
        self.map_type = self.map_type
        self.background_image = self.background_image
        self.map_image = self.map_image
        self.map_border_image = self.map_border_image
        self.finish_line_image = self.finish_line_image
        self.finish_line_x = self.finish_line_x
        self.finish_line_y = self.finish_line_y
        self.first_finish_line_x_range = self.first_finish_line_x_range
        self.first_finish_line_y_range = self.first_finish_line_y_range
        self.second_finish_line_x_range = self.second_finish_line_x_range
        self.second_finish_line_y_range = self.second_finish_line_y_range
        self.game_screen = self.game_screen

    def draw_map_images(self, game_screen, background, map, finish_line, x, y, border):
        game_screen.blit(background, (0, 0))
        game_screen.blit(map, (0, 0))
        game_screen.blit(finish_line, (x, y))
        game_screen.blit(border, (0, 0))

    def map_loop(self):

        game_loop = True

        # pygame.display.set_caption("2D Racing Game - FirstMap - VS PC")

        game_settings.last_count = pygame.time.get_ticks()

        while True:

            clock = pygame.time.Clock()

            car = Player()
            pc_car = PCPlayer()

            pc_car.car_image = random_car()

            game_settings.STARTED = False

            while game_loop:

                clock.tick(game_settings.game_tick)

                car_stopwatch = pygame.time.get_ticks() - game_settings.car_start_time
                car_stopwatch = car_stopwatch // 100 / 10

                enemy_stopwatch = pygame.time.get_ticks() - game_settings.enemy_start_time
                enemy_stopwatch = enemy_stopwatch // 100 / 10

                self.draw_map_images(self.game_screen, self.background_image, self.map_image, self.finish_line_image,
                                     self.finish_line_x, self.finish_line_y, self.map_border_image)

                game_methods.start_countdown(car, pc_car)
                pc_car.start_drive()
                pc_car.first_map_route()

                draw.game_info(game_settings.car_match_time, clock, game_settings.car_lap, car_stopwatch)
                car.car_info()

                draw.enemy_animation(car_stopwatch, pc_car)

                game_methods.check_car_type(car)
                game_methods.speedometer(car)

                car.render_position(self.game_screen)
                pc_car.render_position(self.game_screen)
                pygame.display.update()

                game_methods.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
                enemy_rect = get_enemy_rect(pc_car.car_image, pc_car.car_angle, pc_car.x, pc_car.y)

                player_key_binds(car, car_rect, enemy_rect, self.map_border_image, self.map_type)
                game_methods.collision_vs_pc(car, pc_car, car_rect, enemy_rect, self.map_border_image, enemy_stopwatch,
                                             game_settings.car_time_list,
                                             game_settings.enemy_time_list, self.map_type)

                if self.first_finish_line_x_range < car.x < self.second_finish_line_x_range:
                    if self.first_finish_line_y_range < car.y < self.second_finish_line_y_range:
                        game_methods.check_laps(car, pc_car, car_stopwatch, self.map_type, car.respawn_first_map)
                        game_methods.end_game(car, pc_car, self.map_type, game_settings.f_map_lap_times,
                                              game_settings.f_map_match_times)

            pygame.display.update()
