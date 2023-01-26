import pygame

from racing_game.config import settings
from racing_game.ui import loading_images
from racing_game.ui.loading_images import GAME_SCREEN, normal_font, small_font, time_background2, \
    medium_font, f_light_background
from racing_game.ui.resolution import draw_text


class DrawUI:

    @staticmethod
    def game_info(match_time, lap, stopwatch):
        draw_text(f"LAP TIME - {stopwatch}", small_font, "white", 1790, 20, GAME_SCREEN)
        draw_text(f"RACE TIME - {round(match_time)}", small_font, "cyan", 1790, 60, GAME_SCREEN)

        draw_text(f"LAP - {lap} / {settings.max_laps}", small_font, "cyan", 1777, 1040, GAME_SCREEN)

    @staticmethod
    def player_title():
        draw_text(f"FIRST PLAYER", medium_font, "light blue", 1595, 15, GAME_SCREEN)

    @staticmethod
    def enemy_game_info(match_time, lap, stopwatch):
        draw_text(f"LAP TIME - {stopwatch}", small_font, "white", 30, 20, GAME_SCREEN)
        draw_text(f"RACE TIME - {round(match_time)}", small_font, "cyan", 30, 60, GAME_SCREEN)

        draw_text(f"LAP - {lap} / {settings.max_laps}", small_font, "cyan", 73, 1040, GAME_SCREEN)

        DrawUI.enemy_title()

    @staticmethod
    def enemy_title():
        draw_text(f"SECOND PLAYER", medium_font, "red", 150, 15, GAME_SCREEN)

    @staticmethod
    def game_show_fps(clock):
        draw_text(f"FPS - {round(clock.get_fps())}", small_font, "cyan", 30, 20, GAME_SCREEN)

    @staticmethod
    def player_time_table(fastest_time, slowest_time, match_time):
        GAME_SCREEN.blit(time_background2, (700, 200))
        draw_text(f"FASTEST LAP TIME : {fastest_time}", normal_font, "green", 740, 250, GAME_SCREEN)
        draw_text(f"SLOWEST LAP TIME : {slowest_time}", normal_font, "red", 740, 350, GAME_SCREEN)
        draw_text(f"MATCH TIME : {round(match_time)}", normal_font, "white", 740, 450, GAME_SCREEN)

    @staticmethod
    def enemy_time_table(fastest_time, slowest_time, match_time):
        GAME_SCREEN.blit(time_background2, (700, 200))
        draw_text(f"FASTEST LAP TIME : {fastest_time}", normal_font, "green", 740, 250, GAME_SCREEN)
        draw_text(f"SLOWEST LAP TIME : {slowest_time}", normal_font, "red", 740, 350, GAME_SCREEN)
        draw_text(f"MATCH TIME : {round(match_time)}", normal_font, "white", 740, 450, GAME_SCREEN)

    @staticmethod
    def speedometer(car, x, y):
        speedometr_position = x, y

        if car.car_speed < 0:
            GAME_SCREEN.blit(loading_images.speedometr, speedometr_position)
        if car.car_speed == 0:
            GAME_SCREEN.blit(loading_images.speedometr_0, speedometr_position)
        if 0 < car.car_speed <= 1:
            GAME_SCREEN.blit(loading_images.speedometr_1, speedometr_position)
        if 1 < car.car_speed <= 2:
            GAME_SCREEN.blit(loading_images.speedometr_2, speedometr_position)
        if 2 < car.car_speed <= 3:
            GAME_SCREEN.blit(loading_images.speedometr_3, speedometr_position)
        if 3 < car.car_speed <= 10:
            GAME_SCREEN.blit(loading_images.speedometr_nitro, speedometr_position)

    @staticmethod
    def nitro(car, x, y):
        nitro_position = x, y

        if car.car_nitro < 0:
            GAME_SCREEN.blit(loading_images.nitro_0, nitro_position)
        if car.car_nitro == 0:
            GAME_SCREEN.blit(loading_images.nitro_empty, nitro_position)
        if 0 < car.car_nitro <= 2:
            GAME_SCREEN.blit(loading_images.nitro_1, nitro_position)
        if 2 < car.car_nitro <= 4:
            GAME_SCREEN.blit(loading_images.nitro_2, nitro_position)
        if 4 < car.car_nitro <= 6:
            GAME_SCREEN.blit(loading_images.nitro_3, nitro_position)
        if 6 < car.car_nitro <= 8:
            GAME_SCREEN.blit(loading_images.nitro_4, nitro_position)
        if 8 < car.car_nitro <= 15:
            GAME_SCREEN.blit(loading_images.nitro_5, nitro_position)

    @staticmethod
    def restarting_game():
        loading = 1

        while loading:
            GAME_SCREEN.blit(f_light_background, (0, 0))
            draw_text("Restarting Game.", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Restarting Game..", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Restarting Game...", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)
            loading = False

    @staticmethod
    def loading_game(title, game_mode, map_title, map_image):
        loading = 1

        while loading:
            GAME_SCREEN.blit(f_light_background, (0, 0))

            draw_text(title + " Game.", normal_font, "white", 780, 130, GAME_SCREEN)
            DrawUI.loading_text(game_mode, map_title, map_image)

            draw_text(title + " Game..", normal_font, "white", 780, 130, GAME_SCREEN)
            DrawUI.loading_text(game_mode, map_title, map_image)

            draw_text(title + " Game...", normal_font, "white", 780, 130, GAME_SCREEN)
            DrawUI.loading_text(game_mode, map_title, map_image)

            loading = False

    @staticmethod
    def loading_text(game_mode, map_title, map_image):
        draw_text(game_mode, normal_font, "cyan", 810, 230, GAME_SCREEN)
        draw_text(map_title, normal_font, "purple", 970, 230, GAME_SCREEN)
        GAME_SCREEN.blit(map_image, (600, 450))
        pygame.display.update()
        pygame.time.wait(500)

    @staticmethod
    def check_car_type(car):
        for x in range(16):
            x += 1
            if settings.car_type == x:
                car.car_image = car.player_cars(x - 1)

    @staticmethod
    def check_show_fps(command, clock):
        if settings.show_fps == 1:
            command(clock)

    @staticmethod
    def check_show_xy(command):
        if settings.show_xy == 1:
            command()

    @staticmethod
    def check_audio(command):
        if settings.audio == 1:
            command()

    @staticmethod
    def check_audio_set_volume(command, volume):
        if settings.audio == 1:
            command(volume)

    @staticmethod
    def check_fadeout_audio(command, time):
        if settings.audio == 1:
            command(time)

    @staticmethod
    def check_show_ui(command, player_car, car_stopwatch):
        if settings.show_ui == 1:
            command(player_car, car_stopwatch)

    @staticmethod
    def ui(player_car, car_stopwatch):
        DrawUI.game_info(settings.car_match_time, settings.car_lap, car_stopwatch)

        DrawUI.speedometer(player_car, 1730, 900)
        player_car.car_current_speed()

        DrawUI.nitro(player_car, 1690, 970)
        # player_car.car_current_nitro()

    @staticmethod
    def enemy_ui(enemy_car, enemy_stopwatch):
        DrawUI.enemy_game_info(settings.enemy_match_time, settings.enemy_lap, enemy_stopwatch)

        DrawUI.speedometer(enemy_car, 30, 900)
        enemy_car.car_current_speed()

        DrawUI.nitro(enemy_car, 200, 970)
        # player_car.car_current_nitro()

    @staticmethod
    def car_stopwatch(ticks):
        stopwatch = ticks - settings.car_start_time
        stopwatch = stopwatch // 100 / 10

        return stopwatch

    @staticmethod
    def enemy_stopwatch(ticks):
        stopwatch = ticks - settings.enemy_start_time
        stopwatch = stopwatch // 100 / 10

        return stopwatch

    @staticmethod
    def animation(stopwatch, car, first_image, second_image):
        if stopwatch % 2 == 0:
            car.car_image = first_image
            car.render_position(GAME_SCREEN)
            pygame.display.update()

        if stopwatch % 3 == 0:
            car.car_image = second_image
            car.render_position(GAME_SCREEN)
            pygame.display.update()

    @staticmethod
    def second_animation(stopwatch, enemy, first_image, second_image):
        if stopwatch % 3 == 0:
            enemy.car_image = second_image
            enemy.render_position(GAME_SCREEN)
            pygame.display.update()

        if stopwatch % 2 == 0:
            enemy.car_image = first_image
            enemy.render_position(GAME_SCREEN)
            pygame.display.update()

    @staticmethod
    def car_animation(stopwatch, car):
        if settings.car_type == 1:
            DrawUI.animation(stopwatch, car, loading_images.blue_formula, loading_images.blue_formula_2)

        if settings.car_type == 2:
            DrawUI.animation(stopwatch, car, loading_images.orange_formula, loading_images.orange_formula_2)

        if settings.car_type == 3:
            DrawUI.animation(stopwatch, car, loading_images.yellow_formula, loading_images.yellow_formula_2)

        if settings.car_type == 4:
            DrawUI.animation(stopwatch, car, loading_images.green_formula, loading_images.green_formula_2)

    @staticmethod
    def enemy_animation(stopwatch, enemy):
        if settings.enemy_car_type == 1:
            DrawUI.second_animation(stopwatch, enemy, loading_images.purple_formula, loading_images.purple_formula_2)

        if settings.enemy_car_type == 2:
            DrawUI.second_animation(stopwatch, enemy, loading_images.orange_formula, loading_images.orange_formula_2)

        if settings.enemy_car_type == 3:
            DrawUI.second_animation(stopwatch, enemy, loading_images.yellow_formula, loading_images.yellow_formula_2)

        if settings.enemy_car_type == 4:
            DrawUI.second_animation(stopwatch, enemy, loading_images.green_formula, loading_images.green_formula_2)
