
from racing_game.cars.enemy import EnemyPlayer
from racing_game.cars.pc import PCPlayer
from racing_game.cars.player import Player
from racing_game.config import settings
from racing_game.loop_methods import game_methods
from racing_game.maps.map_loop import MapLoop
from racing_game.ui import load_image
from racing_game.ui.load_image import green_forest, first_map, finish_line, first_map_border, second_map, \
    second_map_border, third_map, third_map_border, fourth_map, fourth_map_border, finish_line_x3, dark_green_forest, \
    fifth_map, fifth_map_border, finish_line_x2


class AllMaps:

    # FIRST MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_vs_pc():
        game_methods.loading_game("Loading", "VS PC", "I. MAP", load_image.first_map_loading)
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
        game_methods.loading_game("Loading", "SOLO", "I. MAP", load_image.first_map_loading)
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
        game_methods.loading_game("Loading", "1V1", "I. MAP", load_image.first_map_loading)
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
        game_methods.loading_game("Loading", "VS PC", "II. MAP", load_image.second_map_loading)
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
        game_methods.loading_game("Loading", "SOLO", "II. MAP", load_image.second_map_loading)
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
        game_methods.loading_game("Loading", "1V1", "II. MAP", load_image.second_map_loading)
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
        game_methods.loading_game("Loading", "VS PC", "III. MAP", load_image.third_map_loading)
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
        game_methods.loading_game("Loading", "SOLO", "III. MAP", load_image.third_map_loading)
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
        game_methods.loading_game("Loading", "1V1", "III. MAP", load_image.third_map_loading)
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
        game_methods.loading_game("Loading", "VS PC", "IV. MAP", load_image.fourth_map_loading)
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
        game_methods.loading_game("Loading", "SOLO", "IV. MAP", load_image.fourth_map_loading)
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
        game_methods.loading_game("Loading", "1V1", "IV. MAP", load_image.fourth_map_loading)
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
        game_methods.loading_game("Loading", "VS PC", "V. MAP", load_image.fifth_map_loading)
        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, green_forest, fifth_map, fifth_map_border,
                     AllMaps.fifth_map_vs_pc, Player.respawn_fifth_map,
                     finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)

    @staticmethod
    def fifth_map_solo():
        game_methods.loading_game("Loading", "SOLO", "V. MAP", load_image.fifth_map_loading)
        MapLoop.loop(Player, None, None, green_forest, fifth_map, fifth_map_border,
                     AllMaps.fifth_map_solo, Player.respawn_fifth_map,
                     finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)

    @staticmethod
    def fifth_map_1v1():
        game_methods.loading_game("Loading", "1V1", "V. MAP", load_image.fifth_map_loading)
        MapLoop.loop(Player, EnemyPlayer, None, green_forest, fifth_map, fifth_map_border,
                     AllMaps.fifth_map_1v1, Player.respawn_fifth_map,
                     finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)
