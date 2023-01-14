from game.cars.enemy import EnemyPlayer
from game.cars.pc import PCPlayer
from game.cars.player import Player
from game.config import settings
from game.maps.map_loop import MapLoop
from game.ui.load_image import green_background, first_map, finish_line, first_map_border, second_map, \
    second_map_border, third_map, third_map_border, fourth_map, fourth_map_border, finish_line_x2


# settings.MAPS[1]['FINISH_LINE_RANGES'][0][0] < enemy_car.x < settings.MAPS[1]['FINISH_LINE_RANGES'][1][0]
# settings.MAPS[1]['FINISH_LINE_RANGES'][0][1] < enemy_car.y < settings.MAPS[1]['FINISH_LINE_RANGES'][1][1]

# (settings.FIRST_MAP_FINISH_LINE_X, settings.FIRST_MAP_FINISH_LINE_Y)

class AllMaps:

    # FIRST MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, green_background, first_map, first_map_border, AllMaps.first_map_vs_pc,
                     finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.f_map_lap_times, settings.f_map_match_times)

    @staticmethod
    def first_map_solo():
        MapLoop.loop(Player, None, green_background, first_map, first_map_border, AllMaps.first_map_solo,
                     finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.f_map_lap_times, settings.f_map_match_times)

    @staticmethod
    def first_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, green_background, first_map, first_map_border, AllMaps.first_map_1v1,
                     finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.f_map_lap_times, settings.f_map_match_times)

    # SECOND MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def second_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, green_background, second_map, second_map_border, AllMaps.second_map_vs_pc,
                     finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.s_map_lap_times, settings.s_map_match_times)

    @staticmethod
    def second_map_solo():
        MapLoop.loop(Player, None, green_background, second_map, second_map_border, AllMaps.second_map_solo,
                     finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.s_map_lap_times, settings.s_map_match_times)

    @staticmethod
    def second_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, green_background, second_map, second_map_border, AllMaps.second_map_1v1,
                     finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.s_map_lap_times, settings.s_map_match_times)

    # THIRD MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def third_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, green_background, third_map, third_map_border, AllMaps.third_map_vs_pc,
                     finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.t_map_lap_times, settings.t_map_match_times)

    @staticmethod
    def third_map_solo():
        MapLoop.loop(Player, None, green_background, third_map, third_map_border, AllMaps.third_map_solo,
                     finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.t_map_lap_times, settings.t_map_match_times)

    @staticmethod
    def third_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, green_background, third_map, third_map_border, AllMaps.third_map_1v1,
                     finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.t_map_lap_times, settings.t_map_match_times)

    # FOURTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fourth_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, green_background, fourth_map, fourth_map_border, AllMaps.fourth_map_vs_pc,
                     finish_line_x2, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.fo_map_lap_times, settings.fo_map_match_times)

    @staticmethod
    def fourth_map_solo():
        MapLoop.loop(Player, None, green_background, fourth_map, fourth_map_border, AllMaps.fourth_map_solo,
                     finish_line_x2, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.fo_map_lap_times, settings.fo_map_match_times)

    @staticmethod
    def fourth_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, green_background, fourth_map, fourth_map_border, AllMaps.fourth_map_1v1,
                     finish_line_x2, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE,
                     settings.fo_map_lap_times, settings.fo_map_match_times)
