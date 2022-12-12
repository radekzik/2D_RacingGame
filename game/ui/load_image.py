import pygame
from game.ui.resolution import res

pygame.init()

width = 1920
height = 1080
flags = pygame.HWSURFACE | pygame.FULLSCREEN
game_screen = pygame.display.set_mode((width, height), flags, vsync=1)

first_map = res(pygame.image.load("../images/maps/first_map2.png"), 0.75).convert_alpha()
first_map_border = res(pygame.image.load("../images/borders/first_map_border3.png"), 0.75).convert_alpha()

second_map = res(pygame.image.load("../images/maps/second_map.png"), 0.75).convert_alpha()
second_map_border = res(pygame.image.load("../images/borders/second_map_border2.png"), 0.75).convert_alpha()

third_map = res(pygame.image.load("../images/maps/third_map.png"), 0.75).convert_alpha()
third_map_border = res(pygame.image.load("../images/borders/third_map_border.png"), 0.75).convert_alpha()

blue_formula = res(pygame.image.load("../images/cars/formula_blue.png"), 1.1).convert_alpha()
blue_formula_2 = res(pygame.image.load("../images/cars/formula_blue2.png"), 1.1).convert_alpha()

purple_formula = res(pygame.image.load("../images/cars/formula_purple.png"), 1.1).convert_alpha()
purple_formula_2 = res(pygame.image.load("../images/cars/formula_purple2.png"), 1.1).convert_alpha()

red_formula = res(pygame.image.load("../images/cars/formula_red.png"), 1.1).convert_alpha()

blue_lambo = res(pygame.image.load("../images/cars/blue_lambo.png"), 0.85).convert_alpha()
pink_lambo = res(pygame.image.load("../images/cars/pink_lambo.png"), 0.85).convert_alpha()

menu_background = res(pygame.image.load("../images/backgrounds/blue_grey_gradient.jpg"), 1).convert_alpha()
finish_line = res(pygame.image.load("../images/borders/finish_line.png"), 1.2).convert_alpha()
button_image = res(pygame.image.load("../images/ui/button.png"), 1).convert_alpha()

first_map_image = res(pygame.image.load("../images/ui/first_map_button.png"), 0.27).convert_alpha()
second_map_image = res(pygame.image.load("../images/ui/second_map_button.png"), 0.27).convert_alpha()

esc_menu = res(pygame.image.load("../images/ui/esc_menu.png"), 1).convert_alpha()
time_menu = res(pygame.image.load("../images/ui/time_menu.png"), 1).convert_alpha()
car_selection_menu = res(pygame.image.load("../images/backgrounds/car_selection_background.png"), 1.5).convert_alpha()

semaphor_all_red = res(pygame.image.load("../images/ui/semaphor_all_red.png"), 1)
semaphor_red = res(pygame.image.load("../images/ui/semaphor_red.png"), 1)
semaphor_orange = res(pygame.image.load("../images/ui/semaphor_orange.png"), 1)
semaphor_green = res(pygame.image.load("../images/ui/semaphor_green.png"), 1)

formula_selection = res(pygame.image.load("../images/ui/blue_formula_selection.png"), 2).convert_alpha()
lambo_selection = res(pygame.image.load("../images/ui/blue_lambo_selection.png"), 2).convert_alpha()

f_background = res(pygame.image.load("../images/backgrounds/futuristic_bg.png"), 0.5).convert_alpha()

green_background = res(pygame.image.load("../images/backgrounds/green_bg.png"), 0.75).convert_alpha()

icon_formula = pygame.image.load("../images/icons/streaming.png").convert_alpha()
pygame.display.set_icon(icon_formula)


normal_font = pygame.font.SysFont("impact", 60)
small_font = pygame.font.SysFont("impact", 20)
big_font = pygame.font.SysFont("impact", 100)
medium_font = pygame.font.SysFont("impact", 35)
