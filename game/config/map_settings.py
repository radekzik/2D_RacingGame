from game.cars.enemy import EnemyPlayer
from game.cars.pc import PCPlayer
from game.cars.player import Player
from game.ui.load_image import first_map, first_map_border, green_background, second_map_border, second_map, \
     finish_line, third_map, third_map_border

FINISH_LINES = {
    1: {'FINISH_LINE': (580, 840), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
    2: {'FINISH_LINE': (580, 788), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
    3: {'FINISH_LINE': (480, 855), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
}

VS_PC_SETTINGS = {
    1: {"PLAYER": Player, "ENEMY": PCPlayer, "ENEMY_ROUTE": PCPlayer.first_map_route, "BACKGROUND": green_background,
        "MAP_IMAGE": first_map, "MAP_BORDER": first_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[1],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][1]
        },
    2: {"PLAYER": Player, "ENEMY": PCPlayer, "ENEMY_ROUTE": PCPlayer.second_map_route, "BACKGROUND": green_background,
        "MAP_IMAGE": second_map, "MAP_BORDER": second_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[2],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[2]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[2]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[2]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[2]['FINISH_LINE_RANGES'][1][1]
        },
    3: {"PLAYER": Player, "ENEMY": PCPlayer, "ENEMY_ROUTE": PCPlayer.third_map_route, "BACKGROUND": green_background,
        "MAP_IMAGE": third_map, "MAP_BORDER": third_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[3],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[3]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[3]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[3]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[3]['FINISH_LINE_RANGES'][1][1]
        }
}

SOLO_SETTINGS = {
    1: {"PLAYER": Player, "ENEMY": None, "ENEMY_ROUTE": None, "BACKGROUND": green_background,
        "MAP_IMAGE": first_map, "MAP_BORDER": first_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[1],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][1]
        },
    2: {"PLAYER": Player, "ENEMY": None, "ENEMY_ROUTE": None, "BACKGROUND": green_background,
        "MAP_IMAGE": second_map, "MAP_BORDER": second_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[2],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[2]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[2]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[2]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[2]['FINISH_LINE_RANGES'][1][1]
        },
    3: {"PLAYER": Player, "ENEMY": None, "ENEMY_ROUTE": None, "BACKGROUND": green_background,
        "MAP_IMAGE": third_map, "MAP_BORDER": third_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[3],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[3]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[3]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[3]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[3]['FINISH_LINE_RANGES'][1][1]
        }
}

ONE_VS_ONE_SETTINGS = {
    1: {"PLAYER": Player, "ENEMY": EnemyPlayer, "ENEMY_ROUTE": None, "BACKGROUND": green_background,
        "MAP_IMAGE": first_map, "MAP_BORDER": first_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[1],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][1]
        },
    2: {"PLAYER": Player, "ENEMY": EnemyPlayer, "ENEMY_ROUTE": None, "BACKGROUND": green_background,
        "MAP_IMAGE": second_map, "MAP_BORDER": second_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[2],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][1]
        },
    3: {"PLAYER": Player, "ENEMY": EnemyPlayer, "ENEMY_ROUTE": None, "BACKGROUND": green_background,
        "MAP_IMAGE": third_map, "MAP_BORDER": third_map_border, "FINISH_LINE_IMAGE": finish_line,
        "FINISH_LINE_X_Y": FINISH_LINES[3],
        "FINISH_LINE_RANGE_X_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][0],
        "FINISH_LINE_RANGE_X_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][0],
        "FINISH_LINE_RANGE_Y_1": FINISH_LINES[1]['FINISH_LINE_RANGES'][0][1],
        "FINISH_LINE_RANGE_Y_2": FINISH_LINES[1]['FINISH_LINE_RANGES'][1][1]
        }
}

