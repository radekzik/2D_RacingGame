import pygame

from racing_game.config import settings
from racing_game.ui.resolution import res

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FLAGS = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
GAME_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, 16, vsync=settings.vsync)

# maps
first_map = res(pygame.image.load("../images/maps/first_map.png"), 0.75).convert_alpha()
first_map_border = res(pygame.image.load("../images/borders/first_map_border.png"), 0.75).convert_alpha()

second_map = res(pygame.image.load("../images/maps/second_map.png"), 0.75).convert_alpha()
second_map_border = res(pygame.image.load("../images/borders/second_map_border.png"), 0.75).convert_alpha()

third_map = res(pygame.image.load("../images/maps/third_map.png"), 0.75).convert_alpha()
third_map_border = res(pygame.image.load("../images/borders/third_map_border.png"), 0.75).convert_alpha()

fourth_map = res(pygame.image.load("../images/maps/fourth_map.png"), 0.75).convert_alpha()
fourth_map_border = res(pygame.image.load("../images/borders/fourth_map_border.png"), 0.75).convert_alpha()

fifth_map = res(pygame.image.load("../images/maps/fifth_map.png"), 0.75).convert_alpha()
fifth_map_border = res(pygame.image.load("../images/borders/fifth_map_border.png"), 0.75).convert_alpha()

# cars

# formula
blue_formula = res(pygame.image.load("../images/cars/formula/formula_blue.png"), 1.1).convert_alpha()
blue_formula_2 = res(pygame.image.load("../images/cars/formula/formula_blue2.png"), 1.1).convert_alpha()

purple_formula = res(pygame.image.load("../images/cars/formula/formula_purple.png"), 1.1).convert_alpha()
purple_formula_2 = res(pygame.image.load("../images/cars/formula/formula_purple2.png"), 1.1).convert_alpha()

orange_formula = res(pygame.image.load("../images/cars/formula/formula_orange.png"), 1.1).convert_alpha()
orange_formula_2 = res(pygame.image.load("../images/cars/formula/formula_orange_2.png"), 1.1).convert_alpha()

yellow_formula = res(pygame.image.load("../images/cars/formula/formula_yellow.png"), 1.1).convert_alpha()
yellow_formula_2 = res(pygame.image.load("../images/cars/formula/formula_yellow_2.png"), 1.1).convert_alpha()

green_formula = res(pygame.image.load("../images/cars/formula/formula_green.png"), 1.1).convert_alpha()
green_formula_2 = res(pygame.image.load("../images/cars/formula/formula_green_2.png"), 1.1).convert_alpha()

red_formula = res(pygame.image.load("../images/cars/formula/formula_red.png"), 1.1).convert_alpha()

# lambo
blue_lambo = res(pygame.image.load("../images/cars/lamborghini/lambo_blue.png"), 0.85).convert_alpha()
cyan_lambo = res(pygame.image.load("../images/cars/lamborghini/lambo_cyan.png"), 0.85).convert_alpha()
red_lambo = res(pygame.image.load("../images/cars/lamborghini/lambo_red.png"), 0.85).convert_alpha()
pink_lambo = res(pygame.image.load("../images/cars/lamborghini/lambo_pink.png"), 0.85).convert_alpha()

# spoiler car
dark_purple_spoiler_car = res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_dark_purple.png"),
                              0.85).convert_alpha()

#dark_purple_spoiler_car = res(pygame.image.load("../images/cars/spoiler_car/special_car3.png"),
                              #0.85).convert_alpha()

light_blue_spoiler_car = res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_light_blue.png"),
                             0.85).convert_alpha()
orange_spoiler_car = res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_orange.png"), 0.85).convert_alpha()
pink_spoiler_car = res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_pink.png"), 0.85).convert_alpha()

# cabrio car
blue_cabrio = res(pygame.image.load("../images/cars/cabrio/cabrio_blue.png"), 0.85).convert_alpha()
light_blue_cabrio = res(pygame.image.load("../images/cars/cabrio/cabrio_light_blue.png"), 0.85).convert_alpha()
red_cabrio = res(pygame.image.load("../images/cars/cabrio/cabrio_red.png"), 0.85).convert_alpha()
yellow_cabrio = res(pygame.image.load("../images/cars/cabrio/cabrio_yellow.png"), 0.85).convert_alpha()

# menu backgrounds
f_background = res(pygame.image.load("../images/backgrounds/futuristic_bg.png"), 0.5).convert_alpha()
f_light_background = res(pygame.image.load("../images/backgrounds/futuristic_light_bg.png"), 0.5).convert_alpha()

