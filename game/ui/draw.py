import pygame

from game.config import settings
from game.ui.load_image import game_screen, time_menu, normal_font, small_font, purple_formula_2, purple_formula, \
    pink_lambo, \
    blue_formula_2, blue_lambo, blue_formula, orange_formula, orange_formula_2, yellow_formula_2, yellow_formula, \
    green_formula, green_formula_2
from game.ui.resolution import draw_text


def game_info(match_time, clock, lap, stopwatch):
    draw_text(f"LAP TIME - {stopwatch}", small_font, "cyan", 1670, 900, game_screen)
    draw_text(f"RACE TIME - {round(match_time)}", small_font, "white", 1670, 850, game_screen)
    draw_text(f"FPS - {round(clock.get_fps())}", small_font, "cyan", 1780, 40, game_screen)
    draw_text(f"LAP - {lap} / {settings.max_laps}", small_font, "cyan", 1690, 800, game_screen)


def player_time_table(fastest_time, slowest_time, match_time):
    game_screen.blit(time_menu, (650, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", normal_font, "green", 740, 250, game_screen)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", normal_font, "red", 740, 350, game_screen)
    draw_text(f"MATCH TIME : {round(match_time)}", normal_font, "white", 740, 450, game_screen)


def enemy_time_table(fastest_time, slowest_time, match_time):
    game_screen.blit(time_menu, (1050, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", normal_font, "green", 1150, 250, game_screen)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", normal_font, "red", 1150, 350, game_screen)
    draw_text(f"MATCH TIME : {round(match_time)}", normal_font, "white", 1150, 450, game_screen)


def animation(stopwatch, car, first_image, second_image):
    if stopwatch % 2 == 0:
        car.car_image = first_image
        car.render_position(game_screen)
        pygame.display.update()

    if stopwatch % 3 == 0:
        car.car_image = second_image
        car.render_position(game_screen)
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
    if stopwatch % 3 == 0:
        enemy.car_image = purple_formula
        enemy.render_position(game_screen)
        pygame.display.update()

    if stopwatch % 2 == 0:
        enemy.car_image = purple_formula_2
        enemy.render_position(game_screen)
        pygame.display.update()


