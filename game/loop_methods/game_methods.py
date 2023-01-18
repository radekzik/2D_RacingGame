import game.sounds.sounds
from game.config.settings import FIRST_FINISH_LINE_X_RANGE, SECOND_FINISH_LINE_X_RANGE, SECOND_FINISH_LINE_Y_RANGE, \
    FIRST_FINISH_LINE_Y_RANGE
from game.storage import storing_data
from game.ui import draw, load_image
from game.ui.load_image import *
from game.ui.draw import *
from game.config import settings

pygame.init()


def collision_solo(car, map_border):
    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()
        check_audio(game.sounds.sounds.out_off_the_track_sound.play)


def collision_vs_pc(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch,
                    car_time_list, enemy_time_list, restart_map):
    if car_rect.colliderect(enemy_rect):
        # pygame.draw.rect(game_screen, "green", enemy_rect)
        # pygame.draw.rect(game_screen, "red", car_rect)
        car.car_collide()
        check_audio(game.sounds.sounds.crash_sound.play)

    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()
        check_audio(game.sounds.sounds.out_off_the_track_sound.play)
        # pygame.draw.rect(game_screen, (255, 0, 0), car_rect)

    # if enemy_car.border_collide(pygame.mask.from_surface(map_border)):
    # enemy_car.border_collision()
    # check_audio(game.sounds.sounds.out_off_the_track_sound.play)
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
            draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1000)

            stats_reset_vs_pc(car, enemy_car, car_time_list, enemy_time_list)
            check_new_game()
            restart_map()

        if settings.car_lap > settings.enemy_lap:
            draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1000)

            stats_reset_vs_pc(car, enemy_car, car_time_list, enemy_time_list)
            check_new_game()
            restart_map()


def collision_vs_player(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch,
                        car_time_list, enemy_time_list, restart_map):
    if car_rect.colliderect(enemy_rect):
        car.car_collide()
        check_audio(game.sounds.sounds.crash_sound.play)
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if enemy_rect.colliderect(car_rect):
        enemy_car.car_collide()
        # check_audio(game.sounds.sounds.crash_sound.play)
    else:
        enemy_car.car_image = enemy_car.car_image
        enemy_car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()
        check_audio(game.sounds.sounds.out_off_the_track_sound.play)

    if enemy_car.border_collide(pygame.mask.from_surface(map_border)):
        enemy_car.out_of_track()
        check_audio(game.sounds.sounds.out_off_the_track_sound.play)