# map backgrounds
green_forest = res(pygame.image.load("../images/backgrounds/green_forest.png"), 0.75).convert_alpha()
dark_green_forest = res(pygame.image.load("../images/backgrounds/dark_green_forest.png"), 0.75).convert_alpha()
green_lake_forest = res(pygame.image.load("../images/backgrounds/green_lake_forest2.png"), 0.75).convert_alpha()
green_lake_forest2 = res(pygame.image.load("../images/backgrounds/green_lake_forest3.png"), 0.75).convert_alpha()
dark_green_lake_forest = res(pygame.image.load("../images/backgrounds/dark_green_lake_forest.png"), 0.75).convert_alpha()

# finish
finish_line = res(pygame.image.load("../images/borders/finish_line.png"), 1.2).convert_alpha()
finish_line_x2 = res(pygame.image.load("../images/borders/finish_line.png"), 1.35).convert_alpha()
finish_line_x3 = res(pygame.image.load("../images/borders/finish_line.png"), 1.7).convert_alpha()

# buttons
button_transparent_image = res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1).convert_alpha()
button_play_transparent_image = res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1.3).convert_alpha()
button_win_lose = res(pygame.image.load("../images/ui/buttons/button_win_lose.png"), 1.5).convert_alpha()
button_image = res(pygame.image.load("../images/ui/buttons/button.png"), 1).convert_alpha()
pointer_right = res(pygame.image.load("../images/ui/buttons/pointer_right.png"), 1).convert_alpha()
pointer_left = res(pygame.image.load("../images/ui/buttons/pointer_left.png"), 1).convert_alpha()

on_off_button = res(pygame.image.load("../images/ui/buttons/on_off_button.png"), 1).convert_alpha()
on_off_button_x2 = res(pygame.image.load("../images/ui/buttons/on_off_button.png"), 2).convert_alpha()

# map selection buttons
first_map_image = res(pygame.image.load("../images/ui/buttons/first_map_button.png"), 0.15).convert_alpha()
second_map_image = res(pygame.image.load("../images/ui/buttons/second_map_button.png"), 0.15).convert_alpha()
third_map_image = res(pygame.image.load("../images/ui/buttons/third_map_button.png"), 0.15).convert_alpha()
fourth_map_image = res(pygame.image.load("../images/maps/fourth_map.png"), 0.15).convert_alpha()
fifth_map_image = res(pygame.image.load("../images/maps/fifth_map.png"), 0.15).convert_alpha()

# map loading
first_map_loading = res(pygame.image.load("../images/ui/buttons/first_map_button.png"), 0.3).convert_alpha()
second_map_loading = res(pygame.image.load("../images/ui/buttons/second_map_button.png"), 0.3).convert_alpha()
third_map_loading = res(pygame.image.load("../images/ui/buttons/third_map_button.png"), 0.3).convert_alpha()
fourth_map_loading = res(pygame.image.load("../images/maps/fourth_map.png"), 0.3).convert_alpha()
fifth_map_loading = res(pygame.image.load("../images/maps/fifth_map.png"), 0.3).convert_alpha()

# banners
esc_menu = res(pygame.image.load("../images/ui/esc_menu.png"), 1).convert_alpha()
time_menu = res(pygame.image.load("../images/ui/time_menu.png"), 1).convert_alpha()
time_background = res(pygame.image.load("../images/backgrounds/time_background.png"), 1).convert_alpha()
time_background2 = res(pygame.image.load("../images/backgrounds/time_background3.png"),
                       1).convert_alpha()

# semaphor
semaphor_all_red = res(pygame.image.load("../images/ui/semaphor/semaphor_all_red.png"), 1).convert_alpha()
semaphor_red = res(pygame.image.load("../images/ui/semaphor/semaphor_red.png"), 1).convert_alpha()
semaphor_orange = res(pygame.image.load("../images/ui/semaphor/semaphor_orange.png"), 1).convert_alpha()
semaphor_green = res(pygame.image.load("../images/ui/semaphor/semaphor_green.png"), 1).convert_alpha()

# speedometr
speedometr = res(pygame.image.load("../images/ui/speedometr/speedometr_default.png"), 0.5).convert_alpha()
speedometr_0 = res(pygame.image.load("../images/ui/speedometr/speedometr_0.png"), 0.5).convert_alpha()
speedometr_1 = res(pygame.image.load("../images/ui/speedometr/speedometr_1.png"), 0.5).convert_alpha()
speedometr_2 = res(pygame.image.load("../images/ui/speedometr/speedometr_2.png"), 0.5).convert_alpha()
speedometr_3 = res(pygame.image.load("../images/ui/speedometr/speedometr_3.png"), 0.5).convert_alpha()
speedometr_nitro = res(pygame.image.load("../images/ui/speedometr/speedometr_nitro.png"), 0.5).convert_alpha()

