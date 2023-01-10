from game.cars.pc import PCPlayer
from game.cars.player import Player
from game.config import settings
from game.maps.map_loop import MapLoop
from game.ui.load_image import green_background, first_map, finish_line, first_map_border


class AllMaps:

    @staticmethod
    def first_map_vs_pc():
        MapLoop.loop(Player, PCPlayer, green_background, first_map, first_map_border, AllMaps.first_map_vs_pc,
                     Player.respawn_first_map, finish_line,
                     (settings.FIRST_MAP_FINISH_LINE_X, settings.FIRST_MAP_FINISH_LINE_Y),
                     settings.FIRST_FINISH_LINE_X_RANGE, settings.SECOND_FINISH_LINE_X_RANGE,
                     settings.FIRST_FINISH_LINE_Y_RANGE, settings.SECOND_FINISH_LINE_Y_RANGE)
# dopsat soubory kam se ukladaji casy