def check_new_game():
    settings.started = False

    while not settings.started:
        GAME_SCREEN.blit(time_background, (700, 200))
        draw_text("PLAY AGAIN - SPACE", normal_font, "white", 740, 250, GAME_SCREEN)
        draw_text("EXIT TO MENU - X", normal_font, "cyan", 740, 350, GAME_SCREEN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = 1
                settings.car_start_time = pygame.time.get_ticks()


def check_car_type(car):
    for x in range(12):
        x += 1
        if settings.car_type == x:
            car.car_image = car.player_cars(x - 1)


def check_audio(command):
    if settings.audio == 1:
        command()


def check_show_fps(command, clock):
    if settings.show_fps == 1:
        command(clock)


def check_show_ui(command):
    if settings.show_ui == 1:
        command()


def car_stopwatch(ticks):
    stopwatch = ticks - settings.car_start_time
    stopwatch = stopwatch // 100 / 10

    return stopwatch


def enemy_stopwatch(ticks):
    stopwatch = ticks - settings.enemy_start_time
    stopwatch = stopwatch // 100 / 10

    return stopwatch


def speedometer(car):
    if car.car_speed < 0:
        GAME_SCREEN.blit(speedometr, (1730, 900))
    if car.car_speed == 0:
        GAME_SCREEN.blit(speedometr_0, (1730, 900))
    if 0 < car.car_speed <= 1:
        GAME_SCREEN.blit(speedometr_1, (1730, 900))
    if 1 < car.car_speed <= 2:
        GAME_SCREEN.blit(speedometr_2, (1730, 900))
    if 2 < car.car_speed <= 3:
        GAME_SCREEN.blit(speedometr_3, (1730, 900))
    if 3 < car.car_speed <= 10:
        GAME_SCREEN.blit(speedometr_nitro, (1730, 900))


def start_game():
    while not settings.started:
        draw_text(f"PRESS ANY KEY TO START", medium_font, "orange", 800, 600, GAME_SCREEN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = 1
                check_audio(game.sounds.sounds.starting_sound.play)
                settings.car_start_time = pygame.time.get_ticks()


def start_countdown(car, enemy_car):
    if settings.countdown > 0:

        count_timer = pygame.time.get_ticks()
        car.max_speed = 0
        car.car_nitro = 0
        # car.movement_speed = 0

        enemy_car.max_speed = 0
        enemy_car.car_nitro = 0
        enemy_car.movement_speed = 0

        if count_timer - settings.last_count > 1000:
            settings.countdown -= 1
            settings.last_count = count_timer

    if settings.countdown == 5 or settings.countdown == 4:
        GAME_SCREEN.blit(semaphor_all_red, (880, 500))

    if settings.countdown == 4:
        check_audio(game.sounds.sounds.countdown_sound.play)

    if settings.countdown == 3:
        draw_text(f"{str(settings.countdown)} - READY", normal_font, "red", 850, 570, GAME_SCREEN)
        GAME_SCREEN.blit(semaphor_red, (880, 500))

    if settings.countdown == 2:
        draw_text(f"{str(settings.countdown)} - STEADY", normal_font, "orange", 850, 570, GAME_SCREEN)
        GAME_SCREEN.blit(semaphor_orange, (880, 500))

    if settings.countdown == 1:
        draw_text(f"{str(settings.countdown)} - GO!", normal_font, "green", 880, 570, GAME_SCREEN)
        GAME_SCREEN.blit(semaphor_green, (880, 500))

    if settings.countdown == 0:
        # draw_text(f"", font, "white", 900, 500)

        check_audio(game.sounds.sounds.starting_sound.stop)
        check_audio(game.sounds.sounds.countdown_sound.stop)
        car.max_speed = 3
        car.car_nitro = 5
        car.max_movement_speed = 5

        enemy_car.max_speed = 3
        enemy_car.car_nitro = 5
        enemy_car.max_movement_speed = 5


def stats_reset_vs_pc(car, enemy, car_time_list, enemy_time_list):
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


def stats_reset_solo(car, car_time_list):
    car_time_list.clear()

    settings.car_lap = 0
    settings.enemy_lap = 0
    settings.car_match_time = 0
    settings.enemy_match_time = 0

    car.respawn_first_map()
    settings.car_start_time = pygame.time.get_ticks()
    settings.enemy_start_time = pygame.time.get_ticks()


def check_laps(car, pc_car, car_stopwatch, reset_map, map_respawn):
    if car_stopwatch > 5:
        settings.car_lap += 1

        for time_position in range(0, 1):
            time_position += 1
            settings.car_time_list.insert(time_position, car_stopwatch)

        settings.car_match_time = settings.car_match_time + car_stopwatch

        draw_text(f"Lap Time - {car_stopwatch}", normal_font, "white", 800, 450, GAME_SCREEN)
        pygame.display.update()
        pygame.time.wait(200)

        map_respawn(car)
        settings.car_start_time = pygame.time.get_ticks()

    else:
        draw_text(f"Wrong Way", normal_font, "white", 800, 450, GAME_SCREEN)

        pygame.display.update()
        pygame.time.wait(1000)

        if pc_car is not None:
            stats_reset_vs_pc(car, pc_car, settings.car_time_list, settings.enemy_time_list)
        else:
            stats_reset_solo(car, settings.car_time_list)

        check_new_game()
        reset_map()


def end_game(car, pc_car, reset_map, lap_filename, match_filename):
    if settings.car_lap == settings.max_laps:
        print(settings.car_match_time)
        print(settings.enemy_match_time)
        print(settings.car_lap)
        print(settings.max_laps)

        if settings.car_lap > settings.enemy_lap:
            draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1000)

        if settings.car_lap < settings.enemy_lap:
            draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1000)

        settings.car_time_list.sort()
        settings.enemy_time_list.sort()
        draw.player_time_table(settings.car_time_list[0], settings.car_time_list[2],
                               settings.car_match_time)

        storing_data.save_lap_time(settings.car_time_list[0], lap_filename)
        storing_data.save_match_time(settings.car_match_time, match_filename)

        # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
        pygame.display.update()
        pygame.time.wait(5000)

        if pc_car is not None:
            stats_reset_vs_pc(car, pc_car, settings.car_time_list, settings.enemy_time_list)
        else:
            stats_reset_solo(car, settings.car_time_list)

        check_new_game()
        reset_map()
