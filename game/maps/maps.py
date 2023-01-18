import pygame

from game.cars.enemy import EnemyPlayer
from game.cars.pc import PCPlayer
from game.cars.player import Player
from game.config import settings
from game.maps.map_loop import MapLoop
from game.ui.load_image import green_forest, first_map, finish_line, first_map_border, second_map, \
    second_map_border, third_map, third_map_border, fourth_map, fourth_map_border, finish_line_x3, dark_green_forest, \
    fifth_map, fifth_map_border, finish_line_x2


class AllMaps:

    # FIRST MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, PCPlayer.first_map_route, green_forest, first_map, first_map_border,
                     AllMaps.first_map_vs_pc, Player.respawn_first_map,
                     finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.first_map_lap_times_file, settings.first_map_match_times_file)

    @staticmethod
    def first_map_solo():
        MapLoop.loop(Player, None, None, green_forest, first_map, first_map_border,
                     AllMaps.first_map_solo, Player.respawn_first_map,
                     finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.first_map_lap_times_file, settings.first_map_match_times_file)

    @staticmethod
    def first_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, None, green_forest, first_map, first_map_border,
                     AllMaps.first_map_1v1, Player.respawn_first_map,
                     finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.first_map_lap_times_file, settings.first_map_match_times_file)

    # SECOND MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def second_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, PCPlayer.second_map_route, dark_green_forest, second_map, second_map_border,
                     AllMaps.second_map_vs_pc, Player.respawn_second_map,
                     finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.second_map_lap_times_file, settings.second_map_match_times_file)

    @staticmethod
    def second_map_solo():
        MapLoop.loop(Player, None, None, dark_green_forest, second_map, second_map_border,
                     AllMaps.second_map_solo, Player.respawn_second_map,
                     finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.second_map_lap_times_file, settings.second_map_match_times_file)

    @staticmethod
    def second_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, None, dark_green_forest, second_map, second_map_border,
                     AllMaps.second_map_1v1, Player.respawn_second_map,
                     finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.second_map_lap_times_file, settings.second_map_match_times_file)

    # THIRD MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def third_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, PCPlayer.third_map_route, green_forest, third_map, third_map_border,
                     AllMaps.third_map_vs_pc, Player.respawn_third_map,
                     finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.third_map_lap_times_file, settings.third_map_match_times_file)

    @staticmethod
    def third_map_solo():
        MapLoop.loop(Player, None, None, green_forest, third_map, third_map_border,
                     AllMaps.third_map_solo, Player.respawn_third_map,
                     finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.third_map_lap_times_file, settings.third_map_match_times_file)

    @staticmethod
    def third_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, None, green_forest, third_map, third_map_border,
                     AllMaps.third_map_1v1, Player.respawn_third_map,
                     finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.third_map_lap_times_file, settings.third_map_match_times_file)

    # FOURTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fourth_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, dark_green_forest, fourth_map, fourth_map_border,
                     AllMaps.fourth_map_vs_pc, Player.respawn_fourth_map,
                     finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.fourth_map_lap_times_file, settings.fourth_map_match_times_file)

    @staticmethod
    def fourth_map_solo():
        MapLoop.loop(Player, None, None, dark_green_forest, fourth_map, fourth_map_border,
                     AllMaps.fourth_map_solo, Player.respawn_fourth_map,
                     finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.fourth_map_lap_times_file, settings.fourth_map_match_times_file)

    @staticmethod
    def fourth_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, None, dark_green_forest, fourth_map, fourth_map_border,
                     AllMaps.fourth_map_1v1, Player.respawn_fourth_map,
                     finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.fourth_map_lap_times_file, settings.fourth_map_match_times_file)

    # FIFTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fifth_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, dark_green_forest, fifth_map, fifth_map_border,
                     AllMaps.fifth_map_vs_pc, Player.respawn_fifth_map,
                     finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)

    @staticmethod
    def fifth_map_solo():
        MapLoop.loop(Player, None, None, dark_green_forest, fifth_map, fifth_map_border,
                     AllMaps.fifth_map_solo, Player.respawn_fifth_map,
                     finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)

    @staticmethod
    def fifth_map_1v1():
        MapLoop.loop(Player, EnemyPlayer, None, dark_green_forest, fifth_map, fifth_map_border,
                     AllMaps.fifth_map_1v1, Player.respawn_fifth_map,
                     finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)
