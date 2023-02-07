import pygame

from racing_game.config.settings import Settings

pygame.init()


class LoadingImages:
    WIDTH = 1920
    HEIGHT = 1080
    FLAGS = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
    GAME_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, 16, vsync=Settings.vsync)

    @staticmethod
    def res(image, amount):
        new_res = (image.get_width() * amount), (image.get_height() * amount)

        return pygame.transform.scale(image, new_res)

    @staticmethod
    def res_width(image, amount):
        new_res = (image.get_width() * amount)

        return pygame.transform.scale(image, new_res)

    @staticmethod
    def res_height(image, amount):
        new_res = (image.get_height() * amount)

        return pygame.transform.scale(image, new_res)

    # MAPS -----------------------------------------------------------------------------------------------------------------

    MAPS = {
        1: {"MAP": res(pygame.image.load("../images/maps/first_map.png"), 0.75).convert_alpha(),
            "BORDER": res(pygame.image.load("../images/borders/first_map_border.png"), 0.75).convert_alpha()},

        2: {"MAP": res(pygame.image.load("../images/maps/second_map.png"), 0.75).convert_alpha(),
            "BORDER": res(pygame.image.load("../images/borders/second_map_border.png"), 0.75).convert_alpha()},

        3: {"MAP": res(pygame.image.load("../images/maps/third_map.png"), 0.75).convert_alpha(),
            "BORDER": res(pygame.image.load("../images/borders/third_map_border.png"), 0.75).convert_alpha()},

        4: {"MAP": res(pygame.image.load("../images/maps/fourth_map.png"), 0.75).convert_alpha(),
            "BORDER": res(pygame.image.load("../images/borders/fourth_map_border.png"), 0.75).convert_alpha()},

        5: {"MAP": res(pygame.image.load("../images/maps/fifth_map.png"), 0.75).convert_alpha(),
            "BORDER": res(pygame.image.load("../images/borders/fifth_map_border.png"), 0.75).convert_alpha()}
    }

    MAP_SELECTION = {

        1: {"MAP": res(pygame.image.load("../images/ui/buttons/first_map_button.png"), 0.15).convert_alpha()},
        2: {"MAP": res(pygame.image.load("../images/ui/buttons/second_map_button.png"), 0.15).convert_alpha()},
        3: {"MAP": res(pygame.image.load("../images/ui/buttons/third_map_button.png"), 0.15).convert_alpha()},
        4: {"MAP": res(pygame.image.load("../images/maps/fourth_map.png"), 0.15).convert_alpha()},
        5: {"MAP": res(pygame.image.load("../images/maps/fifth_map.png"), 0.15).convert_alpha()}

    }

    MAP_LOADING = {

        1: {"MAP": res(pygame.image.load("../images/ui/buttons/first_map_button.png"), 0.3).convert_alpha()},
        2: {"MAP": res(pygame.image.load("../images/ui/buttons/second_map_button.png"), 0.3).convert_alpha()},
        3: {"MAP": res(pygame.image.load("../images/ui/buttons/third_map_button.png"), 0.3).convert_alpha()},
        4: {"MAP": res(pygame.image.load("../images/maps/fourth_map.png"), 0.3).convert_alpha()},
        5: {"MAP": res(pygame.image.load("../images/maps/fifth_map.png"), 0.3).convert_alpha()}

    }

    # CARS -----------------------------------------------------------------------------------------------------------------

    FORMULA = {
        1: {"CAR": res(pygame.image.load("../images/cars/formula/formula_blue.png"), 1.1).convert_alpha(),
            "CAR-2": res(pygame.image.load("../images/cars/formula/formula_blue2.png"), 1.1).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/cars/formula/formula_purple.png"), 1.1).convert_alpha(),
            "CAR-2": res(pygame.image.load("../images/cars/formula/formula_purple2.png"), 1.1).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/cars/formula/formula_orange.png"), 1.1).convert_alpha(),
            "CAR-2": res(pygame.image.load("../images/cars/formula/formula_orange_2.png"), 1.1).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/cars/formula/formula_yellow.png"), 1.1).convert_alpha(),
            "CAR-2": res(pygame.image.load("../images/cars/formula/formula_yellow_2.png"), 1.1).convert_alpha()},

        5: {"CAR": res(pygame.image.load("../images/cars/formula/formula_green.png"), 1.1).convert_alpha(),
            "CAR-2": res(pygame.image.load("../images/cars/formula/formula_green_2.png"), 1.1).convert_alpha()},

        6: {"CAR": res(pygame.image.load("../images/cars/formula/formula_red.png"), 1.1).convert_alpha()}

    }

    SPORTS_CAR_I = {

        1: {"CAR": res(pygame.image.load("../images/cars/lamborghini/lambo_blue.png"), 0.85).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/cars/lamborghini/lambo_cyan.png"), 0.85).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/cars/lamborghini/lambo_red.png"), 0.85).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/cars/lamborghini/lambo_pink.png"), 0.85).convert_alpha()},

    }

    SPORTS_CAR_II = {

        1: {"CAR": res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_dark_purple.png"),
                       0.85).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_light_blue.png"),
                       0.85).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_orange.png"), 0.85).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/cars/spoiler_car/spoiler_car_pink.png"), 0.85).convert_alpha()},

    }

    CABRIO = {

        1: {"CAR": res(pygame.image.load("../images/cars/cabrio/cabrio_blue.png"), 0.85).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/cars/cabrio/cabrio_light_blue.png"), 0.85).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/cars/cabrio/cabrio_red.png"), 0.85).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/cars/cabrio/cabrio_yellow.png"), 0.85).convert_alpha()},

    }

    # BACKGROUNDS -----------------------------------------------------------------------------------------------------------------

    MENU_BACKGROUND = {

        1: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/futuristic_bg.png"), 0.5).convert_alpha()},

        2: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/futuristic_light_bg.png"), 0.5).convert_alpha()}

    }

    MAP_BACKGROUND = {

        1: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/green_forest.png"), 0.75).convert_alpha()},

        2: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/dark_green_forest.png"), 0.75).convert_alpha()},

    }

    MAP_BACKGROUND_LAKE = {

        1: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/green_lake_forest2.png"), 0.75).convert_alpha()},

        2: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/green_lake_forest3.png"), 0.75).convert_alpha()},

        3: {"BACKGROUND": res(pygame.image.load("../images/backgrounds/dark_green_lake_forest.png"),
                              0.75).convert_alpha()},

    }

    # FINISH LINES  -----------------------------------------------------------------------------------------------------------------

    FINISH_LINE = {

        1: {"FINISH_LINE": res(pygame.image.load("../images/borders/finish_line.png"), 1.2).convert_alpha()},
        2: {"FINISH_LINE": res(pygame.image.load("../images/borders/finish_line.png"), 1.35).convert_alpha()},
        3: {"FINISH_LINE": res(pygame.image.load("../images/borders/finish_line.png"), 1.7).convert_alpha()}

    }

    # BUTTONS ---------------------------------------------------------------------------------------------------------------

    BUTTONS = {

        1: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1).convert_alpha()},
        2: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_transparent.png"), 1.3).convert_alpha()},

        3: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button.png"), 1).convert_alpha()},
        4: {"BUTTON": res(pygame.image.load("../images/ui/buttons/button_win_lose.png"), 1.5).convert_alpha()},

        5: {"BUTTON": res(pygame.image.load("../images/ui/buttons/settings_button.png"), 0.1).convert_alpha()},
        6: {"BUTTON": res(pygame.image.load("../images/ui/buttons/binds_button.png"), 0.15).convert_alpha()}

    }

    POINTERS = {

        1: {"POINTER": res(pygame.image.load("../images/ui/buttons/pointer_left.png"), 1).convert_alpha()},
        2: {"POINTER": res(pygame.image.load("../images/ui/buttons/pointer_right.png"), 1).convert_alpha()}

    }

    ON_OFF_BUTTONS = {

        1: {"BUTTON": res(pygame.image.load("../images/ui/buttons/on_off_button.png"), 1).convert_alpha()},
        2: {"BUTTON": res(pygame.image.load("../images/ui/buttons/on_off_button.png"), 2).convert_alpha()}

    }

    TIME_TABLES = {

        1: {"TABLE": res(pygame.image.load("../images/backgrounds/time_background.png"), 1).convert_alpha()},
        2: {"TABLE": res(pygame.image.load("../images/backgrounds/time_background3.png"), 1).convert_alpha()}

    }

    SEMAPHORE = {

        1: {"SEMAPHORE": res(pygame.image.load("../images/ui/semaphor/semaphor_all_red.png"), 1).convert_alpha()},
        2: {"SEMAPHORE": res(pygame.image.load("../images/ui/semaphor/semaphor_red.png"), 1).convert_alpha()},
        3: {"SEMAPHORE": res(pygame.image.load("../images/ui/semaphor/semaphor_orange.png"), 1).convert_alpha()},
        4: {"SEMAPHORE": res(pygame.image.load("../images/ui/semaphor/semaphor_green.png"), 1).convert_alpha()}

    }

    SPEEDOMETR = {

        1: {"SPEEDOMETR": res(pygame.image.load("../images/ui/speedometr/speedometr_default.png"),
                              0.5).convert_alpha()},
        2: {"SPEEDOMETR": res(pygame.image.load("../images/ui/speedometr/speedometr_0.png"), 0.5).convert_alpha()},
        3: {"SPEEDOMETR": res(pygame.image.load("../images/ui/speedometr/speedometr_1.png"), 0.5).convert_alpha()},
        4: {"SPEEDOMETR": res(pygame.image.load("../images/ui/speedometr/speedometr_2.png"), 0.5).convert_alpha()},
        5: {"SPEEDOMETR": res(pygame.image.load("../images/ui/speedometr/speedometr_3.png"), 0.5).convert_alpha()},
        6: {"SPEEDOMETR": res(pygame.image.load("../images/ui/speedometr/speedometr_nitro.png"), 0.5).convert_alpha()}

    }

    NITRO = {

        1: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_empty.png"), 0.3).convert_alpha()},
        2: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_0.png"), 0.3).convert_alpha()},
        3: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_1.png"), 0.3).convert_alpha()},
        4: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_2.png"), 0.3).convert_alpha()},
        5: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_3.png"), 0.3).convert_alpha()},
        6: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_4.png"), 0.3).convert_alpha()},
        7: {"NITRO": res(pygame.image.load("../images/ui/nitro/nitro_5.png"), 0.3).convert_alpha()}

    }

    # CAR SELECTIONS -----------------------------------------------------------------------------------------------------------------

    CAR_SELECTION = {

        1: {"CAR": res(pygame.image.load("../images/ui/selections/formula_selection.png"), 2).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/ui/selections/lambo_selection.png"), 2).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/ui/selections/spoiler_car_selection.png"), 2).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/ui/selections/cabrio_selection.png"), 2).convert_alpha()}

    }

    FORMULA_SELECTION = {

        1: {"CAR": res(pygame.image.load("../images/ui/selections/formula_selection_blue.png"), 2).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/ui/selections/formula_selection_orange.png"), 2).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/ui/selections/formula_selection_yellow.png"), 2).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/ui/selections/formula_selection_green.png"), 2).convert_alpha()}

    }

    SPORTS_CAR_I_SELECTION = {

        1: {"CAR": res(pygame.image.load("../images/ui/selections/lambo_selection_blue.png"), 2).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/ui/selections/lambo_selection_cyan.png"), 2).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/ui/selections/lambo_selection_red.png"), 2).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/ui/selections/lambo_selection_pink.png"), 2).convert_alpha()}

    }

    SPORTS_CAR_II_SELECTION = {

        1: {"CAR": res(pygame.image.load("../images/ui/selections/spoiler_car_selection_dark_purple.png"),
                       2).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/ui/selections/spoiler_car_selection_light_blue.png"),
                       2).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/ui/selections/spoiler_car_selection_orange.png"),
                       2).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/ui/selections/spoiler_car_selection_pink.png"), 2).convert_alpha()}

    }

    CABRIO_SELECTION = {

        1: {"CAR": res(pygame.image.load("../images/ui/selections/cabrio_blue_selection.png"),
                       2).convert_alpha()},

        2: {"CAR": res(pygame.image.load("../images/ui/selections/cabrio_light_blue_selection.png"),
                       2).convert_alpha()},

        3: {"CAR": res(pygame.image.load("../images/ui/selections/cabrio_red_selection.png"), 2).convert_alpha()},

        4: {"CAR": res(pygame.image.load("../images/ui/selections/cabrio_yellow_selection.png"),
                       2).convert_alpha()},

    }

    # ICON ----------------------------------------------------------------------------------------------------------------------
    trophy_icon = res(pygame.image.load("../images/icons/trophy-icon.png"), 0.15).convert_alpha()
    lock_icon = res(pygame.image.load("../images/icons/lock-icon.png"), 0.2).convert_alpha()
    icon_formula = pygame.image.load("../images/icons/streaming.png").convert_alpha()
    pygame.display.set_icon(icon_formula)

    # FONTS -----------------------------------------------------------------------------------------------------------------
    NORMAL_FONT = pygame.font.SysFont("impact", 60)
    SMALL_FONT = pygame.font.SysFont("impact", 20)
    BIG_FONT = pygame.font.SysFont("impact", 100)
    MEDIUM_FONT = pygame.font.SysFont("impact", 35)
