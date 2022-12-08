import pygame

from game.config import settings
from game.ui.button import Button, button_hover_render
from game.maps.game_first_map import first_map_1v1, game_first_map_solo, game_first_map
from game.maps.game_second_map import game_second_map_solo, game_second_map
from game.ui.load_image import game_screen, menu_background, big_font, button_image, normal_font, small_font, \
    first_map_image, \
    second_map_image, lambo_selection, formula_selection
from game.ui.resolution import draw_text


def mode_selection():
    pygame.display.set_caption("2D Racing Game - Mode Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MODE SELECTION", big_font, "white", 640, 100, game_screen)

        against_pc = Button(button_image=button_image, x_y=(760, 420),
                            button_text="VERSUS PC", font=normal_font, font_color="white", font_hover_color="cyan")

        one_vs_one = Button(button_image=button_image, x_y=(1160, 420),
                            button_text="1 VS 1", font=normal_font, font_color="white", font_hover_color="cyan")

        solo = Button(button_image=button_image, x_y=(960, 580),
                      button_text="SOLO", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, 950),
                             button_text="BACK", font=normal_font, font_color="white", font_hover_color="cyan")

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

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", big_font, "white", 680, 100, game_screen)
        draw_text("FIRST MAP", small_font, "grey", 430, 450, game_screen)
        draw_text("SECOND MAP", small_font, "grey", 1300, 350, game_screen)

        first_map_button = Button(button_image=first_map_image, x_y=(600, 550),
                                  button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        second_map_button = Button(button_image=second_map_image, x_y=(1350, 550),
                                   button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, 950),
                             button_text="BACK", font=normal_font, font_color="white", font_hover_color="cyan")

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

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", big_font, "white", 680, 100, game_screen)
        draw_text("FIRST MAP", small_font, "grey", 430, 450, game_screen)
        draw_text("SECOND MAP", small_font, "grey", 1300, 350, game_screen)

        first_map_button = Button(button_image=first_map_image, x_y=(600, 550),
                                  button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        second_map_button = Button(button_image=second_map_image, x_y=(1350, 550),
                                   button_text="", font=normal_font, font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(960, 950),
                             button_text="BACK", font=normal_font, font_color="white", font_hover_color="cyan")

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map()
                if second_map_button.on_click(mouse_coordinates):
                    game_second_map()
                if back_button.on_click(mouse_coordinates):
                    mode_selection()

            pygame.display.update()


def car_selection():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while True:
        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("CAR SELECTION", big_font, "white", 720, 100, game_screen)
        draw_text("FORMULA", small_font, "white", 770, 330, game_screen)
        draw_text("LAMBORGHINI", small_font, "white", 1150, 330, game_screen)

        formula_button = Button(x_y=(800, 550), button_image=formula_selection, button_text="", font=small_font,
                                font_color="white", font_hover_color="cyan")
        lambo_button = Button(x_y=(1200, 550), button_image=lambo_selection, button_text="", font=small_font,
                              font_color="white", font_hover_color="cyan")

        back_button = Button(button_image=button_image, x_y=(1000, 900),
                             button_text="BACK", font=normal_font, font_color="white", font_hover_color="cyan")

        formula_button.button_render(game_screen)
        lambo_button.button_render(game_screen)
        back_button.button_render(game_screen)

        button_hover_render(back_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if formula_button.on_click(mouse_coordinates):
                    settings.car_type = 0
                    settings.car_type = 1
                    draw_text("Car Choosen!", normal_font, "green", 830, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if lambo_button.on_click(mouse_coordinates):
                    settings.car_type = 0
                    settings.car_type = 2
                    draw_text("Car Choosen!", normal_font, "green", 830, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def main_menu():
    settings.car_type = 1

    pygame.display.set_caption("2D Racing Game - Menu")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAIN MENU", big_font, "white", 750, 100, game_screen)

        play_button = Button(button_image=button_image, x_y=(960, 350), button_text="PLAY", font=normal_font,
                             font_color="white", font_hover_color="cyan")

        car_selection_button = Button(button_image=button_image, x_y=(960, 500), button_text="CHOOSE CAR",
                                      font=normal_font,
                                      font_color="white", font_hover_color="cyan")

        quit_button = Button(button_image=button_image, x_y=(960, 950), button_text="QUIT", font=normal_font,
                             font_color="white", font_hover_color="cyan")

        play_button.button_render(game_screen)
        car_selection_button.button_render(game_screen)
        quit_button.button_render(game_screen)

        button_hover_render(play_button, mouse_coordinates, game_screen)
        button_hover_render(car_selection_button, mouse_coordinates, game_screen)
        button_hover_render(quit_button, mouse_coordinates, game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.on_click(mouse_coordinates):
                    mode_selection()
                if car_selection_button.on_click(mouse_coordinates):
                    car_selection()
                if quit_button.on_click(mouse_coordinates):
                    pygame.quit()

        pygame.display.update()
