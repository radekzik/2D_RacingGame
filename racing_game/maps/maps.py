
from racing_game.cars.enemy import EnemyPlayer
from racing_game.cars.pc import PCPlayer
from racing_game.cars.player import Player
from racing_game.config.settings import Settings
from racing_game.maps.map_loop import MapLoop
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import LoadingImages


class AllMaps:

    # FIRST MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "I. MAP", LoadingImages.MAP_LOADING[1]["MAP"])

        MapLoop.loop(Player, PCPlayer, PCPlayer.first_map_route, DrawUI.random_selected_map_background(),
                     LoadingImages.MAPS[1]["MAP"], LoadingImages.MAPS[1]["BORDER"],
                     AllMaps.first_map_vs_pc, Player.respawn_first_map, PCPlayer.respawn_first_map,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[1]["FINISH_LINE"],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[1]["LAP_TIMES"], Settings.FILE_PATHS[1]["MATCH_TIMES"])

    @staticmethod
    def first_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "I. MAP", LoadingImages.MAP_LOADING[1]["MAP"])

        MapLoop.loop(Player, None, None, DrawUI.random_selected_map_background(),
                     LoadingImages.MAPS[1]["MAP"], LoadingImages.MAPS[1]["BORDER"],
                     AllMaps.first_map_solo, Player.respawn_first_map, None,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[1]["FINISH_LINE"],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[1]["LAP_TIMES"], Settings.FILE_PATHS[1]["MATCH_TIMES"])

    @staticmethod
    def first_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "I. MAP", LoadingImages.MAP_LOADING[1]["MAP"])

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_selected_map_background(),
                     LoadingImages.MAPS[1]["MAP"], LoadingImages.MAPS[1]["BORDER"],
                     AllMaps.first_map_1v1, Player.respawn_first_map, EnemyPlayer.respawn_first_map,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[1]["FINISH_LINE"],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[1]["LAP_TIMES"], Settings.FILE_PATHS[1]["MATCH_TIMES"])

    # SECOND MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def second_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "II. MAP", LoadingImages.MAP_LOADING[2]["MAP"])

        MapLoop.loop(Player, PCPlayer, PCPlayer.second_map_route, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[2]["MAP"], LoadingImages.MAPS[2]["BORDER"],
                     AllMaps.second_map_vs_pc, Player.respawn_second_map, PCPlayer.respawn_second_map,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[2]["FINISH_LINE"],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[2]["LAP_TIMES"], Settings.FILE_PATHS[2]["MATCH_TIMES"])

    @staticmethod
    def second_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "II. MAP", LoadingImages.MAP_LOADING[2]["MAP"])

        MapLoop.loop(Player, None, None, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[2]["MAP"], LoadingImages.MAPS[2]["BORDER"],
                     AllMaps.second_map_solo, Player.respawn_second_map, None,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[2]["FINISH_LINE"],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[2]["LAP_TIMES"], Settings.FILE_PATHS[2]["MATCH_TIMES"])

    @staticmethod
    def second_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "II. MAP", LoadingImages.MAP_LOADING[2]["MAP"])

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[2]["MAP"], LoadingImages.MAPS[2]["BORDER"],
                     AllMaps.second_map_1v1, Player.respawn_second_map, EnemyPlayer.respawn_second_map,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[2]["FINISH_LINE"],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[2]["LAP_TIMES"], Settings.FILE_PATHS[2]["MATCH_TIMES"])

    # THIRD MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def third_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "III. MAP", LoadingImages.MAP_LOADING[3]["MAP"])

        MapLoop.loop(Player, PCPlayer, PCPlayer.third_map_route, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[3]["MAP"], LoadingImages.MAPS[3]["BORDER"],
                     AllMaps.third_map_vs_pc, Player.respawn_third_map, PCPlayer.respawn_third_map,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[3]["FINISH_LINE"],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[3]["LAP_TIMES"], Settings.FILE_PATHS[3]["MATCH_TIMES"])

    @staticmethod
    def third_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "III. MAP", LoadingImages.MAP_LOADING[3]["MAP"])

        MapLoop.loop(Player, None, None, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[3]["MAP"], LoadingImages.MAPS[3]["BORDER"],
                     AllMaps.third_map_solo, Player.respawn_third_map, None,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[3]["FINISH_LINE"],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[3]["LAP_TIMES"], Settings.FILE_PATHS[3]["MATCH_TIMES"])

    @staticmethod
    def third_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "III. MAP", LoadingImages.MAP_LOADING[3]["MAP"])

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[3]["MAP"], LoadingImages.MAPS[3]["BORDER"],
                     AllMaps.third_map_1v1, Player.respawn_third_map, EnemyPlayer.respawn_third_map,
                     LoadingImages.FINISH_LINE[1]["FINISH_LINE"], Settings.FINISH_LINES[3]["FINISH_LINE"],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[3]["LAP_TIMES"], Settings.FILE_PATHS[3]["MATCH_TIMES"])

    # FOURTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fourth_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "IV. MAP", LoadingImages.MAP_LOADING[4]["MAP"])

        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[4]["MAP"], LoadingImages.MAPS[4]["BORDER"],
                     AllMaps.fourth_map_vs_pc, Player.respawn_fourth_map, PCPlayer.respawn_fourth_map,
                     LoadingImages.FINISH_LINE[3]["FINISH_LINE"], Settings.FINISH_LINES[4]["FINISH_LINE"],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[4]["LAP_TIMES"], Settings.FILE_PATHS[4]["MATCH_TIMES"])

    @staticmethod
    def fourth_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "IV. MAP", LoadingImages.MAP_LOADING[4]["MAP"])

        MapLoop.loop(Player, None, None, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[4]["MAP"], LoadingImages.MAPS[4]["BORDER"],
                     AllMaps.fourth_map_solo, Player.respawn_fourth_map, None,
                     LoadingImages.FINISH_LINE[3]["FINISH_LINE"], Settings.FINISH_LINES[4]["FINISH_LINE"],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[4]["LAP_TIMES"], Settings.FILE_PATHS[4]["MATCH_TIMES"])

    @staticmethod
    def fourth_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "IV. MAP", LoadingImages.MAP_LOADING[4]["MAP"])

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_all_maps_background(),
                     LoadingImages.MAPS[4]["MAP"], LoadingImages.MAPS[4]["BORDER"],
                     AllMaps.fourth_map_1v1, Player.respawn_fourth_map, EnemyPlayer.respawn_fourth_map,
                     LoadingImages.FINISH_LINE[3]["FINISH_LINE"], Settings.FINISH_LINES[4]["FINISH_LINE"],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[4]["LAP_TIMES"], Settings.FILE_PATHS[4]["MATCH_TIMES"])

    # FIFTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fifth_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "V. MAP", LoadingImages.MAP_LOADING[5]["MAP"])

        MapLoop.loop(Player, PCPlayer, PCPlayer.fifth_map_route, DrawUI.random_selected_map_background(),
                     LoadingImages.MAPS[5]["MAP"], LoadingImages.MAPS[5]["BORDER"],
                     AllMaps.fifth_map_vs_pc, Player.respawn_fifth_map, PCPlayer.respawn_fifth_map,
                     LoadingImages.FINISH_LINE[2]["FINISH_LINE"], Settings.FINISH_LINES[5]["FINISH_LINE"],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[5]["LAP_TIMES"], Settings.FILE_PATHS[5]["MATCH_TIMES"])

    @staticmethod
    def fifth_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "V. MAP", LoadingImages.MAP_LOADING[5]["MAP"])

        MapLoop.loop(Player, None, None, DrawUI.random_selected_map_background(),
                     LoadingImages.MAPS[5]["MAP"], LoadingImages.MAPS[5]["BORDER"],
                     AllMaps.fifth_map_solo, Player.respawn_fifth_map, None,
                     LoadingImages.FINISH_LINE[2]["FINISH_LINE"], Settings.FINISH_LINES[5]["FINISH_LINE"],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[5]["LAP_TIMES"], Settings.FILE_PATHS[5]["MATCH_TIMES"])

    @staticmethod
    def fifth_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "V. MAP", LoadingImages.MAP_LOADING[5]["MAP"])

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_selected_map_background(),
                     LoadingImages.MAPS[5]["MAP"], LoadingImages.MAPS[5]["BORDER"],
                     AllMaps.fifth_map_1v1, Player.respawn_fifth_map, EnemyPlayer.respawn_fifth_map,
                     LoadingImages.FINISH_LINE[2]["FINISH_LINE"], Settings.FINISH_LINES[5]["FINISH_LINE"],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     Settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     Settings.FILE_PATHS[5]["LAP_TIMES"], Settings.FILE_PATHS[5]["MATCH_TIMES"])
