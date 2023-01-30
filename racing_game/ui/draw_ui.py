import random

import pygame

from racing_game.config.settings import Settings
from racing_game.ui.loading_images import LoadingImages


class DrawUI:

    @staticmethod
    def random_all_maps_background():
        global background

        random_number = random.randint(1, 5)

        map_background_list = [LoadingImages.green_forest, LoadingImages.green_lake_forest,
                               LoadingImages.green_lake_forest2, LoadingImages.dark_green_forest,
                               LoadingImages.dark_green_lake_forest]

        for x in range(5):
            x += 1
            if random_number == x:
                background = map_background_list[x - 1]

        return background

    @staticmethod
    def random_selected_map_background():
        global background

        random_number = random.randint(1, 2)

        map_background_list = [LoadingImages.green_forest, LoadingImages.dark_green_forest]

        for x in range(2):
            x += 1
            if random_number == x:
                background = map_background_list[x - 1]

        return background

    @staticmethod
    def draw_text(text, font, color, x, y, game_window):
        set_font = font.render(text, True, color)
        game_window.blit(set_font, (x, y))

    @staticmethod
    def game_info(match_time, lap, stopwatch):
        DrawUI.draw_text(f"LAP TIME - {stopwatch}", LoadingImages.small_font, "white", 1790, 20, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"RACE TIME - {round(match_time)}", LoadingImages.small_font, "cyan", 1790, 60, LoadingImages.GAME_SCREEN)

        DrawUI.draw_text(f"LAP - {lap} / {Settings.max_laps}", LoadingImages.small_font, "cyan", 1777, 1040, LoadingImages.GAME_SCREEN)

    @staticmethod
    def player_title():
        DrawUI.draw_text(f"FIRST PLAYER", LoadingImages.medium_font, "light blue", 1595, 15, LoadingImages.GAME_SCREEN)

    @staticmethod
    def enemy_game_info(match_time, lap, stopwatch):
        DrawUI.draw_text(f"LAP TIME - {stopwatch}", LoadingImages.small_font, "white", 30, 20, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"RACE TIME - {round(match_time)}", LoadingImages.small_font, "cyan", 30, 60, LoadingImages.GAME_SCREEN)

        DrawUI.draw_text(f"LAP - {lap} / {Settings.max_laps}", LoadingImages.small_font, "cyan", 73, 1040, LoadingImages.GAME_SCREEN)

        DrawUI.enemy_title()

    @staticmethod
    def enemy_title():
        DrawUI.draw_text(f"SECOND PLAYER", LoadingImages.medium_font, "red", 150, 15, LoadingImages.GAME_SCREEN)

    @staticmethod
    def game_show_fps(clock):
        DrawUI.draw_text(f"FPS - {round(clock.get_fps())}", LoadingImages.small_font, "cyan", 30, 20, LoadingImages.GAME_SCREEN)

    @staticmethod
    def player_time_table(fastest_time, slowest_time, match_time):

        LoadingImages.GAME_SCREEN.blit(LoadingImages.time_background2, (700, 200))
        DrawUI.draw_text(f"FASTEST LAP TIME : {fastest_time}", LoadingImages.normal_font, "green", 740, 250, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"SLOWEST LAP TIME : {slowest_time}", LoadingImages.normal_font, "red", 740, 350, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"MATCH TIME : {round(match_time)}", LoadingImages.normal_font, "white", 740, 450, LoadingImages.GAME_SCREEN)

    @staticmethod
    def enemy_time_table(fastest_time, slowest_time, match_time):

        LoadingImages.GAME_SCREEN.blit(LoadingImages.time_background2, (700, 200))
        DrawUI.draw_text(f"FASTEST LAP TIME : {fastest_time}", LoadingImages.normal_font, "green", 740, 250, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"SLOWEST LAP TIME : {slowest_time}", LoadingImages.normal_font, "red", 740, 350, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"MATCH TIME : {round(match_time)}", LoadingImages.normal_font, "white", 740, 450, LoadingImages.GAME_SCREEN)

    @staticmethod
    def speedometer(car, x, y):
        speedometr_position = x, y

        if car.car_speed < 0:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.speedometr, speedometr_position)
        if car.car_speed == 0:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.speedometr_0, speedometr_position)
        if 0 < car.car_speed <= 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.speedometr_1, speedometr_position)
        if 1 < car.car_speed <= 2:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.speedometr_2, speedometr_position)
        if 2 < car.car_speed <= 3:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.speedometr_3, speedometr_position)
        if 3 < car.car_speed <= 10:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.speedometr_nitro, speedometr_position)

    @staticmethod
    def nitro(car, x, y):
        nitro_position = x, y

        if car.car_nitro < 0:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_0, nitro_position)
        if car.car_nitro == 0:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_empty, nitro_position)
        if 0 < car.car_nitro <= 2:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_1, nitro_position)
        if 2 < car.car_nitro <= 4:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_2, nitro_position)
        if 4 < car.car_nitro <= 6:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_3, nitro_position)
        if 6 < car.car_nitro <= 8:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_4, nitro_position)
        if 8 < car.car_nitro <= 15:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.nitro_5, nitro_position)

    @staticmethod
    def restarting_game():
        loading = 1

        while loading:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[2]["BACKGROUND"], (0, 0))
            DrawUI.draw_text("Restarting Game.", LoadingImages.normal_font, "white", 780, 230, LoadingImages.GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            DrawUI.draw_text("Restarting Game..", LoadingImages.normal_font, "white", 780, 230, LoadingImages.GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            DrawUI.draw_text("Restarting Game...", LoadingImages.normal_font, "white", 780, 230, LoadingImages.GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)
            loading = False

    @staticmethod
    def loading_game(title, game_mode, map_title, map_image):
        loading = 1

        while loading:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[2]["BACKGROUND"], (0, 0))

            DrawUI.draw_text(title + " Game.", LoadingImages.normal_font, "white", 780, 130, LoadingImages.GAME_SCREEN)
            DrawUI.loading_text(game_mode, map_title, map_image)

            DrawUI.draw_text(title + " Game..", LoadingImages.normal_font, "white", 780, 130, LoadingImages.GAME_SCREEN)
            DrawUI.loading_text(game_mode, map_title, map_image)

            DrawUI.draw_text(title + " Game...", LoadingImages.normal_font, "white", 780, 130, LoadingImages.GAME_SCREEN)
            DrawUI.loading_text(game_mode, map_title, map_image)

            loading = False

    @staticmethod
    def loading_text(game_mode, map_title, map_image):

        DrawUI.draw_text(game_mode, LoadingImages.normal_font, "cyan", 810, 230, LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(map_title, LoadingImages.normal_font, "purple", 970, 230, LoadingImages.GAME_SCREEN)

        LoadingImages.GAME_SCREEN.blit(map_image, (600, 450))
        pygame.display.update()
        pygame.time.wait(500)

    @staticmethod
    def check_car_type(car):
        for x in range(16):
            x += 1
            if Settings.car_type == x:
                car.car_image = car.player_cars(x - 1)

    @staticmethod
    def check_show_fps(command, clock):
        if Settings.show_fps == 1:
            command(clock)

    @staticmethod
    def check_show_xy(command):
        if Settings.show_xy == 1:
            command()

    @staticmethod
    def check_audio(command):
        if Settings.audio == 1:
            command()

    @staticmethod
    def check_audio_set_volume(command, volume):
        if Settings.audio == 1:
            command(volume)

    @staticmethod
    def check_fadeout_audio(command, time):
        if Settings.audio == 1:
            command(time)

    @staticmethod
    def check_show_ui(command, player_car, car_stopwatch):
        if Settings.show_ui == 1:
            command(player_car, car_stopwatch)

    @staticmethod
    def ui(player_car, car_stopwatch):
        DrawUI.game_info(Settings.car_match_time, Settings.car_lap, car_stopwatch)

        DrawUI.speedometer(player_car, 1730, 900)
        player_car.car_current_speed()

        DrawUI.nitro(player_car, 1690, 970)
        # player_car.car_current_nitro()

    @staticmethod
    def enemy_ui(enemy_car, enemy_stopwatch):
        DrawUI.enemy_game_info(Settings.enemy_match_time, Settings.enemy_lap, enemy_stopwatch)

        DrawUI.speedometer(enemy_car, 30, 900)
        enemy_car.car_current_speed()

        DrawUI.nitro(enemy_car, 200, 970)
        # player_car.car_current_nitro()

    @staticmethod
    def car_stopwatch(ticks):
        stopwatch = ticks - Settings.car_start_time
        stopwatch = stopwatch // 100 / 10

        return stopwatch

    @staticmethod
    def enemy_stopwatch(ticks):
        stopwatch = ticks - Settings.enemy_start_time
        stopwatch = stopwatch // 100 / 10

        return stopwatch

    @staticmethod
    def animation(stopwatch, car, first_image, second_image):
        if stopwatch % 2 == 0:
            car.car_image = first_image
            car.render_position(LoadingImages.GAME_SCREEN)
            pygame.display.update()

        if stopwatch % 3 == 0:
            car.car_image = second_image
            car.render_position(LoadingImages.GAME_SCREEN)
            pygame.display.update()

    @staticmethod
    def second_animation(stopwatch, enemy, first_image, second_image):
        if stopwatch % 3 == 0:
            enemy.car_image = second_image
            enemy.render_position(LoadingImages.GAME_SCREEN)
            pygame.display.update()

        if stopwatch % 2 == 0:
            enemy.car_image = first_image
            enemy.render_position(LoadingImages.GAME_SCREEN)
            pygame.display.update()

    @staticmethod
    def car_animation(stopwatch, car):
        if Settings.car_type == 1:
            DrawUI.animation(stopwatch, car, LoadingImages.FORMULA[1]["CAR"], LoadingImages.FORMULA[1]["CAR-2"])

        if Settings.car_type == 2:
            DrawUI.animation(stopwatch, car,  LoadingImages.FORMULA[3]["CAR"], LoadingImages.FORMULA[3]["CAR-2"])

        if Settings.car_type == 3:
            DrawUI.animation(stopwatch, car,  LoadingImages.FORMULA[4]["CAR"], LoadingImages.FORMULA[4]["CAR-2"])

        if Settings.car_type == 4:
            DrawUI.animation(stopwatch, car,  LoadingImages.FORMULA[5]["CAR"], LoadingImages.FORMULA[5]["CAR-2"])

    @staticmethod
    def enemy_animation(stopwatch, enemy):
        if Settings.enemy_car_type == 1:
            DrawUI.second_animation(stopwatch, enemy, LoadingImages.FORMULA[1]["CAR"], LoadingImages.FORMULA[1]["CAR-2"])

        if Settings.enemy_car_type == 2:
            DrawUI.second_animation(stopwatch, enemy, LoadingImages.FORMULA[3]["CAR"], LoadingImages.FORMULA[3]["CAR-2"])

        if Settings.enemy_car_type == 3:
            DrawUI.second_animation(stopwatch, enemy, LoadingImages.FORMULA[4]["CAR"], LoadingImages.FORMULA[4]["CAR-2"])

        if Settings.enemy_car_type == 4:
            DrawUI.second_animation(stopwatch, enemy, LoadingImages.FORMULA[5]["CAR"], LoadingImages.FORMULA[5]["CAR-2"])
