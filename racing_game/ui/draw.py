import pygame

from racing_game.config import settings
from racing_game.ui.load_image import GAME_SCREEN, normal_font, small_font, purple_formula_2, purple_formula, \
    blue_formula_2, blue_formula, orange_formula, orange_formula_2, yellow_formula_2, yellow_formula, \
    green_formula, green_formula_2, time_background2, medium_font
from racing_game.ui.resolution import draw_text


def game_info(match_time, lap, stopwatch):
    draw_text(f"LAP TIME - {stopwatch}", small_font, "white", 1790, 20, GAME_SCREEN)
    draw_text(f"RACE TIME - {round(match_time)}", small_font, "cyan", 1790, 60, GAME_SCREEN)

    draw_text(f"LAP - {lap} / {settings.max_laps}", small_font, "cyan", 1777, 1040, GAME_SCREEN)


def player_title():
    draw_text(f"FIRST PLAYER", medium_font, "light blue", 1595, 15, GAME_SCREEN)


def enemy_game_info(match_time, lap, stopwatch):
    draw_text(f"LAP TIME - {stopwatch}", small_font, "white", 30, 20, GAME_SCREEN)
    draw_text(f"RACE TIME - {round(match_time)}", small_font, "cyan", 30, 60, GAME_SCREEN)

    draw_text(f"LAP - {lap} / {settings.max_laps}", small_font, "cyan", 73, 1040, GAME_SCREEN)

    enemy_title()


def enemy_title():
    draw_text(f"SECOND PLAYER", medium_font, "red", 150, 15, GAME_SCREEN)


def game_show_fps(clock):
    draw_text(f"FPS - {round(clock.get_fps())}", small_font, "cyan", 30, 20, GAME_SCREEN)


def player_time_table(fastest_time, slowest_time, match_time):
    GAME_SCREEN.blit(time_background2, (700, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", normal_font, "green", 740, 250, GAME_SCREEN)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", normal_font, "red", 740, 350, GAME_SCREEN)
    draw_text(f"MATCH TIME : {round(match_time)}", normal_font, "white", 740, 450, GAME_SCREEN)


def enemy_time_table(fastest_time, slowest_time, match_time):
    GAME_SCREEN.blit(time_background2, (700, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", normal_font, "green", 740, 250, GAME_SCREEN)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", normal_font, "red", 740, 350, GAME_SCREEN)
    draw_text(f"MATCH TIME : {round(match_time)}", normal_font, "white", 740, 450, GAME_SCREEN)


def animation(stopwatch, car, first_image, second_image):
    if stopwatch % 2 == 0:
        car.car_image = first_image
        car.render_position(GAME_SCREEN)
        pygame.display.update()

    if stopwatch % 3 == 0:
        car.car_image = second_image
        car.render_position(GAME_SCREEN)
        pygame.display.update()


def second_animation(stopwatch, enemy, first_image, second_image):
    if stopwatch % 3 == 0:
        enemy.car_image = second_image
        enemy.render_position(GAME_SCREEN)
        pygame.display.update()

    if stopwatch % 2 == 0:
        enemy.car_image = first_image
        enemy.render_position(GAME_SCREEN)
        pygame.display.update()


def car_animation(stopwatch, car):
    if settings.car_type == 1:
        animation(stopwatch, car, blue_formula, blue_formula_2)

    if settings.car_type == 2:
        animation(stopwatch, car, orange_formula, orange_formula_2)

    if settings.car_type == 3:
        animation(stopwatch, car, yellow_formula, yellow_formula_2)

    if settings.car_type == 4:
        animation(stopwatch, car, green_formula, green_formula_2)


def enemy_animation(stopwatch, enemy):
    if settings.enemy_car_type == 1:
        second_animation(stopwatch, enemy, purple_formula, purple_formula_2)

    if settings.enemy_car_type == 2:
        second_animation(stopwatch, enemy, orange_formula, orange_formula_2)

    if settings.enemy_car_type == 3:
        second_animation(stopwatch, enemy, yellow_formula, yellow_formula_2)

    if settings.enemy_car_type == 4:
        second_animation(stopwatch, enemy, green_formula, green_formula_2)
