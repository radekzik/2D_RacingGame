import pygame

FINISH_LINES = {
    1: {'FINISH_LINE': (580, 840), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
    2: {'FINISH_LINE': (580, 788), 'FINISH_LINE_RANGES': [(650, 860), (680, 1080)]},
    3: {'FINISH_LINE': (480, 855), 'FINISH_LINE_RANGES': [(550, 860), (580, 1080)]},
    4: {'FINISH_LINE': (550, 732), 'FINISH_LINE_RANGES': [(600, 750), (700, 1080)]},
    5: {'FINISH_LINE': (540, 800), 'FINISH_LINE_RANGES': [(550, 800), (670, 1080)]}
}

# check start racing_game
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

nitro = 0

# on - 1 / off - 2
audio = 1
camera_focus = 2
vsync = 1

fullscreen_flag = pygame.HWSURFACE | pygame.FULLSCREEN
window_flag = pygame.HWSURFACE

fullscreen = 1
show_fps = 1
show_ui = 1
show_xy = 1

# file paths
first_map_lap_times_file = "first_map_lap_times.txt"
first_map_match_times_file = "first_map_match_times.txt"

second_map_lap_times_file = "second_map_lap_times.txt"
second_map_match_times_file = "second_map_match_times.txt"

third_map_lap_times_file = "third_map_lap_times.txt"
third_map_match_times_file = "third_map_match_times.txt"

fourth_map_lap_times_file = "fourth_map_lap_times.txt"
fourth_map_match_times_file = "fourth_map_match_times.txt"

fifth_map_lap_times_file = "fifth_map_lap_times.txt"
fifth_map_match_times_file = "fifth_map_match_times.txt"

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
