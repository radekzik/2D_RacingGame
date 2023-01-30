
from racing_game.cars.enemy import EnemyPlayer
from racing_game.cars.pc import PCPlayer
from racing_game.cars.player import Player
from racing_game.config import settings
from racing_game.maps.map_loop import MapLoop
from racing_game.ui import loading_images
from racing_game.ui.draw_ui import DrawUI


class AllMaps:

    # FIRST MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "I. MAP", loading_images.first_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.first_map_route, DrawUI.random_selected_map_background(),
                     loading_images.MAPS[1]["MAP"], loading_images.MAPS[1]["BORDER"],
                     AllMaps.first_map_vs_pc, Player.respawn_first_map, PCPlayer.respawn_first_map,
                     loading_images.finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[1]["LAP_TIMES"], settings.FILE_PATHS[1]["MATCH_TIMES"])

    @staticmethod
    def first_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "I. MAP", loading_images.first_map_loading)

        MapLoop.loop(Player, None, None, DrawUI.random_selected_map_background(),
                     loading_images.MAPS[1]["MAP"], loading_images.MAPS[1]["BORDER"],
                     AllMaps.first_map_solo, Player.respawn_first_map, None,
                     loading_images.finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[1]["LAP_TIMES"], settings.FILE_PATHS[1]["MATCH_TIMES"])

    @staticmethod
    def first_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "I. MAP", loading_images.first_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_selected_map_background(),
                     loading_images.MAPS[1]["MAP"], loading_images.MAPS[1]["BORDER"],
                     AllMaps.first_map_1v1, Player.respawn_first_map, EnemyPlayer.respawn_first_map,
                     loading_images.finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[1]["LAP_TIMES"], settings.FILE_PATHS[1]["MATCH_TIMES"])

    # SECOND MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def second_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "II. MAP", loading_images.second_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.second_map_route, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[2]["MAP"], loading_images.MAPS[2]["BORDER"],
                     AllMaps.second_map_vs_pc, Player.respawn_second_map, PCPlayer.respawn_second_map,
                     loading_images.finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[2]["LAP_TIMES"], settings.FILE_PATHS[2]["MATCH_TIMES"])

    @staticmethod
    def second_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "II. MAP", loading_images.second_map_loading)

        MapLoop.loop(Player, None, None, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[2]["MAP"], loading_images.MAPS[2]["BORDER"],
                     AllMaps.second_map_solo, Player.respawn_second_map, None,
                     loading_images.finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[2]["LAP_TIMES"], settings.FILE_PATHS[2]["MATCH_TIMES"])

    @staticmethod
    def second_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "II. MAP", loading_images.second_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[2]["MAP"], loading_images.MAPS[2]["BORDER"],
                     AllMaps.second_map_1v1, Player.respawn_second_map, EnemyPlayer.respawn_second_map,
                     loading_images.finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[2]["LAP_TIMES"], settings.FILE_PATHS[2]["MATCH_TIMES"])

    # THIRD MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def third_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "III. MAP", loading_images.third_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.third_map_route, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[3]["MAP"], loading_images.MAPS[3]["BORDER"],
                     AllMaps.third_map_vs_pc, Player.respawn_third_map, PCPlayer.respawn_third_map,
                     loading_images.finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[3]["LAP_TIMES"], settings.FILE_PATHS[3]["MATCH_TIMES"])

    @staticmethod
    def third_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "III. MAP", loading_images.third_map_loading)

        MapLoop.loop(Player, None, None, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[3]["MAP"], loading_images.MAPS[3]["BORDER"],
                     AllMaps.third_map_solo, Player.respawn_third_map, None,
                     loading_images.finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[3]["LAP_TIMES"], settings.FILE_PATHS[3]["MATCH_TIMES"])

    @staticmethod
    def third_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "III. MAP", loading_images.third_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[3]["MAP"], loading_images.MAPS[3]["BORDER"],
                     AllMaps.third_map_1v1, Player.respawn_third_map, EnemyPlayer.respawn_third_map,
                     loading_images.finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[3]["LAP_TIMES"], settings.FILE_PATHS[3]["MATCH_TIMES"])

    # FOURTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fourth_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "IV. MAP", loading_images.fourth_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[4]["MAP"], loading_images.MAPS[4]["BORDER"],
                     AllMaps.fourth_map_vs_pc, Player.respawn_fourth_map, PCPlayer.respawn_fourth_map,
                     loading_images.finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[4]["LAP_TIMES"], settings.FILE_PATHS[4]["MATCH_TIMES"])

    @staticmethod
    def fourth_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "IV. MAP", loading_images.fourth_map_loading)

        MapLoop.loop(Player, None, None, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[4]["MAP"], loading_images.MAPS[4]["BORDER"],
                     AllMaps.fourth_map_solo, Player.respawn_fourth_map, None,
                     loading_images.finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[4]["LAP_TIMES"], settings.FILE_PATHS[4]["MATCH_TIMES"])

    @staticmethod
    def fourth_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "IV. MAP", loading_images.fourth_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_all_maps_background(),
                     loading_images.MAPS[4]["MAP"], loading_images.MAPS[4]["BORDER"],
                     AllMaps.fourth_map_1v1, Player.respawn_fourth_map, EnemyPlayer.respawn_fourth_map,
                     loading_images.finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[4]["LAP_TIMES"], settings.FILE_PATHS[4]["MATCH_TIMES"])

    # FIFTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fifth_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "V. MAP", loading_images.fifth_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, DrawUI.random_selected_map_background(),
                     loading_images.MAPS[5]["MAP"], loading_images.MAPS[5]["BORDER"],
                     AllMaps.fifth_map_vs_pc, Player.respawn_fifth_map, PCPlayer.respawn_fifth_map,
                     loading_images.finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[5]["LAP_TIMES"], settings.FILE_PATHS[5]["MATCH_TIMES"])

    @staticmethod
    def fifth_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "V. MAP", loading_images.fifth_map_loading)

        MapLoop.loop(Player, None, None, DrawUI.random_selected_map_background(),
                     loading_images.MAPS[5]["MAP"], loading_images.MAPS[5]["BORDER"],
                     AllMaps.fifth_map_solo, Player.respawn_fifth_map, None,
                     loading_images.finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[5]["LAP_TIMES"], settings.FILE_PATHS[5]["MATCH_TIMES"])

    @staticmethod
    def fifth_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "V. MAP", loading_images.fifth_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, DrawUI.random_selected_map_background(),
                     loading_images.MAPS[5]["MAP"], loading_images.MAPS[5]["BORDER"],
                     AllMaps.fifth_map_1v1, Player.respawn_fifth_map, EnemyPlayer.respawn_fifth_map,
                     loading_images.finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.FILE_PATHS[5]["LAP_TIMES"], settings.FILE_PATHS[5]["MATCH_TIMES"])
