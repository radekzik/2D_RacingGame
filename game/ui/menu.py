import pygame

from game.config import settings
from game.storage.storing_data import load_lap_times, load_match_times
from game.maps.game_third_map import game_third_map
from game.ui.button import Button, button_hover_render
from game.maps.game_first_map import first_map_1v1, game_first_map_solo, game_first_map
from game.maps.game_second_map import game_second_map_solo, game_second_map
from game.ui.load_image import game_screen, menu_background, big_font, button_image, normal_font, small_font, \
    first_map_image, \
    second_map_image, blue_lambo_selection, blue_formula_selection, f_background, formula_selection, lambo_selection, \
    orange_formula_selection, green_formula_selection, yellow_formula_selection
from game.ui.resolution import draw_text

title_y = 70
title_color = "purple"
quit_y = 980


def mode_selection():
    pygame.display.set_caption("2D Racing Game - Mode Selection")

    while True:

        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MODE SELECTION", big_font, title_color, 640, title_y, game_screen)

        against_pc = Button(button_image=button_image, x_y=(760, 420),
                            button_text="VERSUS PC", font=normal_font, font_color="white", font_hover_color="cyan")

        one_vs_one = Button(button_image=button_image, x_y=(1160, 420),
                            button_text="1 VS 1", font=normal_font, font_color="white", font_hover_color="cyan")

        solo = Button(button_image=button_image, x_y=(960, 580),
                      button_text="SOLO", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        solo.button_render(game_screen)
        against_pc.button_render(game_screen)
        one_vs_one.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(solo, mouse_coordinates, game_screen)
        button_hover_render(against_pc, mouse_coordinates, game_screen)
        button_hover_render(one_vs_one, mouse_coordinates, game_screen)
        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo.on_click(mouse_coordinates):
                    solo_map_selection()

                if against_pc.on_click(mouse_coordinates):
                    vs_map_selection()

                if one_vs_one.on_click(mouse_coordinates):
                    first_map_1v1()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def solo_map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", big_font, title_color, 680, title_y, game_screen)

        draw_text("FIRST MAP", small_font, "grey", 430, 450, game_screen)
        draw_text("SECOND MAP", small_font, "grey", 1300, 350, game_screen)

        first_map_button = Button(button_image=first_map_image, x_y=(600, 550),
                                  button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        second_map_button = Button(button_image=second_map_image, x_y=(1350, 550),
                                   button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map_solo()
                if second_map_button.on_click(mouse_coordinates):
                    game_second_map_solo()
                if back_button.on_click(mouse_coordinates):
                    mode_selection()

            pygame.display.update()


def vs_map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", big_font, title_color, 680, title_y, game_screen)
        draw_text("FIRST MAP", small_font, "grey", 430, 450, game_screen)
        draw_text("SECOND MAP", small_font, "grey", 1300, 350, game_screen)
        # draw_text("THIRD MAP", small_font, "grey", 680, 800, game_screen)

        first_map_button = Button(button_image=first_map_image, x_y=(600, 550),
                                  button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        second_map_button = Button(button_image=second_map_image, x_y=(1350, 550),
                                   button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        third_map_button = Button(button_image=button_image, x_y=(1350, 850),
                                  button_text="THIRD MAP", font=normal_font, font_color="white",
                                  font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        third_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(third_map_button, mouse_coordinates, game_screen)
        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map()
                if second_map_button.on_click(mouse_coordinates):
                    game_second_map()
                if third_map_button.on_click(mouse_coordinates):
                    game_third_map()
                if back_button.on_click(mouse_coordinates):
                    mode_selection()

            pygame.display.update()


def car_selection():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while True:
        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("CAR SELECTION", big_font, title_color, 680, title_y, game_screen)

        draw_text("FORMULA", small_font, "white", 720, 330, game_screen)
        draw_text("LAMBORGHINI", small_font, "white", 1100, 330, game_screen)

        formula_button = Button(x_y=(750, 550), button_image=formula_selection, button_text="", font=small_font,
                                font_color="white", font_hover_color="cyan")
        lambo_button = Button(x_y=(1150, 550), button_image=lambo_selection, button_text="", font=small_font,
                              font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        formula_button.button_render(game_screen)
        lambo_button.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if formula_button.on_click(mouse_coordinates):
                    car_selection_formula()

                if lambo_button.on_click(mouse_coordinates):
                    car_selection_lambo()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def car_selection_formula():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while True:
        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("FORMULA", big_font, title_color, 660, title_y, game_screen)

        blue_formula_button = Button(x_y=(350, 550), button_image=blue_formula_selection, button_text="",
                                     font=small_font,
                                     font_color="white", font_hover_color="cyan")
        orange_formula_button = Button(x_y=(750, 550), button_image=orange_formula_selection, button_text="",
                                       font=small_font,
                                       font_color="white", font_hover_color="cyan")

        yellow_formula_button = Button(x_y=(1150, 550), button_image=yellow_formula_selection, button_text="",
                                       font=small_font,
                                       font_color="white", font_hover_color="cyan")

        green_formula_button = Button(x_y=(1550, 550), button_image=green_formula_selection, button_text="",
                                      font=small_font,
                                      font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        blue_formula_button.button_render(game_screen)
        orange_formula_button.button_render(game_screen)
        yellow_formula_button.button_render(game_screen)
        green_formula_button.button_render(game_screen)

        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if blue_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 1
                    draw_text("Car Choosen!", normal_font, "blue", 780, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if orange_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 2
                    draw_text("Car Choosen!", normal_font, "orange", 780, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if yellow_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 3
                    draw_text("Car Choosen!", normal_font, "yellow", 780, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if green_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 4
                    draw_text("Car Choosen!", normal_font, "green", 780, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if back_button.on_click(mouse_coordinates):
                    car_selection()

            pygame.display.update()


def car_selection_lambo():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while True:
        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("LAMBORGHINI", big_font, title_color, 660, title_y, game_screen)

        lambo1_button = Button(x_y=(750, 550), button_image=blue_formula_selection, button_text="", font=small_font,
                               font_color="white", font_hover_color="cyan")
        lambo2_button = Button(x_y=(1150, 550), button_image=blue_formula_selection, button_text="", font=small_font,
                               font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        lambo1_button.button_render(game_screen)
        lambo2_button.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if lambo1_button.on_click(mouse_coordinates):
                    settings.car_type = 5
                    draw_text("Car Choosen!", normal_font, "green", 780, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if lambo2_button.on_click(mouse_coordinates):
                    settings.car_type = 6
                    draw_text("Car Choosen!", normal_font, "green", 780, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def stats():
    pygame.display.set_caption("2D Racing Game - Stats")
    loading = True

    while True:
        game_screen.blit(f_background, (0, 0))

        while loading:
            draw_text("Loading stats.", normal_font, "white", 780, 230, game_screen)
            pygame.display.update()
            pygame.time.wait(1000)

            draw_text("Loading stats..", normal_font, "white", 780, 230, game_screen)
            pygame.display.update()
            pygame.time.wait(1000)

            draw_text("Loading stats...", normal_font, "white", 780, 230, game_screen)
            pygame.display.update()
            pygame.time.wait(1000)
            loading = False

        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("STATS", big_font, title_color, 865, title_y, game_screen)

        draw_text("FASTEST LAP TIMES", small_font, "white", 670, 330, game_screen)
        draw_text("FASTEST RACE TIMES", small_font, "white", 1170, 330, game_screen)

        lap_times = load_lap_times()
        match_times = load_match_times()

        draw_text(f"1. - {lap_times[0]}" + "s", small_font, "green", 670, 400, game_screen)
        draw_text(f"2. - {lap_times[1]}" + "s", small_font, "orange", 670, 450, game_screen)
        draw_text(f"3. - {lap_times[2]}" + "s", small_font, "orange", 670, 500, game_screen)
        draw_text(f"4. - {lap_times[3]}" + "s", small_font, "orange", 670, 550, game_screen)
        draw_text(f"5. - {lap_times[4]}" + "s", small_font, "red", 670, 600, game_screen)

        draw_text(f"1. - {match_times[0]}" + "s", small_font, "green", 1170, 400, game_screen)
        draw_text(f"2. - {match_times[1]}" + "s", small_font, "orange", 1170, 450, game_screen)
        draw_text(f"3. - {match_times[2]}" + "s", small_font, "orange", 1170, 500, game_screen)
        draw_text(f"4. - {match_times[3]}" + "s", small_font, "orange", 1170, 550, game_screen)
        draw_text(f"5. - {match_times[4]}" + "s", small_font, "red", 1170, 600, game_screen)

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def binds():
    pygame.display.set_caption("2D Racing Game - Binds")

    while True:
        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("BINDS", big_font, title_color, 820, title_y, game_screen)

        draw_text("W - Forward", normal_font, "white", 620, 300, game_screen)
        draw_text("S - Backward", normal_font, "cyan", 950, 300, game_screen)
        draw_text("A - Left", normal_font, "cyan", 680, 450, game_screen)
        draw_text("D - Right", normal_font, "white", 1010, 450, game_screen)

        draw_text("E - Nitro", normal_font, "white", 680, 600, game_screen)
        draw_text("Q - Drift", normal_font, "cyan", 1010, 600, game_screen)

        draw_text("X - Exit", normal_font, "orange", 880, 750, game_screen)

        back_button = Button(button_image=button_image, x_y=(960, quit_y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def main_menu():
    pygame.display.set_caption("2D Racing Game - Menu")

    while True:

        game_screen.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAIN MENU", big_font, title_color, 750, title_y, game_screen)

        play_button = Button(button_image=button_image, x_y=(960, 300), button_text="PLAY", font=normal_font,
                             font_color="white", font_hover_color="cyan")

        car_selection_button = Button(button_image=button_image, x_y=(590, 390), button_text="CHOOSE CAR",
                                      font=normal_font,
                                      font_color="white", font_hover_color="cyan")

        stats_button = Button(button_image=button_image, x_y=(1330, 390), button_text="STATS",
                              font=normal_font,
                              font_color="white", font_hover_color="cyan")

        binds_button = Button(button_image=button_image, x_y=(960, 430), button_text="BINDS",
                              font=normal_font,
                              font_color="white", font_hover_color="cyan")

        quit_button = Button(button_image=button_image, x_y=(960, quit_y), button_text="QUIT", font=normal_font,
                             font_color="orange", font_hover_color="red")

        play_button.button_render(game_screen)
        car_selection_button.button_render(game_screen)
        stats_button.button_render(game_screen)
        binds_button.button_render(game_screen)
        quit_button.button_render(game_screen)

        button_hover_render(play_button, mouse_coordinates, game_screen)
        button_hover_render(car_selection_button, mouse_coordinates, game_screen)
        button_hover_render(stats_button, mouse_coordinates, game_screen)
        button_hover_render(binds_button, mouse_coordinates, game_screen)
        button_hover_render(quit_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.on_click(mouse_coordinates):
                    mode_selection()
                if car_selection_button.on_click(mouse_coordinates):
                    car_selection()
                if stats_button.on_click(mouse_coordinates):
                    stats()
                if binds_button.on_click(mouse_coordinates):
                    binds()
                if quit_button.on_click(mouse_coordinates):
                    pygame.quit()

        pygame.display.update()