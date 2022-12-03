from button import Button
from resolution import draw_text
from load_image import *
from player import Player
from enemy import EnemyPlayer
from pc import PCPlayer
from rects import *

pygame.init()


def player_key_binds(car, car_rect, enemy_rect, map_border):
    global animation_value
    stopwatch = pygame.time.get_ticks() - car_start_time
    stopwatch = stopwatch // 100 / 10
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_w]:
        car.forward_control()
        car_animation(stopwatch, car)

    else:
        car.forward_slowdown()

    if pressed_key[pygame.K_s]:
        car.backward_control()
    else:
        car.forward_slowdown()

    if pressed_key[pygame.K_d]:
        car.rotate_right()

    if pressed_key[pygame.K_a]:
        car.rotate_left()

    if pressed_key[pygame.K_q]:
        car.drift()
    else:
        car.movement_speed = 2.5

    if pressed_key[pygame.K_x]:
        mode_selection()

    if pressed_key[pygame.K_w]:
        if pressed_key[pygame.K_e] and not car.border_collide(pygame.mask.from_surface(map_border)) \
                and not car_rect.colliderect(enemy_rect):
            car.nitro()


def enemy_key_binds(enemy_car, car_rect, enemy_rect, map_border):
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_i]:
        enemy_car.forward_control()
    else:
        enemy_car.forward_slowdown()

    if pressed_key[pygame.K_k]:
        enemy_car.backward_control()
    else:
        enemy_car.forward_slowdown()

    if pressed_key[pygame.K_l]:
        enemy_car.rotate_right()

    if pressed_key[pygame.K_j]:
        enemy_car.rotate_left()

    if pressed_key[pygame.K_u]:
        enemy_car.drift()
    else:
        enemy_car.movement_speed = 2.5

    if pressed_key[pygame.K_x]:
        mode_selection()

    if pressed_key[pygame.K_i]:
        if pressed_key[pygame.K_o] and not enemy_car.border_collide(pygame.mask.from_surface(map_border)) \
                and not enemy_rect.colliderect(car_rect):
            enemy_car.nitro()


def game_info(match_time, clock, lap, stopwatch):
    draw_text("W - Forward", small_font, "white", 70, 40, game_screen)
    draw_text("S - Backward", small_font, "white", 70, 70, game_screen)
    draw_text("A - Left", small_font, "white", 70, 100, game_screen)
    draw_text("D - Right", small_font, "white", 70, 130, game_screen)
    draw_text("X - Exit", small_font, "white", 190, 40, game_screen)
    draw_text("E - Nitro", small_font, "white", 190, 70, game_screen)
    draw_text("Q - Drift", small_font, "white", 190, 100, game_screen)
    draw_text(f"LAP TIME - {stopwatch}", small_font, "white", 1670, 900, game_screen)
    draw_text(f"MATCH TIME - {match_time}", small_font, "white", 1670, 850, game_screen)
    draw_text(f"FPS - {round(clock.get_fps())}", small_font, "white", 1780, 40, game_screen)
    draw_text(f"LAP - {lap} / 3", small_font, "white", 1690, 800, game_screen)


