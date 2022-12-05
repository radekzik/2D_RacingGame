from button import Button
from draw import game_info, player_time_table, enemy_animation, car_animation
from key_binds import player_key_binds, enemy_key_binds
from resolution import draw_text
from load_image import *
from player import Player
from enemy import EnemyPlayer
from pc import PCPlayer
from rects import *
import settings

pygame.init()





def collision_solo(car, map_border):
    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()


def collision_vs_pc(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch, car_time_list, enemy_time_list):
    if car_rect.colliderect(enemy_rect):
        car.car_collide()
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()

    if FIRST_FINISH_LINE_X_RANGE < enemy_car.x < SECOND_FINISH_LINE_X_RANGE:
        if FIRST_FINISH_LINE_Y_RANGE < enemy_car.y < SECOND_FINISH_LINE_Y_RANGE:
            settings.enemy_lap += 1
            settings.enemy_start_time = pygame.time.get_ticks()
            settings.enemy_match_time = settings.enemy_match_time + enemy_stopwatch
            enemy_car.respawn_first_map()
            enemy_car.next_route_position = 0
            enemy_car.start_drive()

    if settings.enemy_lap == settings.max_laps:
        print(settings.enemy_lap)
        if settings.car_lap < settings.enemy_lap:
            draw_text(f"YOU LOST THE RACE!", font, "red", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)
        if settings.car_lap > settings.enemy_lap:
            draw_text(f"YOU WON THE RACE!", font, "gold", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)
        stats_reset(car, enemy_car, car_time_list, enemy_time_list)

        check_new_game()
        game_first_map()


def collision_vs_player(car, enemy_car, car_rect, enemy_rect, map_border):
    if car_rect.colliderect(enemy_rect):
        car.car_collide()
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if enemy_rect.colliderect(car_rect):
        enemy_car.car_collide()
    else:
        enemy_car.car_image = enemy_car.car_image
        enemy_car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()

    if enemy_car.border_collide(pygame.mask.from_surface(map_border)):
        enemy_car.out_of_track()


