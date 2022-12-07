import pygame

import settings
from load_image import game_screen, time_menu, normal_font, small_font, purple_formula_2, purple_formula, pink_lambo, \
    blue_formula_2, blue_lambo, blue_formula
from resolution import draw_text


def game_info(match_time, clock, lap, stopwatch):
    draw_text("W - Forward", small_font, "white", 70, 40, game_screen)
    draw_text("S - Backward", small_font, "cyan", 70, 70, game_screen)
    draw_text("A - Left", small_font, "white", 70, 100, game_screen)
    draw_text("D - Right", small_font, "cyan", 70, 130, game_screen)
    draw_text("X - Exit", small_font, "cyan", 190, 40, game_screen)
    draw_text("E - Nitro", small_font, "white", 190, 70, game_screen)
    draw_text("Q - Drift", small_font, "cyan", 190, 100, game_screen)
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


def car_animation(stopwatch, car):
    if settings.car_type == 1:
        if stopwatch % 2 == 0:
            car.car_image = blue_formula
            car.render_position(game_screen)
            pygame.display.update()

        if stopwatch % 3 == 0:
            car.car_image = blue_formula_2
            car.render_position(game_screen)
            pygame.display.update()

    if settings.car_type == 2:
        if stopwatch % 2 == 0:
            car.car_image = blue_lambo
            car.render_position(game_screen)
            pygame.display.update()

        if stopwatch % 3 == 0:
            car.car_image = pink_lambo
            car.render_position(game_screen)
            pygame.display.update()


def enemy_animation(stopwatch, enemy):
    if stopwatch % 3 == 0:
        enemy.car_image = purple_formula
        enemy.render_position(game_screen)
        pygame.display.update()

    if stopwatch % 2 == 0:
        enemy.car_image = purple_formula_2
        enemy.render_position(game_screen)
        pygame.display.update()

    # if enemy_car_type == 2:
    # if stopwatch % 2 == 0:
    # enemy.car_image = pink_lambo
    # enemy.render_position(game_screen)
    # pygame.display.update()

    # if stopwatch % 3 == 0:
    # enemy.car_image = blue_lambo
    # enemy.render_position(game_screen)
    # pygame.display.update()
