
from game.storage import storing_data
from game.ui import draw
from game.ui.load_image import *
from game.cars.rects import *
from game.ui.draw import *
from game.config import settings


pygame.init()


def collision_solo(car, map_border):
    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()


def collision_vs_pc(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch, car_time_list, enemy_time_list
                    , restart_map):
    if car_rect.colliderect(enemy_rect):
        # pygame.draw.rect(game_screen, "green", enemy_rect)
        # pygame.draw.rect(game_screen, "red", car_rect)
        car.car_collide()

    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()
        # pygame.draw.rect(game_screen, (255, 0, 0), car_rect)

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
            draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)

            stats_reset(car, enemy_car, car_time_list, enemy_time_list)
            check_new_game()
            restart_map()

        if settings.car_lap > settings.enemy_lap:
            draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)

            stats_reset(car, enemy_car, car_time_list, enemy_time_list)
            check_new_game()
            restart_map()


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
        draw_text("PLAY AGAIN - SPACE", normal_font, "white", 740, 250, game_screen)
        draw_text("EXIT TO MENU - X", normal_font, "cyan", 740, 350, game_screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = True
                settings.car_start_time = pygame.time.get_ticks()


def check_car_type(car):
    # formula
    if settings.car_type == 1:
        car.car_blue_formula()
    if settings.car_type == 2:
        car.car_orange_formula()
    if settings.car_type == 3:
        car.car_yellow_formula()
    if settings.car_type == 4:
        car.car_green_formula()

    # lambo
    if settings.car_type == 5:
        car.car_blue_lambo()
    if settings.car_type == 6:
        car.car_cyan_lambo()
    if settings.car_type == 7:
        car.car_red_lambo()
    if settings.car_type == 8:
        car.car_pink_lambo()

    # spoiler car
    if settings.car_type == 9:
        car.spoiler_car_dark_purple()
    if settings.car_type == 10:
        car.spoiler_car_light_blue()
    if settings.car_type == 11:
        car.spoiler_car_orange()
    if settings.car_type == 12:
        car.spoiler_car_pink()


def start_game():
    while not settings.started:
        draw_text(f"PRESS ANY KEY TO START", medium_font, "orange", 800, 600, game_screen)

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
        draw_text(f"{str(settings.countdown)} - READY", normal_font, "red", 850, 570, game_screen)
        game_screen.blit(semaphor_red, (880, 500))

    if settings.countdown == 2:
        draw_text(f"{str(settings.countdown)} - STEADY", normal_font, "orange", 850, 570, game_screen)
        game_screen.blit(semaphor_orange, (880, 500))

    if settings.countdown == 1:
        draw_text(f"{str(settings.countdown)} - GO!", normal_font, "green", 880, 570, game_screen)
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


def check_laps(car, pc_car, car_stopwatch, reset_map, map_respawn):
    if car_stopwatch > 5:
        settings.car_lap += 1

        for time_position in range(0, 1):
            time_position += 1
            settings.car_time_list.insert(time_position, car_stopwatch)

        settings.car_match_time = settings.car_match_time + car_stopwatch

        draw_text(f"Lap Time - {car_stopwatch}", normal_font, "white", 800, 450, game_screen)
        pygame.display.update()
        pygame.time.wait(200)

        map_respawn()
        settings.car_start_time = pygame.time.get_ticks()

    else:
        draw_text(f"Wrong Way", normal_font, "white", 800, 450, game_screen)

        pygame.display.update()
        pygame.time.wait(1000)

        stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)

        check_new_game()
        reset_map()


def end_game(car, pc_car, reset_map):
    if settings.car_lap == settings.max_laps:
        print(settings.car_match_time)
        print(settings.enemy_match_time)
        print(settings.car_lap)
        print(settings.max_laps)

        if settings.car_lap > settings.enemy_lap:
            draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)

        if settings.car_lap < settings.enemy_lap:
            draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)

        settings.car_time_list.sort()
        settings.enemy_time_list.sort()
        draw.player_time_table(settings.car_time_list[0], settings.car_time_list[2],
                               settings.car_match_time)

        storing_data.save_lap_time(settings.car_time_list[0])
        storing_data.save_match_time(settings.car_match_time)

        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
        pygame.display.update()
        pygame.time.wait(5000)
        stats_reset(car, pc_car, settings.car_time_list, settings.enemy_time_list)
        check_new_game()
        reset_map()
