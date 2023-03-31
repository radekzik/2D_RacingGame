
from racing_game.storage.data_processing import DataProcessing


class Settings:
    FINISH_LINES = {
        1: {'FINISH_LINE': (580, 840), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
        2: {'FINISH_LINE': (580, 788), 'FINISH_LINE_RANGES': [(650, 800), (680, 1080)]},
        3: {'FINISH_LINE': (480, 855), 'FINISH_LINE_RANGES': [(550, 860), (580, 1080)]},
        4: {'FINISH_LINE': (550, 732), 'FINISH_LINE_RANGES': [(600, 750), (700, 1080)]},
        5: {'FINISH_LINE': (540, 800), 'FINISH_LINE_RANGES': [(550, 800), (670, 1080)]}
    }

    FILE_PATHS = {
        1: {"LAP_TIMES": "racing_game/storage/files/first_map_lap_times.txt",
            "MATCH_TIMES": "racing_game/storage/files/first_map_match_times.txt"},

        2: {"LAP_TIMES": "racing_game/storage/files/second_map_lap_times.txt",
            "MATCH_TIMES": "racing_game/storage/files/second_map_match_times.txt"},

        3: {"LAP_TIMES": "racing_game/storage/files/third_map_lap_times.txt",
            "MATCH_TIMES": "racing_game/storage/files/third_map_match_times.txt"},

        4: {"LAP_TIMES": "racing_game/storage/files/fourth_map_lap_times.txt",
            "MATCH_TIMES": "racing_game/storage/files/fourth_map_match_times.txt"},

        5: {"LAP_TIMES": "racing_game/storage/files/fifth_map_lap_times.txt",
            "MATCH_TIMES": "racing_game/storage/files/fifth_map_match_times.txt"},

        6: {"WINS": "racing_game/storage/files/wins.txt"},
    }

    # start check
    started = False

    # tick
    game_tick = 240

    # car types
    car_type = 1
    enemy_car_type = 0

    # countdown
    countdown = 5
    last_count = 0

    # times
    car_start_time = 0
    enemy_start_time = 0
    car_match_time = 0
    enemy_match_time = 0

    # laps
    max_laps = 3  # default
    car_lap = 0
    enemy_lap = 0

    # lists
    car_time_list = []
    enemy_time_list = []

    # audio - on - 1 / off - 2 --- vsync - on - 1 / off - 0
    audio = 1
    vsync = 1

    # on - 1 / off - 2
    show_fps = 1
    show_ui = 1
    show_xy = 1

    win_file = DataProcessing.load_wins(FILE_PATHS[6]["WINS"])

    win_coins = int(win_file[len(win_file) - 1])
    # win_coins = 30
    # print(win_coins)