def player_time_table(fastest_time, slowest_time, match_time):
    game_screen.blit(time_menu, (650, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", font, "white", 740, 250, game_screen)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", font, "white", 740, 350, game_screen)
    draw_text(f"MATCH TIME : {round(match_time)}", font, "white", 740, 450, game_screen)


def enemy_time_table(fastest_time, slowest_time, match_time):
    game_screen.blit(time_menu, (1050, 200))
    draw_text(f"FASTEST LAP TIME : {fastest_time}", font, "white", 1150, 250, game_screen)
    draw_text(f"SLOWEST LAP TIME : {slowest_time}", font, "white", 1150, 350, game_screen)
    draw_text(f"MATCH TIME : {round(match_time)}", font, "white", 1150, 450, game_screen)


def collision_solo(car, map_border):
    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()


def collision_vs_pc(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch, car_time_list, enemy_time_list):
    global enemy_lap
    global enemy_start_time
    global enemy_match_time

    if car_rect.colliderect(enemy_rect):
        car.car_collide()
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()

    if FIRST_FINISH_LINE_X_RANGE < enemy_car.x < SECOND_FINISH_LINE_X_RANGE:
        if FIRST_FINISH_LINE_Y_RANGE < enemy_car.y < SECOND_FINISH_LINE_Y_RANGE:
            enemy_lap += 1
            enemy_start_time = pygame.time.get_ticks()
            enemy_match_time = enemy_match_time + enemy_stopwatch
            enemy_car.respawn_first_map()
            enemy_car.next_route_position = 0
            enemy_car.start_drive()

    if enemy_lap == max_laps:
        print(enemy_lap)
        if car_lap < enemy_lap:
            draw_text(f"YOU LOST THE RACE!", font, "red", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)
        if car_lap > enemy_lap:
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
    global started
    global car_start_time

    started = False

    while not started:
        game_screen.blit(time_menu, (700, 200))
        draw_text("PLAY AGAIN - SPACE", font, "white", 740, 250, game_screen)
        draw_text("EXIT TO MENU - X", font, "white", 740, 350, game_screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                started = True
                car_start_time = pygame.time.get_ticks()


def check_car_type(car):
    if car_type == 1:
        car.first_map_car()
    if car_type == 2:
        car.second_map_car()


def car_animation(stopwatch, car):
    global car_type

    if car_type == 1:
        if stopwatch % 2 == 0:
            car.car_image = blue_formula
            car.render_position(game_screen)
            pygame.display.update()

        if stopwatch % 3 == 0:
            car.car_image = blue_formula_2
            car.render_position(game_screen)
            pygame.display.update()

    if car_type == 2:
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


def start_game():
    global started
    global car_start_time

    while not started:
        draw_text(f"Press Any Key To Start", font, "white", 70, 220, game_screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                started = True
                car_start_time = pygame.time.get_ticks()


def start_countdown(car, enemy_car):
    global countdown
    global last_count

    if countdown > 0:

        count_timer = pygame.time.get_ticks()
        car.max_speed = 0
        car.car_nitro = 0
        car.movement_speed = 0

        enemy_car.max_speed = 0
        enemy_car.car_nitro = 0
        enemy_car.movement_speed = 0

        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer

    if countdown == 5 or countdown == 4:
        game_screen.blit(semaphor_all_red, (880, 500))

    if countdown == 3:
        draw_text(f"{str(countdown)} - READY", font, "red", 850, 570, game_screen)
        game_screen.blit(semaphor_red, (880, 500))

    if countdown == 2:
        draw_text(f"{str(countdown)} - STEADY", font, "orange", 850, 570, game_screen)
        game_screen.blit(semaphor_orange, (880, 500))

    if countdown == 1:
        draw_text(f"{str(countdown)} - GO!", font, "green", 880, 570, game_screen)
        game_screen.blit(semaphor_green, (880, 500))

    if countdown == 0:
        # draw_text(f"", font, "white", 900, 500)

        car.max_speed = 3
        car.car_nitro = 5
        car.max_movement_speed = 2.5

        enemy_car.max_speed = 3
        enemy_car.car_nitro = 5
        enemy_car.max_movement_speed = 2.5


def stats_reset(car, enemy, car_time_list, enemy_time_list):
    global car_lap
    global car_match_time
    global car_start_time
    global enemy_start_time
    global enemy_match_time
    global enemy_lap

    car_time_list.clear()
    enemy_time_list.clear()

    car_lap = 0
    enemy_lap = 0
    car_match_time = 0
    enemy_match_time = 0

    car.respawn_first_map()
    enemy.respawn_first_map()
    enemy.next_route_position = 0
    car_start_time = pygame.time.get_ticks()
    enemy_start_time = pygame.time.get_ticks()


def game_first_map():
    global car_type
    global started
    global countdown
    global last_count
    global car_start_time
    global enemy_start_time
    global enemy_lap
    global animation_value
    global max_laps
    global car_lap
    global car_match_time
    global enemy_match_time

    max_laps = 3
    car_lap = 0
    enemy_lap = 0

    animation_value = 0
    car_start_time = 0
    enemy_start_time = 0
    car_match_time = 0
    enemy_match_time = 0

    car_time_list = []
    enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap - VS PC")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        pc_car = PCPlayer()

        started = False

        while game_loop:

            clock.tick(60)

            car_stopwatch = pygame.time.get_ticks() - car_start_time
            car_stopwatch = car_stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(first_map, (0, 0))
            game_screen.blit(finish_line, (580, 840))

            start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.first_map_route()

            game_info(car_match_time, clock, car_lap, car_stopwatch)

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
            collision_vs_pc(car, pc_car, car_rect, enemy_rect, first_map_border, enemy_stopwatch, car_time_list,
                            enemy_time_list)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if car_stopwatch > 5:

                        car_lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            car_time_list.insert(time_position, car_stopwatch)
                        car_match_time = car_match_time + car_stopwatch
                        draw_text(f"Lap Time - {car_stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        stats_reset(car, pc_car, car_time_list, enemy_time_list)

                        check_new_game()
                        game_first_map()

                    if car_lap == max_laps:
                        print(car_match_time)
                        print(enemy_match_time)
                        print(car_lap)
                        print(max_laps)

                        if car_lap > enemy_lap:
                            draw_text(f"YOU WON THE RACE!", font, "gold", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        if car_lap < enemy_lap:
                            draw_text(f"YOU LOST THE RACE!", font, "red", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        car_time_list.sort()
                        enemy_time_list.sort()
                        player_time_table(car_time_list[0], car_time_list[2], car_match_time)
                        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        stats_reset(car, pc_car, car_time_list, enemy_time_list)
                        check_new_game()
                        game_first_map()

        animation_value += 1
        pygame.display.update()


def game_second_map():
    global car_type
    global started
    global countdown
    global last_count
    global car_start_time
    global enemy_start_time
    global enemy_lap
    global animation_value
    global max_laps
    global car_lap
    global car_match_time
    global enemy_match_time

    max_laps = 3
    car_lap = 0
    enemy_lap = 0

    animation_value = 0
    car_start_time = 0
    enemy_start_time = 0
    car_match_time = 0
    enemy_match_time = 0

    car_time_list = []
    enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap - VS PC")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        pc_car = PCPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - car_start_time
            stopwatch = stopwatch // 100 / 10

            enemy_stopwatch = pygame.time.get_ticks() - enemy_start_time
            enemy_stopwatch = enemy_stopwatch // 100 / 10

            game_screen.blit(menu_background, (0, 0))
            game_screen.blit(second_map, (0, 0))
            game_screen.blit(finish_line, (580, 795))
            game_screen.blit(second_map_border, (0, 0))

            start_countdown(car, pc_car)
            pc_car.start_drive()
            pc_car.second_map_route()

            game_info(car_match_time, clock, car_lap, stopwatch)

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

            collision_vs_pc(car, pc_car, car_rect, enemy_rect, second_map_border, enemy_stopwatch, car_time_list,
                            enemy_time_list)

            if FIRST_FINISH_LINE_X_RANGE < car.x < SECOND_FINISH_LINE_X_RANGE:
                if FIRST_FINISH_LINE_Y_RANGE < car.y < SECOND_FINISH_LINE_Y_RANGE:
                    if stopwatch > 5:

                        car_lap += 1
                        for time_position in range(0, 1):
                            time_position += 1
                            car_time_list.insert(time_position, stopwatch)
                        car_match_time = car_match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        stats_reset(car, pc_car, car_time_list, enemy_time_list)

                        check_new_game()
                        game_second_map()

                    if car_lap == max_laps:

                        if car_lap > enemy_lap:
                            draw_text(f"YOU WON THE RACE!", font, "gold", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        if car_lap < enemy_lap:
                            draw_text(f"YOU LOST THE RACE!", font, "red", 800, 600, game_screen)

                            pygame.display.update()
                            pygame.time.wait(1000)

                        car_time_list.sort()
                        enemy_time_list.sort()
                        player_time_table(car_time_list[0], car_time_list[2], car_match_time)
                        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        stats_reset(car, pc_car, car_time_list, enemy_time_list)
                        check_new_game()
                        game_second_map()

            animation_value += 1
            pygame.display.update()


def game_first_map_solo(lap=0, match_time=0):
    global car_type
    global max_laps
    global started
    global countdown
    global last_count
    global car_start_time

    max_laps = 3
    car_start_time = 0

    car_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap - Solo")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - car_start_time
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
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)
                        car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map_solo()

                    if lap == max_laps:
                        car_time_list.sort()

                        player_time_table(car_time_list[0], car_time_list[2], match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()
                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()
                        check_new_game()
                        game_first_map_solo()

            pygame.display.update()


def game_second_map_solo(lap=0, match_time=0):
    global car_type
    global max_laps
    global started
    global countdown
    global last_count
    global car_start_time

    max_laps = 3
    car_start_time = 0

    car_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - SecondMap - Solo")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - car_start_time
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
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)
                        car_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_second_map_solo()

                    if lap == max_laps:
                        car_time_list.sort()

                        player_time_table(car_time_list[0], car_time_list[2], match_time)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()
                        lap = 0
                        pygame.display.update()
                        match_time = 0
                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()
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
    global car_type
    global max_laps
    global started
    global countdown
    global last_count
    global car_start_time

    max_laps = 3
    car_start_time = 0

    car_time_list = []
    enemy_time_list = []

    game_loop = True

    pygame.display.set_caption("2D Racing Game - FirstMap")

    countdown = 5
    last_count = pygame.time.get_ticks()

    while True:

        clock = pygame.time.Clock()

        car = Player()
        enemy_car = EnemyPlayer()

        started = False

        while game_loop:

            clock.tick(240)

            stopwatch = pygame.time.get_ticks() - car_start_time
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
                            car_time_list.insert(time_position, stopwatch)

                        match_time = match_time + stopwatch
                        draw_text(f"Lap Time - {stopwatch}", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(200)

                        car.respawn_first_map()
                        car_start_time = pygame.time.get_ticks()

                    else:
                        draw_text(f"Wrong Way", font, "white", 800, 450, game_screen)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0
                        pygame.display.update()
                        match_time = 0

                        car.respawn_first_map()
                        enemy_car.respawn()

                        car_start_time = pygame.time.get_ticks()

                        check_new_game()
                        game_first_map()

                    if lap == max_laps:
                        car_time_list.sort()
                        enemy_time_list.sort()
                        player_time_table(car_time_list[0], car_time_list[2], match_time)

                        pygame.display.update()
                        pygame.time.wait(5000)
                        car_time_list.clear()
                        enemy_time_list.clear()

                        lap = 0

                        pygame.display.update()
                        match_time = 0

                        car.respawn_first_map()
                        enemy_car.respawn()

                        car_start_time = pygame.time.get_ticks()

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
    global car_type

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
                    car_type = 0
                    car_type = 1
                    draw_text("Car Choosen!", font, "white", 830, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if lambo_button.on_click(mouse_coordinates):
                    car_type = 0
                    car_type = 2
                    draw_text("Car Choosen!", font, "white", 830, 230, game_screen)
                    pygame.display.update()
                    pygame.time.wait(2000)
                    mode_selection()

                if back_button.on_click(mouse_coordinates):
                    main_menu()

            pygame.display.update()


def main_menu():
    global car_type
    car_type = 1
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
