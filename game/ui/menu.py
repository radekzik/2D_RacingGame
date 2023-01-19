import pygame

from game.config import settings
from game.maps.maps import AllMaps
from game.storage.storing_data import load_lap_times, load_match_times
from game.ui.button import Button, button_hover_render
from game.ui.load_image import GAME_SCREEN, big_font, button_transparent_image, normal_font, small_font, \
    first_map_image, \
    second_map_image, blue_lambo_selection, blue_formula_selection, f_background, formula_selection, lambo_selection, \
    orange_formula_selection, green_formula_selection, yellow_formula_selection, cyan_lambo_selection, \
    red_lambo_selection, pink_lambo_selection, third_map_image, dark_purple_spoiler_car_selection, \
    light_blue_spoiler_car_selection, orange_spoiler_car_selection, pink_spoiler_car_selection, spoiler_car_selection, \
    pointer_right, pointer_left, on_off_button, button_image, fourth_map_image, fifth_map_image, medium_font
from game.ui.resolution import draw_text

TITLE_Y = 70
TITLE_COLOR = "purple"
QUIT_Y = 980


def mode_selection():
    pygame.display.set_caption("2D Racing Game - Mode Selection")

    while 1:

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MODE SELECTION", big_font, TITLE_COLOR, 640, TITLE_Y, GAME_SCREEN)

        against_pc = Button(button_image=button_transparent_image, x_y=(760, 420),
                            button_text="VERSUS PC", font=normal_font, font_color="white", font_hover_color="cyan")

        one_vs_one = Button(button_image=button_transparent_image, x_y=(1160, 420),
                            button_text="1 VS 1", font=normal_font, font_color="white", font_hover_color="cyan")

        solo = Button(button_image=button_transparent_image, x_y=(960, 580),
                      button_text="SOLO", font=normal_font, font_color="white", font_hover_color="cyan")

        # multiplayer = Button(button_image=button_transparent_image, x_y=(1160, 580),
        #  button_text="MULTIPLAYER", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        solo.button_render(GAME_SCREEN)
        # multiplayer.button_render(game_screen)
        against_pc.button_render(GAME_SCREEN)
        one_vs_one.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(solo, mouse_coordinates, GAME_SCREEN)
        # button_hover_render(multiplayer, mouse_coordinates, game_screen)
        button_hover_render(against_pc, mouse_coordinates, GAME_SCREEN)
        button_hover_render(one_vs_one, mouse_coordinates, GAME_SCREEN)
        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo.on_click(mouse_coordinates):
                    map_selection(AllMaps.first_map_solo, AllMaps.second_map_solo,
                                  AllMaps.third_map_solo, AllMaps.fourth_map_solo, AllMaps.fifth_map_solo)

                # if multiplayer.on_click(mouse_coordinates):
                # multiplayer_selection()

                if against_pc.on_click(mouse_coordinates):
                    map_selection(AllMaps.first_map_vs_pc, AllMaps.second_map_vs_pc,
                                  AllMaps.third_map_vs_pc, AllMaps.fourth_map_vs_pc, AllMaps.fifth_map_vs_pc)

                if one_vs_one.on_click(mouse_coordinates):
                    map_selection(AllMaps.first_map_1v1, AllMaps.second_map_1v1,
                                  AllMaps.third_map_1v1, AllMaps.fourth_map_1v1, AllMaps.fifth_map_1v1)

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def map_selection(first_button, second_button, third_button, fourth_button, fifth_button):
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while 1:

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", big_font, TITLE_COLOR, 680, TITLE_Y, GAME_SCREEN)

        draw_text("I. MAP", small_font, "cyan", 410, 380, GAME_SCREEN)
        draw_text("II. MAP", small_font, "cyan", 940, 340, GAME_SCREEN)
        draw_text("III. MAP", small_font, "cyan", 1440, 315, GAME_SCREEN)
        draw_text("IV. MAP", small_font, "cyan", 675, 615, GAME_SCREEN)
        draw_text("V. MAP", small_font, "cyan", 1185, 615, GAME_SCREEN)

        first_map_button = Button(button_image=first_map_image, x_y=(500, 450),
                                  button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        second_map_button = Button(button_image=second_map_image, x_y=(970, 450),
                                   button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        third_map_button = Button(button_image=third_map_image, x_y=(1470, 450),
                                  button_text="", font=normal_font, font_color="white",
                                  font_hover_color="cyan")

        fourth_map_button = Button(button_image=fourth_map_image, x_y=(700, 750),
                                   button_text="", font=normal_font, font_color="white",
                                   font_hover_color="cyan")

        fifth_map_button = Button(button_image=fifth_map_image, x_y=(1220, 750),
                                  button_text="", font=normal_font, font_color="white",
                                  font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        first_map_button.button_render(GAME_SCREEN)
        second_map_button.button_render(GAME_SCREEN)
        third_map_button.button_render(GAME_SCREEN)
        fourth_map_button.button_render(GAME_SCREEN)
        fifth_map_button.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    first_button()
                if second_map_button.on_click(mouse_coordinates):
                    second_button()
                if third_map_button.on_click(mouse_coordinates):
                    third_button()
                if fourth_map_button.on_click(mouse_coordinates):
                    fourth_button()
                if fifth_map_button.on_click(mouse_coordinates):
                    fifth_button()
                if back_button.on_click(mouse_coordinates):
                    mode_selection()

        pygame.display.update()


def multiplayer_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while 1:

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", big_font, TITLE_COLOR, 680, TITLE_Y, GAME_SCREEN)

        game_connect = Button(button_image=button_transparent_image, x_y=(960, 500),
                              button_text="CONNECT", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        game_connect.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(game_connect, mouse_coordinates, GAME_SCREEN)
        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.on_click(mouse_coordinates):
                    mode_selection()

        pygame.display.update()


def car_selection():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("CAR SELECTION", big_font, TITLE_COLOR, 680, TITLE_Y, GAME_SCREEN)

        draw_text("FORMULA", small_font, "white", 525, 330, GAME_SCREEN)
        draw_text("LAMBORGHINI", small_font, "white", 910, 330, GAME_SCREEN)
        draw_text("SPOILER CAR", small_font, "white", 1310, 330, GAME_SCREEN)

        formula_button = Button(x_y=(560, 550), button_image=formula_selection, button_text="", font=small_font,
                                font_color="white", font_hover_color="cyan")

        lambo_button = Button(x_y=(960, 550), button_image=lambo_selection, button_text="", font=small_font,
                              font_color="white", font_hover_color="cyan")

        spoiler_car_button = Button(x_y=(1360, 550), button_image=spoiler_car_selection, button_text="",
                                    font=small_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        formula_button.button_render(GAME_SCREEN)
        lambo_button.button_render(GAME_SCREEN)
        spoiler_car_button.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if formula_button.on_click(mouse_coordinates):
                    car_selection_formula()

                if lambo_button.on_click(mouse_coordinates):
                    car_selection_lambo()

                if spoiler_car_button.on_click(mouse_coordinates):
                    car_selection_spoiler_car()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def car_selection_formula():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("FORMULA", big_font, TITLE_COLOR, 770, TITLE_Y, GAME_SCREEN)

        draw_text("BLUE", small_font, "cyan", 330, 340, GAME_SCREEN)
        draw_text("ORANGE", small_font, "orange", 720, 340, GAME_SCREEN)
        draw_text("YELLOW", small_font, "yellow", 1115, 340, GAME_SCREEN)
        draw_text("GREEN", small_font, "green", 1530, 340, GAME_SCREEN)

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

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        blue_formula_button.button_render(GAME_SCREEN)
        orange_formula_button.button_render(GAME_SCREEN)
        yellow_formula_button.button_render(GAME_SCREEN)
        green_formula_button.button_render(GAME_SCREEN)

        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if blue_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 1
                    draw_text("Car Selected!", normal_font, "blue", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if orange_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 2
                    draw_text("Car Selected!", normal_font, "orange", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if yellow_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 3
                    draw_text("Car Selected!", normal_font, "yellow", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if green_formula_button.on_click(mouse_coordinates):
                    settings.car_type = 4
                    draw_text("Car Selected!", normal_font, "green", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if back_button.on_click(mouse_coordinates):
                    car_selection()

        pygame.display.update()


def car_selection_lambo():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("LAMBORGHINI", big_font, TITLE_COLOR, 710, TITLE_Y, GAME_SCREEN)

        draw_text("BLUE", small_font, "lightblue", 330, 340, GAME_SCREEN)
        draw_text("CYAN", small_font, "cyan", 730, 340, GAME_SCREEN)
        draw_text("RED", small_font, "red", 1130, 340, GAME_SCREEN)
        draw_text("PINK", small_font, "pink", 1530, 340, GAME_SCREEN)

        blue_lambo_button = Button(x_y=(350, 550), button_image=blue_lambo_selection, button_text="",
                                   font=small_font,
                                   font_color="white", font_hover_color="cyan")
        cyan_lambo_button = Button(x_y=(750, 550), button_image=cyan_lambo_selection, button_text="",
                                   font=small_font,
                                   font_color="white", font_hover_color="cyan")

        red_lambo_button = Button(x_y=(1150, 550), button_image=red_lambo_selection, button_text="",
                                  font=small_font,
                                  font_color="white", font_hover_color="cyan")

        pink_lambo_button = Button(x_y=(1550, 550), button_image=pink_lambo_selection, button_text="",
                                   font=small_font,
                                   font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        blue_lambo_button.button_render(GAME_SCREEN)
        cyan_lambo_button.button_render(GAME_SCREEN)
        red_lambo_button.button_render(GAME_SCREEN)
        pink_lambo_button.button_render(GAME_SCREEN)

        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if blue_lambo_button.on_click(mouse_coordinates):
                    settings.car_type = 5
                    draw_text("Car Selected!", normal_font, "blue", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if cyan_lambo_button.on_click(mouse_coordinates):
                    settings.car_type = 6
                    draw_text("Car Selected!", normal_font, "cyan", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if red_lambo_button.on_click(mouse_coordinates):
                    settings.car_type = 7
                    draw_text("Car Selected!", normal_font, "red", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if pink_lambo_button.on_click(mouse_coordinates):
                    settings.car_type = 8
                    draw_text("Car Selected!", normal_font, "pink", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if back_button.on_click(mouse_coordinates):
                    car_selection()

        pygame.display.update()


def car_selection_spoiler_car():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("SPOILER CAR", big_font, TITLE_COLOR, 720, TITLE_Y, GAME_SCREEN)

        draw_text("DARK PURPLE", small_font, "violet", 300, 340, GAME_SCREEN)
        draw_text("LIGHT BLUE", small_font, "cyan", 710, 335, GAME_SCREEN)
        draw_text("ORANGE", small_font, "orange", 1115, 340, GAME_SCREEN)
        draw_text("PINK", small_font, "purple", 1530, 340, GAME_SCREEN)

        dark_purple_spoiler_car_button = Button(x_y=(350, 550), button_image=dark_purple_spoiler_car_selection,
                                                button_text="", font=small_font,
                                                font_color="white", font_hover_color="cyan")

        light_blue_spoiler_car_button = Button(x_y=(750, 550), button_image=light_blue_spoiler_car_selection,
                                               button_text="", font=small_font,
                                               font_color="white", font_hover_color="cyan")

        orange_spoiler_car_button = Button(x_y=(1150, 550), button_image=orange_spoiler_car_selection,
                                           button_text="", font=small_font,
                                           font_color="white", font_hover_color="cyan")

        pink_spoiler_car_button = Button(x_y=(1550, 550), button_image=pink_spoiler_car_selection,
                                         button_text="", font=small_font,
                                         font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        dark_purple_spoiler_car_button.button_render(GAME_SCREEN)
        light_blue_spoiler_car_button.button_render(GAME_SCREEN)
        orange_spoiler_car_button.button_render(GAME_SCREEN)
        pink_spoiler_car_button.button_render(GAME_SCREEN)

        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if dark_purple_spoiler_car_button.on_click(mouse_coordinates):
                    settings.car_type = 9
                    draw_text("Car Selected!", normal_font, "violet", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if light_blue_spoiler_car_button.on_click(mouse_coordinates):
                    settings.car_type = 10
                    draw_text("Car Selected!", normal_font, "cyan", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if orange_spoiler_car_button.on_click(mouse_coordinates):
                    settings.car_type = 11
                    draw_text("Car Selected!", normal_font, "orange", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if pink_spoiler_car_button.on_click(mouse_coordinates):
                    settings.car_type = 12
                    draw_text("Car Selected!", normal_font, "purple", 790, 230, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    main_menu()

                if back_button.on_click(mouse_coordinates):
                    car_selection()

        pygame.display.update()


def pointer_right_():
    pointer_right_button = Button(button_image=pointer_right, x_y=(1600, 500),
                                  button_text="", font=normal_font, font_color="white", font_hover_color="white")

    return pointer_right_button


def pointer_left_():
    pointer_left_button = Button(button_image=pointer_left, x_y=(320, 500),
                                 button_text="", font=normal_font, font_color="white", font_hover_color="white")
    return pointer_left_button


def stats_first_map():
    pygame.display.set_caption("2D Racing Game - Stats")
    loading = 1

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))

        while loading:
            draw_text("Loading stats.", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Loading stats..", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Loading stats...", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)
            loading = False

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("STATS - FIRST MAP", big_font, TITLE_COLOR, 600, TITLE_Y, GAME_SCREEN)

        draw_text("FASTEST LAP TIMES", medium_font, "purple", 580, 330, GAME_SCREEN)
        draw_text("FASTEST RACE TIMES", medium_font, "purple", 1080, 330, GAME_SCREEN)

        lap_times = load_lap_times("first_map_lap_times.txt")
        match_times = load_match_times("first_map_match_times.txt")

        draw_text(f"1. - {lap_times[0]}" + "s", small_font, "green", 670, 400, GAME_SCREEN)
        draw_text(f"2. - {lap_times[1]}" + "s", small_font, "orange", 670, 450, GAME_SCREEN)
        draw_text(f"3. - {lap_times[2]}" + "s", small_font, "orange", 670, 500, GAME_SCREEN)
        draw_text(f"4. - {lap_times[3]}" + "s", small_font, "orange", 670, 550, GAME_SCREEN)
        draw_text(f"5. - {lap_times[4]}" + "s", small_font, "red", 670, 600, GAME_SCREEN)

        draw_text(f"1. - {match_times[0]}" + "s", small_font, "green", 1170, 400, GAME_SCREEN)
        draw_text(f"2. - {match_times[1]}" + "s", small_font, "orange", 1170, 450, GAME_SCREEN)
        draw_text(f"3. - {match_times[2]}" + "s", small_font, "orange", 1170, 500, GAME_SCREEN)
        draw_text(f"4. - {match_times[3]}" + "s", small_font, "orange", 1170, 550, GAME_SCREEN)
        draw_text(f"5. - {match_times[4]}" + "s", small_font, "red", 1170, 600, GAME_SCREEN)

        pointer_right_button = Button(button_image=pointer_right, x_y=(1600, 500),
                                      button_text="", font=normal_font, font_color="white", font_hover_color="white")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        pointer_right_button.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pointer_right_button.on_click(mouse_coordinates):
                    stats_second_map()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def stats_second_map():
    pygame.display.set_caption("2D Racing Game - Stats")
    loading = 1

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))

        while loading:
            draw_text("Loading stats.", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Loading stats..", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Loading stats...", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)
            loading = False

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("STATS - SECOND MAP", big_font, TITLE_COLOR, 560, TITLE_Y, GAME_SCREEN)

        draw_text("FASTEST LAP TIMES", small_font, "white", 670, 330, GAME_SCREEN)
        draw_text("FASTEST RACE TIMES", small_font, "white", 1170, 330, GAME_SCREEN)

        lap_times = load_lap_times("second_map_lap_times.txt")
        match_times = load_match_times("second_map_match_times.txt")

        draw_text(f"1. - {lap_times[0]}" + "s", small_font, "green", 670, 400, GAME_SCREEN)
        draw_text(f"2. - {lap_times[1]}" + "s", small_font, "orange", 670, 450, GAME_SCREEN)
        draw_text(f"3. - {lap_times[2]}" + "s", small_font, "orange", 670, 500, GAME_SCREEN)
        draw_text(f"4. - {lap_times[3]}" + "s", small_font, "orange", 670, 550, GAME_SCREEN)
        draw_text(f"5. - {lap_times[4]}" + "s", small_font, "red", 670, 600, GAME_SCREEN)

        draw_text(f"1. - {match_times[0]}" + "s", small_font, "green", 1170, 400, GAME_SCREEN)
        draw_text(f"2. - {match_times[1]}" + "s", small_font, "orange", 1170, 450, GAME_SCREEN)
        draw_text(f"3. - {match_times[2]}" + "s", small_font, "orange", 1170, 500, GAME_SCREEN)
        draw_text(f"4. - {match_times[3]}" + "s", small_font, "orange", 1170, 550, GAME_SCREEN)
        draw_text(f"5. - {match_times[4]}" + "s", small_font, "red", 1170, 600, GAME_SCREEN)

        pointer_right_button = Button(button_image=pointer_right, x_y=(1600, 500),
                                      button_text="", font=normal_font, font_color="white", font_hover_color="white")

        pointer_left_button = Button(button_image=pointer_left, x_y=(320, 500),
                                     button_text="", font=normal_font, font_color="white", font_hover_color="white")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        pointer_right_button.button_render(GAME_SCREEN)
        pointer_left_button.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pointer_right_button.on_click(mouse_coordinates):
                    stats_third_map()

                if pointer_left_button.on_click(mouse_coordinates):
                    stats_first_map()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def stats_third_map():
    pygame.display.set_caption("2D Racing Game - Stats")
    loading = 1

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))

        while loading:
            draw_text("Loading stats.", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Loading stats..", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)

            draw_text("Loading stats...", normal_font, "white", 780, 230, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(300)
            loading = False

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("STATS - THIRD MAP", big_font, TITLE_COLOR, 600, TITLE_Y, GAME_SCREEN)

        draw_text("FASTEST LAP TIMES", small_font, "white", 670, 330, GAME_SCREEN)
        draw_text("FASTEST RACE TIMES", small_font, "white", 1170, 330, GAME_SCREEN)

        lap_times = load_lap_times("third_map_lap_times.txt")
        match_times = load_match_times("third_map_match_times.txt")

        draw_text(f"1. - {lap_times[0]}" + "s", small_font, "green", 670, 400, GAME_SCREEN)
        draw_text(f"2. - {lap_times[1]}" + "s", small_font, "orange", 670, 450, GAME_SCREEN)
        draw_text(f"3. - {lap_times[2]}" + "s", small_font, "orange", 670, 500, GAME_SCREEN)
        draw_text(f"4. - {lap_times[3]}" + "s", small_font, "orange", 670, 550, GAME_SCREEN)
        draw_text(f"5. - {lap_times[4]}" + "s", small_font, "red", 670, 600, GAME_SCREEN)

        draw_text(f"1. - {match_times[0]}" + "s", small_font, "green", 1170, 400, GAME_SCREEN)
        draw_text(f"2. - {match_times[1]}" + "s", small_font, "orange", 1170, 450, GAME_SCREEN)
        draw_text(f"3. - {match_times[2]}" + "s", small_font, "orange", 1170, 500, GAME_SCREEN)
        draw_text(f"4. - {match_times[3]}" + "s", small_font, "orange", 1170, 550, GAME_SCREEN)
        draw_text(f"5. - {match_times[4]}" + "s", small_font, "red", 1170, 600, GAME_SCREEN)

        pointer_left_button = Button(button_image=pointer_left, x_y=(320, 500),
                                     button_text="", font=normal_font, font_color="white", font_hover_color="white")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        pointer_left_button.button_render(GAME_SCREEN)
        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pointer_left_button.on_click(mouse_coordinates):
                    stats_second_map()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def binds():
    pygame.display.set_caption("2D Racing Game - Binds")

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("BINDS", big_font, TITLE_COLOR, 820, TITLE_Y, GAME_SCREEN)

        #  draw_text("W - Forward", medium_font, "white", 620, 300, GAME_SCREEN)
        # draw_text("S - Backward", normal_font, "cyan", 950, 300, GAME_SCREEN)
        # draw_text("A - Left", normal_font, "cyan", 680, 450, GAME_SCREEN)
        # draw_text("D - Right", normal_font, "white", 1010, 450, GAME_SCREEN)

        # draw_text("E - Nitro", normal_font, "white", 680, 600, GAME_SCREEN)
        # draw_text("Q - Faster Movement", normal_font, "cyan", 1010, 600, GAME_SCREEN)

        # draw_text("R - Restart", normal_font, "orange", 990, 750, GAME_SCREEN)
        # draw_text("X - Exit", normal_font, "red", 690, 750, GAME_SCREEN)

        draw_text("CAR CONTROL", normal_font, "purple", 495, 200, GAME_SCREEN)

        draw_text("W", medium_font, "white", 625, 280, GAME_SCREEN)
        draw_text("Forward", medium_font, "cyan", 1220, 280, GAME_SCREEN)

        draw_text("S", medium_font, "white", 630, 330, GAME_SCREEN)
        draw_text("Backward", medium_font, "cyan", 1220, 330, GAME_SCREEN)

        draw_text("A", medium_font, "white", 630, 380, GAME_SCREEN)
        draw_text("Left", medium_font, "cyan", 1220, 380, GAME_SCREEN)

        draw_text("D", medium_font, "white", 630, 430, GAME_SCREEN)
        draw_text("Right", medium_font, "cyan", 1220, 430, GAME_SCREEN)

        draw_text("CAR ABILITIES", normal_font, "purple", 495, 480, GAME_SCREEN)

        draw_text("E", medium_font, "white", 632, 560, GAME_SCREEN)
        draw_text("Nitro", medium_font, "cyan", 1220, 560, GAME_SCREEN)

        draw_text("Q", medium_font, "white", 630, 610, GAME_SCREEN)
        draw_text("Faster Movement", medium_font, "cyan", 1220, 610, GAME_SCREEN)

        draw_text("IN-GAME", normal_font, "purple", 550, 660, GAME_SCREEN)

        draw_text("R", medium_font, "white", 630, 740, GAME_SCREEN)
        draw_text("Restart Game", medium_font, "cyan", 1220, 740, GAME_SCREEN)

        draw_text("X", medium_font, "white", 630, 790, GAME_SCREEN)
        draw_text("Exit", medium_font, "cyan", 1220, 790, GAME_SCREEN)

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def on_off_display(button, mouse_coordinates, option, value, text, x, y, delay):
    if button.on_click(mouse_coordinates):
        option = value
        draw_text(text, normal_font, "green", x, y, GAME_SCREEN)
        pygame.display.update()
        pygame.time.wait(delay)


def game_settings():
    pygame.display.set_caption("2D Racing Game - Settings")

    while 1:
        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("SETTINGS", big_font, TITLE_COLOR, 765, TITLE_Y, GAME_SCREEN)

        draw_text("AUDIO", normal_font, "cyan", 620, 300, GAME_SCREEN)
        # draw_text("CAMERA FOCUS", normal_font, "cyan", 620, 400, GAME_SCREEN)
        draw_text("VSYNC", normal_font, "cyan", 620, 400, GAME_SCREEN)
        draw_text("UI", normal_font, "cyan", 620, 500, GAME_SCREEN)
        draw_text("FPS", normal_font, "cyan", 620, 600, GAME_SCREEN)
        draw_text("CAR XY", normal_font, "cyan", 620, 700, GAME_SCREEN)

        audio_on_button = Button(button_image=on_off_button, x_y=(1220, 340),
                                 button_text="ON", font=small_font, font_color="white", font_hover_color="white")

        audio_off_button = Button(button_image=on_off_button, x_y=(1300, 340),
                                  button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

        # camera_on_button = Button(button_image=on_off_button, x_y=(1220, 440),
        # button_text="ON", font=small_font, font_color="white", font_hover_color="white")

        # camera_off_button = Button(button_image=on_off_button, x_y=(1300, 440),
        # button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

        vsync_on_button = Button(button_image=on_off_button, x_y=(1220, 440),
                                 button_text="ON", font=small_font, font_color="white", font_hover_color="white")
        vsync_off_button = Button(button_image=on_off_button, x_y=(1300, 440),
                                  button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

        show_ui_on_button = Button(button_image=on_off_button, x_y=(1220, 540),
                                   button_text="ON", font=small_font, font_color="white", font_hover_color="white")
        show_ui_off_button = Button(button_image=on_off_button, x_y=(1300, 540),
                                    button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

        show_fps_on_button = Button(button_image=on_off_button, x_y=(1220, 640),
                                    button_text="ON", font=small_font, font_color="white", font_hover_color="white")
        show_fps_off_button = Button(button_image=on_off_button, x_y=(1300, 640),
                                     button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

        show_xy_on_button = Button(button_image=on_off_button, x_y=(1220, 740),
                                   button_text="ON", font=small_font, font_color="white", font_hover_color="white")
        show_xy_off_button = Button(button_image=on_off_button, x_y=(1300, 740),
                                    button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

        back_button = Button(button_image=button_image, x_y=(960, QUIT_Y),
                             button_text="BACK", font=normal_font, font_color="orange", font_hover_color="red")

        audio_on_button.button_render(GAME_SCREEN)
        audio_off_button.button_render(GAME_SCREEN)

        # camera_on_button.button_render(GAME_SCREEN)
        # camera_off_button.button_render(GAME_SCREEN)

        vsync_on_button.button_render(GAME_SCREEN)
        vsync_off_button.button_render(GAME_SCREEN)

        show_ui_on_button.button_render(GAME_SCREEN)
        show_ui_off_button.button_render(GAME_SCREEN)

        show_fps_on_button.button_render(GAME_SCREEN)
        show_fps_off_button.button_render(GAME_SCREEN)

        show_xy_on_button.button_render(GAME_SCREEN)
        show_xy_off_button.button_render(GAME_SCREEN)

        back_button.button_render(GAME_SCREEN)

        button_hover_render(back_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # on_off_display(audio_on_button, mouse_coordinates, settings.audio, 1, "AUDIO ON!", 830, 210, 1000)
                # on_off_display(audio_off_button, mouse_coordinates, settings.audio, 2, "AUDIO OFF!", 830, 210, 1000)

                # on_off_display(camera_on_button, mouse_coordinates, settings.camera_focus, 1, "CAMERA FOCUS ON!", 730,
                # 210, 1000)
                # on_off_display(audio_off_button, mouse_coordinates, settings.camera_focus, 2, "CAMERA FOCUS OFF!", 730,
                # 210, 1000)

                # on_off_display(vsync_on_button, mouse_coordinates, settings.vsync, 1, "VSYNC ON!", 830, 210, 1000)
                # on_off_display(vsync_off_button, mouse_coordinates, settings.vsync, 0, "VSYNC OFF!", 830, 210, 1000)

                # on_off_display(show_fps_on_button, mouse_coordinates, settings.show_fps, 1, "FPS ON!", 850, 210, 1000)
                # on_off_display(show_fps_off_button, mouse_coordinates, settings.show_fps, 2, "FPS OFF!", 850, 210, 1000)

                # on_off_display(show_ui_on_button, mouse_coordinates, settings.show_fps, 1, "UI ON!", 850, 210, 1000)
                # on_off_display(show_ui_off_button, mouse_coordinates, settings.show_fps, 2, "UI OFF!", 850, 210, 1000)

                if audio_on_button.on_click(mouse_coordinates):
                    settings.audio = 1
                    print(settings.audio)
                    draw_text("AUDIO ON!", normal_font, "green", 830, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)

                if audio_off_button.on_click(mouse_coordinates):
                    settings.audio = 2
                    print(settings.audio)
                    draw_text("AUDIO OFF!", normal_font, "green", 830, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(2000)

                # if camera_on_button.on_click(mouse_coordinates):
                #  settings.camera_focus = 1
                #  draw_text("CAMERA FOCUS ON!", normal_font, "green", 730, 210, GAME_SCREEN)
                #  pygame.display.update()
                # pygame.time.wait(2000)

                # if camera_off_button.on_click(mouse_coordinates):
                # settings.camera_focus = 2
                # draw_text("CAMERA FOCUS OFF!", normal_font, "green", 730, 210, GAME_SCREEN)
                # pygame.display.update()
                # pygame.time.wait(2000)

                if vsync_on_button.on_click(mouse_coordinates):
                    settings.vsync = 1
                    print(settings.vsync)
                    draw_text("VSYNC ON!", normal_font, "green", 830, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if vsync_off_button.on_click(mouse_coordinates):
                    settings.vsync = 0
                    print(settings.vsync)
                    draw_text("VSYNC OFF!", normal_font, "green", 830, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if show_ui_on_button.on_click(mouse_coordinates):
                    settings.show_ui = 1
                    print(settings.show_ui)
                    draw_text("UI ON!", normal_font, "green", 850, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if show_ui_off_button.on_click(mouse_coordinates):
                    settings.show_ui = 2
                    print(settings.show_ui)
                    draw_text("UI OFF!", normal_font, "green", 850, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if show_fps_on_button.on_click(mouse_coordinates):
                    settings.show_fps = 1
                    print(settings.show_fps)
                    draw_text("FPS ON!", normal_font, "green", 850, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if show_fps_off_button.on_click(mouse_coordinates):
                    settings.show_fps = 2
                    print(settings.show_fps)
                    draw_text("FPS OFF!", normal_font, "green", 850, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if show_xy_on_button.on_click(mouse_coordinates):
                    settings.show_xy = 1
                    draw_text("X-Y ON!", normal_font, "green", 850, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if show_xy_off_button.on_click(mouse_coordinates):
                    settings.show_xy = 2
                    draw_text("X-Y OFF!", normal_font, "green", 850, 210, GAME_SCREEN)
                    pygame.display.update()
                    pygame.time.wait(1200)

                if back_button.on_click(mouse_coordinates):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("2D Racing Game - Menu")

    while 1:

        GAME_SCREEN.blit(f_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAIN MENU", big_font, TITLE_COLOR, 750, TITLE_Y, GAME_SCREEN)

        play_button = Button(button_image=button_transparent_image, x_y=(960, 300), button_text="PLAY",
                             font=normal_font,
                             font_color="white", font_hover_color="cyan")

        car_selection_button = Button(button_image=button_transparent_image, x_y=(590, 390), button_text="SELECT CAR",
                                      font=normal_font,
                                      font_color="white", font_hover_color="cyan")

        stats_button = Button(button_image=button_transparent_image, x_y=(1330, 390), button_text="STATS",
                              font=normal_font,
                              font_color="white", font_hover_color="cyan")

        binds_button = Button(button_image=button_transparent_image, x_y=(960, 430), button_text="BINDS",
                              font=normal_font,
                              font_color="white", font_hover_color="cyan")

        settings_button = Button(button_image=button_transparent_image, x_y=(960, 550), button_text="SETTINGS",
                                 font=normal_font,
                                 font_color="white", font_hover_color="cyan")

        quit_button = Button(button_image=button_image, x_y=(960, QUIT_Y), button_text="QUIT", font=normal_font,
                             font_color="orange", font_hover_color="red")

        play_button.button_render(GAME_SCREEN)
        car_selection_button.button_render(GAME_SCREEN)
        stats_button.button_render(GAME_SCREEN)
        binds_button.button_render(GAME_SCREEN)
        settings_button.button_render(GAME_SCREEN)
        quit_button.button_render(GAME_SCREEN)

        button_hover_render(play_button, mouse_coordinates, GAME_SCREEN)
        button_hover_render(car_selection_button, mouse_coordinates, GAME_SCREEN)
        button_hover_render(stats_button, mouse_coordinates, GAME_SCREEN)
        button_hover_render(binds_button, mouse_coordinates, GAME_SCREEN)
        button_hover_render(settings_button, mouse_coordinates, GAME_SCREEN)
        button_hover_render(quit_button, mouse_coordinates, GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.on_click(mouse_coordinates):
                    mode_selection()
                if car_selection_button.on_click(mouse_coordinates):
                    car_selection()
                if stats_button.on_click(mouse_coordinates):
                    stats_first_map()
                if binds_button.on_click(mouse_coordinates):
                    binds()
                if settings_button.on_click(mouse_coordinates):
                    game_settings()
                if quit_button.on_click(mouse_coordinates):
                    pygame.quit()

        pygame.display.update()
