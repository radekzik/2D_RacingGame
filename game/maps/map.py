import pygame.display

from game.cars.pc import PCPlayer, random_car
from game.config import settings

from game.handler.key_binds import player_key_binds
from game.loop_methods import game_methods
from game.ui import draw
from game.cars.player import Player

from game.config.settings import FIRST_MAP_FINISH_LINE_X, FIRST_MAP_FINISH_LINE_Y
from game.ui.load_image import first_map, green_forest, first_map_border, finish_line, game_screen, second_map, \
    second_map_border, third_map, third_map_border


class Map:

    def __init__(self):

        self.game_screen = game_screen
        self.tick = settings.game_tick

        self.background_image = self.background_image
        self.map_image = self.map_image
        self.map_border_image = self.map_border_image

        self.finish_line_image = self.finish_line_image
        self.finish_line_x = self.finish_line_x
        self.finish_line_y = self.finish_line_y

        self.map_loop(FirstMap, PCPlayer)

        # self.map_type = self.map_type
        # self.title = self.title
        # self.first_finish_line_x_range = self.first_finish_line_x_range
        # self.first_finish_line_y_range = self.first_finish_line_y_range
        # self.second_finish_line_x_range = self.second_finish_line_x_range
        # self.second_finish_line_y_range = self.second_finish_line_y_range

    def draw_map_images(self, screen, background, map_img, finish_line, x, y, border):
        screen.blit(background, (0, 0))
        screen.blit(map_img, (0, 0))
        screen.blit(finish_line, (x, y))
        screen.blit(border, (0, 0))

    # def loop_methods(self, car, pc_car, car_stopwatch, enemy_stopwatch):

    def map_loop(self, map_type, enemy_type):

        game_loop = True

        # pygame.display.set_caption("2D Racing Game - FirstMap - VS PC")

        settings.last_count = pygame.time.get_ticks()

        while True:

            map_type()

            clock = pygame.time.Clock()

            player = Player()
            enemy = enemy_type()

            enemy.car_image = random_car()

            settings.started = False

            while game_loop:

                clock.tick(settings.game_tick)

                car_stopwatch = pygame.time.get_ticks() - settings.car_start_time
                car_stopwatch = car_stopwatch // 100 / 10

                enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
                enemy_stopwatch = enemy_stopwatch // 100 / 10

                self.draw_map_images(self.game_screen, self.background_image, self.map_image, self.finish_line_image,
                                     self.finish_line_x, self.finish_line_y, self.map_border_image)

                game_methods.start_countdown(player, enemy)
                enemy.start_drive()
                enemy.first_map_route()

                draw.game_info(settings.car_match_time, clock, settings.car_lap, car_stopwatch)
                player.car_info()

                draw.enemy_animation(car_stopwatch, enemy)

                game_methods.check_car_type(player)
                game_methods.speedometer(player)

                player.render_position(self.game_screen)
                enemy.render_position(self.game_screen)
                pygame.display.update()

                game_methods.start_game()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                player_key_binds(player, player.get_car_rect(), enemy.get_car_rect(), self.map_border_image,
                                 self.map_type)
                game_methods.collision_vs_pc(player, enemy, player.get_car_rect(), enemy.get_car_rect(),
                                             self.map_border_image,
                                             enemy_stopwatch,
                                             settings.car_time_list,
                                             settings.enemy_time_list, self.map_type)

                if self.first_finish_line_x_range < player.x < self.second_finish_line_x_range:
                    if self.first_finish_line_y_range < player.y < self.second_finish_line_y_range:
                        game_methods.check_laps(player, enemy, car_stopwatch, self.map_type, player.respawn_first_map)
                        game_methods.end_game(player, enemy, self.map_type, settings.f_map_lap_times,
                                              settings.f_map_match_times)

            pygame.display.update()


class FirstMap(Map):
    background_image = green_forest

    map_image = first_map
    map_border_image = first_map_border

    finish_line_image = finish_line
    finish_line_x = FIRST_MAP_FINISH_LINE_X
    finish_line_y = FIRST_MAP_FINISH_LINE_Y


class SecondMap(Map):
    def __init__(self):
        super().__init__()
        self.background_image = green_forest

        self.map_image = second_map
        self.map_border_image = second_map_border

        self.finish_line_image = finish_line
        self.finish_line_x = FIRST_MAP_FINISH_LINE_X
        self.finish_line_y = FIRST_MAP_FINISH_LINE_Y


class ThirdMap(Map):
    def __init__(self):
        super().__init__()
        self.background_image = green_forest

        self.map_image = third_map
        self.map_border_image = third_map_border

        self.finish_line_image = finish_line
        self.finish_line_x = FIRST_MAP_FINISH_LINE_X
        self.finish_line_y = FIRST_MAP_FINISH_LINE_Y