def check_new_game():

    settings.started = False

    while not settings.started:
        game_screen.blit(time_menu, (700, 200))
        draw_text("PLAY AGAIN - SPACE", font, "white", 740, 250, game_screen)
        draw_text("EXIT TO MENU - X", font, "white", 740, 350, game_screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = True
                settings.car_start_time = pygame.time.get_ticks()


def check_car_type(car):
    if settings.car_type == 1:
        car.first_map_car()
    if settings.car_type == 2:
        car.second_map_car()


def start_game():

    while not settings.started:
        draw_text(f"Press Any Key To Start", font, "white", 70, 220, game_screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = True
                settings.car_start_time = pygame.time.get_ticks()


def start_countdown(car, enemy_car):
    if settings.countdown > 0:

        count_timer = pygame.time.get_ticks()
        car.max_speed = 0
        car.car_nitro = 0
        car.movement_speed = 0

        enemy_car.max_speed = 0
        enemy_car.car_nitro = 0
        enemy_car.movement_speed = 0

        if count_timer - settings.last_count > 1000:
            settings.countdown -= 1
            settings.last_count = count_timer

    if settings.countdown == 5 or settings.countdown == 4:
        game_screen.blit(semaphor_all_red, (880, 500))

    if settings.countdown == 3:
        draw_text(f"{str(settings.countdown)} - READY", font, "red", 850, 570, game_screen)
        game_screen.blit(semaphor_red, (880, 500))

    if settings.countdown == 2:
        draw_text(f"{str(settings.countdown)} - STEADY", font, "orange", 850, 570, game_screen)
        game_screen.blit(semaphor_orange, (880, 500))

    if settings.countdown == 1:
        draw_text(f"{str(settings.countdown)} - GO!", font, "green", 880, 570, game_screen)
        game_screen.blit(semaphor_green, (880, 500))

    if settings.countdown == 0:
        # draw_text(f"", font, "white", 900, 500)

        car.max_speed = 3
        car.car_nitro = 5
        car.max_movement_speed = 2.5

        enemy_car.max_speed = 3
        enemy_car.car_nitro = 5
        enemy_car.max_movement_speed = 2.5


def stats_reset(car, enemy, car_time_list, enemy_time_list):
    car_time_list.clear()
    enemy_time_list.clear()

    settings.car_lap = 0
    settings.enemy_lap = 0
    settings.car_match_time = 0
    settings.enemy_match_time = 0

    car.respawn_first_map()
    enemy.respawn_first_map()
    enemy.next_route_position = 0
    settings.car_start_time = pygame.time.get_ticks()
    settings.enemy_start_time = pygame.time.get_ticks()


def game_first_map():
    settings.max_laps = 3
    settings.car_lap = 0
    settings.enemy_lap = 0

    settings.animation_value = 0
    settings.car_start_time = 0
    settings.enemy_start_time = 0
    settings.car_match_time = 0
    settings.enemy_match_time = 0

    settings.car_time_list = []
    settings.enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap - VS PC")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        pc_car = PCPlayer()

        settings.started = False

        while game_loop:

            clock.tick(60)

            car_stopwatch = pygame.time.get_ticks() - settings.car_start_time
            car_stopwatch = car_stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (580, 840))

            start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.first_map_route()

            game_info(settings.car_match_time, clock, settings.car_lap, car_stopwatch)

            car.car_info()

            pc_car.first_map_car()
            enemy_animation(car_stopwatch, pc_car)

            check_car_type(car)

            car.render_position(game_screen)
            pc_car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # finish_line_rect = get_finish_line_rect()
            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(pc_car.car_image, pc_car.car_angle, pc_car.x, pc_car.y)

            player_key_binds(car, car_rect, enemy_rect, first_map_border)
            collision_vs_pc(car, pc_car, car_rect, enemy_rect, first_map_border, enemy_stopwatch,
                            settings.car_time_list,
                            settings.enemy_time_list)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if car_stopwatch > 5:

                        settings.car_lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, car_stopwatch)
                        settings.car_match_time = settings.car_match_time + car_stopwatch
                        draw_text(f"Lap Time - {car_stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)

                        check_new_game()
                        game_first_map()

                    if settings.car_lap == settings.max_laps:
                        print(settings.car_match_time)
                        print(settings.enemy_match_time)
                        print(settings.car_lap)
                        print(settings.max_laps)

                        if settings.car_lap > settings.enemy_lap:
                            draw_text(f"YOU WON THE RACE!", font, "gold", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        if settings.car_lap < settings.enemy_lap:
                            draw_text(f"YOU LOST THE RACE!", font, "red", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        settings.car_time_list.sort()
                        settings.enemy_time_list.sort()
                        player_time_table(settings.car_time_list[0], settings.car_time_list[2], settings.car_match_time)
                        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)
                        check_new_game()
                        game_first_map()

        settings.animation_value += 1
        pygame.display.update()


def game_second_map():
    settings.max_laps = 3
    settings.car_lap = 0
    settings.enemy_lap = 0

    settings.animation_value = 0
    settings.car_start_time = 0
    settings.enemy_start_time = 0
    settings.car_match_time = 0
    settings.enemy_match_time = 0

    settings.car_time_list = []
    settings.enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap - VS PC")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        pc_car = PCPlayer()

        settings.started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - settings.enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (580, 795))
            game_screen.blit(second_map_border, (0, 0))

            start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.second_map_route()

            game_info(settings.car_match_time, clock, settings.car_lap, stopwatch)

            car.car_info()

            pc_car.first_map_car()
            enemy_animation(stopwatch, pc_car)

            check_car_type(car)

            car.render_position(game_screen)
            pc_car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # finish_line_rect = finish_line.get_rect(topleft=(580, 795))

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(pc_car.car_image, pc_car.car_angle, pc_car.x, pc_car.y)

            player_key_binds(car, car_rect, enemy_rect, second_map_border)

            collision_vs_pc(car, pc_car, car_rect, enemy_rect, second_map_border, enemy_stopwatch,
                            settings.car_time_list,
                            settings.enemy_time_list)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        settings.car_lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, stopwatch)
                        settings.car_match_time = settings.car_match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)

                        check_new_game()
                        game_second_map()

                    if settings.car_lap == settings.max_laps:

                        if settings.car_lap > settings.enemy_lap:
                            draw_text(f"YOU WON THE RACE!", font, "gold", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        if settings.car_lap < settings.enemy_lap:
                            draw_text(f"YOU LOST THE RACE!", font, "red", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        settings.car_time_list.sort()
                        settings.enemy_time_list.sort()
                        player_time_table(settings.car_time_list[0], settings.car_time_list[2], settings.car_match_time)
                        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)
                        check_new_game()
                        game_second_map()

            settings.animation_value += 1
            pygame.display.update()


def game_first_map_solo(lap=0, match_time=0):
    settings.max_laps = 3
    settings.car_start_time = 0

    settings.car_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap - Solo")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        settings.started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (580, 849))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)
            car.car_info()
            check_car_type(car)

            car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            player_key_binds(car, car_rect, enemy_rect, first_map_border)

            collision_solo(car, first_map_border)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)
                        settings.car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map_solo()

                    if lap == settings.max_laps:
                        settings.car_time_list.sort()

                        player_time_table(settings.car_time_list[0], settings.car_time_list[2], match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        settings.car_time_list.clear()
                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()
                        check_new_game()
                        game_first_map_solo()

            pygame.display.update()


def game_second_map_solo(lap=0, match_time=0):
    settings.max_laps = 3
    settings.car_start_time = 0

    settings.car_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap - Solo")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        settings.started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (580, 795))
            game_screen.blit(second_map_border, (0, 0))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)

            car.car_info()

            check_car_type(car)

            car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            player_key_binds(car, car_rect, enemy_rect, second_map_border)

            collision_solo(car, second_map_border)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)
                        settings.car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_second_map_solo()

                    if lap == settings.max_laps:
                        settings.car_time_list.sort()

                        player_time_table(settings.car_time_list[0], settings.car_time_list[2], match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        settings.car_time_list.clear()
                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()
                        check_new_game()
                        game_second_map_solo()

            pygame.display.update()


def mode_selection():
    pygame.display.set_caption("2D Racing Game - Mode Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MODE SELECTION", second_font, "white", 640, 100, game_screen)

        against_pc = Button(button_image=button_image, x_y=(760, 420),
                            button_text="VERSUS PC", font=font, font_color="white")

        one_vs_one = Button(button_image=button_image, x_y=(1160, 420),
                            button_text="1 VS 1", font=font, font_color="white")

        solo = Button(button_image=button_image, x_y=(960, 580),
                      button_text="SOLO", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(960, 950),
                             button_text="BACK", font=font, font_color="white")

        solo.button_render(game_screen)
        against_pc.button_render(game_screen)
        one_vs_one.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo.on_click(mouse_coordinates):
                    solo_map_selection()

                if against_pc.on_click(mouse_coordinates):
                    vs_map_selection()

                if one_vs_one.on_click(mouse_coordinates):
                    test_map()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def test_map(lap=0, match_time=0):
    settings.max_laps = 3
    settings.car_start_time = 0

    settings.car_time_list = []
    settings.enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap")

    settings.countdown = 5
    settings.last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        settings.started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - settings.car_start_time
            stopwatch = stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (580, 849))

            start_countdown(car, enemy_car)

            game_info(match_time, clock, lap, stopwatch)

            car.car_info()

            check_car_type(car)

            car.render_position(game_screen)
            enemy_car.render_position(game_screen)

            pygame.display.update()
            start_game()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            car_rect = get_car_rect(car.car_image, car.car_angle, car.x, car.y)
            enemy_rect = get_enemy_rect(enemy_car.car_image, enemy_car.car_angle, enemy_car.x, enemy_car.y)

            player_key_binds(car, car_rect, enemy_rect, first_map_border)
            enemy_key_binds(enemy_car, car_rect, enemy_rect, first_map_border)

            collision_vs_player(car, enemy_car, car_rect, enemy_rect, first_map_border)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            settings.car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        settings.car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        settings.car_time_list.clear()
                        settings.enemy_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0

                        car.respawn_first_map()
                        enemy_car.respawn()

                        settings.car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map()

                    if lap == settings.max_laps:
                        settings.car_time_list.sort()
                        settings.enemy_time_list.sort()
                        player_time_table(settings.car_time_list[0], settings.car_time_list[2], match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        settings.car_time_list.clear()
                        settings.enemy_time_list.clear()

                        lap = 0

                        pygame.display.update()
                        match_time = 0

                        car.respawn_first_map()
                        enemy_car.respawn()

                        settings.car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map()

            pygame.display.update()


def solo_map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", second_font, "white", 680, 100, game_screen)
        draw_text("FIRST MAP", small_font, "grey", 430, 450, game_screen)
        draw_text("SECOND MAP", small_font, "grey", 1300, 350, game_screen)

        first_map_button = Button(button_image=first_map_image, x_y=(600, 550),
                                  button_text="", font=font, font_color="white")

        second_map_button = Button(button_image=second_map_image, x_y=(1350, 550),
                                   button_text="", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(960, 950),
                             button_text="BACK", font=font, font_color="white")

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map_solo()
                if second_map_button.on_click(mouse_coordinates):
                    game_second_map_solo()
                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def vs_map_selection():
    pygame.display.set_caption("2D Racing Game - Map Selection")

    while True:

        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("MAP SELECTION", second_font, "white", 680, 100, game_screen)
        draw_text("FIRST MAP", small_font, "grey", 430, 450, game_screen)
        draw_text("SECOND MAP", small_font, "grey", 1300, 350, game_screen)

        first_map_button = Button(button_image=first_map_image, x_y=(600, 550),
                                  button_text="", font=font, font_color="white")

        second_map_button = Button(button_image=second_map_image, x_y=(1350, 550),
                                   button_text="", font=font, font_color="white")

        back_button = Button(button_image=button_image, x_y=(960, 950),
                             button_text="BACK", font=font, font_color="white")

        first_map_button.button_render(game_screen)
        second_map_button.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_map_button.on_click(mouse_coordinates):
                    game_first_map()
                if second_map_button.on_click(mouse_coordinates):
                    game_second_map()
                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def car_selection():
    pygame.display.set_caption("2D Racing Game - Car Selection")

    while True:
        game_screen.blit(menu_background, (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        draw_text("CAR SELECTION", second_font, "white", 720, 100, game_screen)
        draw_text("FORMULA", small_font, "white", 770, 330, game_screen)
        draw_text("LAMBORGHINI", small_font, "white", 1150, 330, game_screen)

        formula_button = Button(x_y=(800, 550), button_image=formula_selection, button_text="", font=small_font,
                                font_color="white")
        lambo_button = Button(x_y=(1200, 550), button_image=lambo_selection, button_text="", font=small_font,
                              font_color="white")

        back_button = Button(button_image=button_image, x_y=(1000, 900),
                             button_text="BACK", font=font, font_color="white")

        formula_button.button_render(game_screen)
        lambo_button.button_render(game_screen)
        back_button.button_render(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if formula_button.on_click(mouse_coordinates):
                    settings.car_type = 0
                    settings.car_type = 1
                    draw_text("Car Choosen!", font, "green", 830, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if lambo_button.on_click(mouse_coordinates):
                    settings.car_type = 0
                    settings.car_type = 2
                    draw_text("Car Choosen!", font, "green", 830, 230, game_screen)
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

        draw_text("MAIN MENU", second_font, "white", 750, 100, game_screen)

        play_button = Button(button_image=button_image, x_y=(960, 350), button_text="PLAY", font=font,
                             font_color="white")

        car_selection_button = Button(button_image=button_image, x_y=(960, 500), button_text="CHOOSE CAR", font=font,
                                      font_color="white")

        quit_button = Button(button_image=button_image, x_y=(960, 950), button_text="QUIT", font=font,
                             font_color="white")

        play_button.button_render(game_screen)
        car_selection_button.button_render(game_screen)
        quit_button.button_render(game_screen)

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