# nitro
nitro_empty = res(pygame.image.load("../images/ui/nitro/nitro_empty.png"), 0.3).convert_alpha()
nitro_0 = res(pygame.image.load("../images/ui/nitro/nitro_0.png"), 0.3).convert_alpha()
nitro_1 = res(pygame.image.load("../images/ui/nitro/nitro_1.png"), 0.3).convert_alpha()
nitro_2 = res(pygame.image.load("../images/ui/nitro/nitro_2.png"), 0.3).convert_alpha()
nitro_3 = res(pygame.image.load("../images/ui/nitro/nitro_3.png"), 0.3).convert_alpha()
nitro_4 = res(pygame.image.load("../images/ui/nitro/nitro_4.png"), 0.3).convert_alpha()
nitro_5 = res(pygame.image.load("../images/ui/nitro/nitro_5.png"), 0.3).convert_alpha()

formula_selection = res(pygame.image.load("../images/ui/selections/formula_selection.png"), 2).convert_alpha()
lambo_selection = res(pygame.image.load("../images/ui/selections/lambo_selection.png"), 2).convert_alpha()
spoiler_car_selection = res(pygame.image.load("../images/ui/selections/spoiler_car_selection.png"), 2).convert_alpha()
cabrio_selection = res(pygame.image.load("../images/ui/selections/cabrio_selection.png"), 2).convert_alpha()

blue_formula_selection = res(pygame.image.load("../images/ui/selections/formula_selection_blue.png"), 2).convert_alpha()
orange_formula_selection = res(pygame.image.load("../images/ui/selections/formula_selection_orange.png"),
                               2).convert_alpha()
yellow_formula_selection = res(pygame.image.load("../images/ui/selections/formula_selection_yellow.png"),
                               2).convert_alpha()
green_formula_selection = res(pygame.image.load("../images/ui/selections/formula_selection_green.png"),
                              2).convert_alpha()

blue_lambo_selection = res(pygame.image.load("../images/ui/selections/lambo_selection_blue.png"), 2).convert_alpha()
cyan_lambo_selection = res(pygame.image.load("../images/ui/selections/lambo_selection_cyan.png"), 2).convert_alpha()
red_lambo_selection = res(pygame.image.load("../images/ui/selections/lambo_selection_red.png"), 2).convert_alpha()
pink_lambo_selection = res(pygame.image.load("../images/ui/selections/lambo_selection_pink.png"), 2).convert_alpha()

dark_purple_spoiler_car_selection = res(pygame.image.load("../images/ui/selections/spoiler_car_selection_dark_purple.png"), 2).convert_alpha()
light_blue_spoiler_car_selection = res(pygame.image.load("../images/ui/selections/spoiler_car_selection_light_blue.png"), 2).convert_alpha()
orange_spoiler_car_selection = res(pygame.image.load("../images/ui/selections/spoiler_car_selection_orange.png"), 2).convert_alpha()
pink_spoiler_car_selection = res(pygame.image.load("../images/ui/selections/spoiler_car_selection_pink.png"), 2).convert_alpha()

blue_cabrio_selection = res(pygame.image.load("../images/ui/selections/cabrio_blue_selection.png"), 2).convert_alpha()
light_blue_cabrio_selection = res(pygame.image.load("../images/ui/selections/cabrio_light_blue_selection.png"), 2).convert_alpha()
red_cabrio_selection = res(pygame.image.load("../images/ui/selections/cabrio_red_selection.png"), 2).convert_alpha()
yellow_cabrio_selection = res(pygame.image.load("../images/ui/selections/cabrio_yellow_selection.png"), 2).convert_alpha()


settings_button_icon = res(pygame.image.load("../images/ui/buttons/settings_button.png"), 0.1).convert_alpha()
binds_button_icon = res(pygame.image.load("../images/ui/buttons/binds_button.png"), 0.15).convert_alpha()

# icon
icon_formula = pygame.image.load("../images/icons/streaming.png").convert_alpha()
pygame.display.set_icon(icon_formula)

# fonts
normal_font = pygame.font.SysFont("impact", 60)
small_font = pygame.font.SysFont("impact", 20)
big_font = pygame.font.SysFont("impact", 100)
medium_font = pygame.font.SysFont("impact", 35)
