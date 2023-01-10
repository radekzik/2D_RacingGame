MAPS = {
    1: {'FINISH_LINE': (580, 840), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
    2: {
        'FINISH_LINE': (580, 788),
        'FINISH_LINE_RANGES': [
            (650, 860),
            (680, 1080)
        ]
    },
    3: {
        'FINISH_LINE': (480, 855),
        'FINISH_LINE_RANGES': [
            (650, 860),
            (680, 1080)
        ]
    },
}

# check start game
started = False

# tick
game_tick = 60

map_type = 0
mode_type = 0

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
max_laps = 3
car_lap = 0
enemy_lap = 0

# lists
car_time_list = []
enemy_time_list = []

# on - 1 / off - 2
audio = 2
camera_focus = 2

# file paths
f_map_lap_times = "first_map_lap_times.txt"
f_map_match_times = "first_map_match_times.txt"

s_map_lap_times = "second_map_lap_times.txt"
s_map_match_times = "second_map_match_times.txt"

t_map_lap_times = "third_map_lap_times.txt"
t_map_match_times = "third_map_match_times.txt"

# finish line x-y
FIRST_MAP_FINISH_LINE_X = 580
FIRST_MAP_FINISH_LINE_Y = 840

SECOND_MAP_FINISH_LINE_X = 580
SECOND_MAP_FINISH_LINE_Y = 788

THIRD_MAP_FINISH_LINE_X = 480
THIRD_MAP_FINISH_LINE_Y = 855

# finish line x-y range
FIRST_FINISH_LINE_X_RANGE = 650
SECOND_FINISH_LINE_X_RANGE = 680

FIRST_FINISH_LINE_Y_RANGE = 860
SECOND_FINISH_LINE_Y_RANGE = 1080
