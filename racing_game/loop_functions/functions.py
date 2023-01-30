import racing_game.sounds.sounds
from racing_game.storage.data_processing import DataProcessing
from racing_game.ui.loading_images import *
from racing_game.ui.draw_ui import *

pygame.init()


class Collisions:

    @staticmethod
    def collision_solo(car, map_border, restart_map):
        if car.border_collide(pygame.mask.from_surface(map_border)):
            # car.out_of_track()

            # check_audio(racing_game.sounds.sounds.out_off_the_track_sound.play)

            DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.lose.play)

            DrawUI.draw_text("YOU HIT A BARRIER!", normal_font, "orange", 800, 600, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(500)

            LoopFunctions.check_new_game()
            restart_map()

    @staticmethod
    def collision_vs_pc(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch,
                        car_time_list, enemy_time_list, restart_map, player_respawn, enemy_respawn,
                        x_range1, x_range2, y_range1, y_range2,):
        if car_rect.colliderect(enemy_rect):
            car.car_collide()
            DrawUI.check_audio(racing_game.sounds.sounds.crash_sound.play)

        else:
            car.car_image = car.car_image
            car.max_speed = 3

        if car.border_collide(pygame.mask.from_surface(map_border)):
            car.out_of_track()

            DrawUI.check_audio(racing_game.sounds.sounds.out_off_the_track_sound.play)

        if x_range1 < enemy_car.x < x_range2:
            if y_range1 < enemy_car.y < y_range2:
                Settings.enemy_lap += 1
                Settings.enemy_start_time = pygame.time.get_ticks()
                Settings.enemy_match_time = Settings.enemy_match_time + enemy_stopwatch
                enemy_respawn(enemy_car)
                enemy_car.next_route_position = 0
                enemy_car.start_drive()

        if Settings.enemy_lap == Settings.max_laps:
            print(Settings.enemy_lap)
            if Settings.car_lap < Settings.enemy_lap:
                DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
                DrawUI.check_audio(racing_game.sounds.sounds.lose.play)
                GAME_SCREEN.blit(button_win_lose, (770, 560))
                DrawUI.draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, GAME_SCREEN)

                pygame.display.update()
                pygame.time.wait(1000)

                LoopFunctions.stats_reset_vs_pc(car, enemy_car, car_time_list, enemy_time_list, player_respawn,
                                                enemy_respawn)
                LoopFunctions.check_new_game()
                restart_map()

            if Settings.car_lap > Settings.enemy_lap:
                DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
                DrawUI.check_audio(racing_game.sounds.sounds.win.play)
                GAME_SCREEN.blit(button_win_lose, (770, 560))
                DrawUI.draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, GAME_SCREEN)

                pygame.display.update()
                pygame.time.wait(1000)

                LoopFunctions.stats_reset_vs_pc(car, enemy_car, car_time_list, enemy_time_list, player_respawn,
                                                enemy_respawn)
                LoopFunctions.check_new_game()
                restart_map()

    @staticmethod
    def collision_vs_player(car, enemy_car, car_rect, enemy_rect, map_border):
        if car_rect.colliderect(enemy_rect):
            car.car_collide()
            DrawUI.check_audio(racing_game.sounds.sounds.crash_sound.play)

        if enemy_rect.colliderect(car_rect):
            enemy_car.car_collide()
            DrawUI.check_audio(racing_game.sounds.sounds.crash_sound.play)

        if car.border_collide(pygame.mask.from_surface(map_border)):
            car.out_of_track()
            DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.out_off_the_track_sound.play)

        if enemy_car.border_collide(pygame.mask.from_surface(map_border)):
            enemy_car.out_of_track()
            DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.out_off_the_track_sound.play)


# LOOP METHODS----------------------------------------------------------------------------------------------------------

class LoopFunctions:

    @staticmethod
    def check_new_game():
        Settings.started = False

        while not Settings.started:
            GAME_SCREEN.blit(time_background, (700, 200))
            DrawUI.draw_text("PLAY AGAIN - SPACE", normal_font, "white", 740, 250, GAME_SCREEN)
            DrawUI.draw_text("EXIT TO MENU - X", normal_font, "cyan", 740, 350, GAME_SCREEN)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Settings.started = 1
                    Settings.car_start_time = pygame.time.get_ticks()

    @staticmethod
    def start_game():
        while not Settings.started:
            DrawUI.draw_text(f"PRESS ANY KEY TO START", medium_font, "orange", 800, 600, GAME_SCREEN)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    Settings.started = 1
                    DrawUI.check_audio(racing_game.sounds.sounds.starting_sound.play)
                    Settings.car_start_time = pygame.time.get_ticks()
                    Settings.enemy_start_time = pygame.time.get_ticks()
                    DrawUI.check_audio_set_volume(racing_game.sounds.sounds.car_engine.play, -1)

    @staticmethod
    def start_countdown(car, enemy_car):
        if Settings.countdown > 0:

            count_timer = pygame.time.get_ticks()
            car.max_speed = 0

            # car.movement_speed = 0

            enemy_car.max_speed = 0

            enemy_car.movement_speed = 0

            if count_timer - Settings.last_count > 1000:
                Settings.countdown -= 1
                Settings.last_count = count_timer

        if Settings.countdown == 5 or Settings.countdown == 4:
            GAME_SCREEN.blit(semaphor_all_red, (880, 500))

        if Settings.countdown == 4:
            DrawUI.check_audio(racing_game.sounds.sounds.countdown_sound.play)

        if Settings.countdown == 3:
            DrawUI.draw_text(f"{str(Settings.countdown)} - READY", normal_font, "red", 850, 570, GAME_SCREEN)
            GAME_SCREEN.blit(semaphor_red, (880, 500))

        if Settings.countdown == 2:
            DrawUI.draw_text(f"{str(Settings.countdown)} - STEADY", normal_font, "orange", 850, 570, GAME_SCREEN)
            GAME_SCREEN.blit(semaphor_orange, (880, 500))

        if Settings.countdown == 1:
            DrawUI.draw_text(f"{str(Settings.countdown)} - GO!", normal_font, "green", 880, 570, GAME_SCREEN)
            GAME_SCREEN.blit(semaphor_green, (880, 500))

        if Settings.countdown == 0:

            DrawUI.check_audio(racing_game.sounds.sounds.starting_sound.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.countdown_sound.stop)
            car.max_speed = 3

            car.max_movement_speed = 5

            enemy_car.max_speed = 3

            enemy_car.max_movement_speed = 5

    @staticmethod
    def stats_reset_vs_pc(car, enemy, car_time_list, enemy_time_list, player_respawn, enemy_respawn):
        car_time_list.clear()
        enemy_time_list.clear()

        Settings.car_lap = 0
        Settings.enemy_lap = 0
        Settings.car_match_time = 0
        Settings.enemy_match_time = 0

        player_respawn(car)
        enemy_respawn(enemy)

        enemy.next_route_position = 0
        Settings.car_start_time = pygame.time.get_ticks()
        Settings.enemy_start_time = pygame.time.get_ticks()

    @staticmethod
    def stats_reset_solo(car, car_time_list, player_respawn):
        car_time_list.clear()

        Settings.car_lap = 0
        Settings.enemy_lap = 0
        Settings.car_match_time = 0
        Settings.enemy_match_time = 0

        player_respawn(car)
        Settings.car_start_time = pygame.time.get_ticks()
        Settings.enemy_start_time = pygame.time.get_ticks()

    @staticmethod
    def check_laps(car, pc_car, car_stopwatch, reset_map, player_respawn, enemy_respawn):
        if car_stopwatch > 5:
            Settings.car_lap += 1
            DrawUI.check_audio(racing_game.sounds.sounds.finish.play)

            for time_position in range(0, 1):
                time_position += 1
                Settings.car_time_list.insert(time_position, car_stopwatch)

            Settings.car_match_time = Settings.car_match_time + car_stopwatch

            DrawUI.draw_text(f"LAP TIME - {car_stopwatch}", normal_font, "white", 800, 450, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(200)

            player_respawn(car)
            Settings.car_start_time = pygame.time.get_ticks()

        else:
            DrawUI.check_audio(racing_game.sounds.sounds.countdown_sound.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.starting_sound.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.lose.play)
            DrawUI.draw_text(f"WRONG WAY!", normal_font, "white", 830, 450, GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1000)

            if pc_car is not None:
                LoopFunctions.stats_reset_vs_pc(car, pc_car, Settings.car_time_list, Settings.enemy_time_list,
                                                player_respawn, enemy_respawn)
            else:
                LoopFunctions.stats_reset_solo(car, Settings.car_time_list, player_respawn)

            LoopFunctions.check_new_game()
            reset_map()

    @staticmethod
    def end_game(car, pc_car, reset_map, lap_filename, match_filename, player_respawn, enemy_respawn):
        if Settings.car_lap == Settings.max_laps:

            if Settings.car_lap > Settings.enemy_lap:
                DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
                DrawUI.check_audio(racing_game.sounds.sounds.win.play)
                GAME_SCREEN.blit(button_win_lose, (770, 560))
                DrawUI.draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, GAME_SCREEN)

                pygame.display.update()
                pygame.time.wait(1000)

            if Settings.car_lap < Settings.enemy_lap:
                DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
                DrawUI.check_audio(racing_game.sounds.sounds.lose.play)
                GAME_SCREEN.blit(button_win_lose, (770, 560))
                DrawUI.draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, GAME_SCREEN)

                pygame.display.update()
                pygame.time.wait(1000)

            Settings.car_time_list.sort()
            Settings.enemy_time_list.sort()
            DrawUI.player_time_table(Settings.car_time_list[0], Settings.car_time_list[Settings.max_laps - 1],
                                     Settings.car_match_time)

            if Settings.car_time_list[0] <= 9.9:
                DataProcessing.save_lap_time(Settings.car_time_list[0], lap_filename)

            DataProcessing.save_match_time(Settings.car_match_time, match_filename)

            # enemy_time_table(enemy_time_list[0], enemy_time_list[2], enemy_match_time)
            pygame.display.update()
            pygame.time.wait(5000)

            if pc_car is not None:
                LoopFunctions.stats_reset_vs_pc(car, pc_car, Settings.car_time_list, Settings.enemy_time_list,
                                                player_respawn, enemy_respawn)
            else:
                LoopFunctions.stats_reset_solo(car, Settings.car_time_list, player_respawn)

            LoopFunctions.check_new_game()
            reset_map()

    @staticmethod
    def enemy_check_laps(pc_car, enemy_stopwatch, reset_map, enemy_respawn):
        if enemy_stopwatch > 5:
            Settings.enemy_lap += 1
            DrawUI.check_audio(racing_game.sounds.sounds.finish.play)

            for time_position in range(0, 1):
                time_position += 1
                Settings.enemy_time_list.insert(time_position, enemy_stopwatch)

            Settings.enemy_match_time = Settings.enemy_match_time + enemy_stopwatch

            DrawUI.draw_text(f"LAP TIME - {enemy_stopwatch}", normal_font, "white", 800, 450, GAME_SCREEN)
            pygame.display.update()
            pygame.time.wait(200)

            enemy_respawn(pc_car)
            Settings.enemy_start_time = pygame.time.get_ticks()

        else:
            DrawUI.check_audio(racing_game.sounds.sounds.countdown_sound.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.starting_sound.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
            DrawUI.check_audio(racing_game.sounds.sounds.lose.play)

            DrawUI.draw_text(f"WRONG WAY!", normal_font, "white", 830, 450, GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1000)

            LoopFunctions.check_new_game()
            reset_map()

    @staticmethod
    def enemy_end_game(reset_map):
        if Settings.enemy_lap == Settings.max_laps:

            if Settings.enemy_lap > Settings.car_lap:
                DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
                DrawUI.check_audio(racing_game.sounds.sounds.win.play)
                GAME_SCREEN.blit(button_win_lose, (770, 560))
                DrawUI.draw_text(f"SECOND PLAYER WON THE RACE!", normal_font, "gold", 710, 600, GAME_SCREEN)

                pygame.display.update()
                pygame.time.wait(1000)

            if Settings.enemy_lap < Settings.car_lap:
                DrawUI.check_audio(racing_game.sounds.sounds.car_engine.stop)
                DrawUI.check_audio(racing_game.sounds.sounds.lose.play)

                GAME_SCREEN.blit(button_win_lose, (770, 560))
                DrawUI.draw_text(f"FIRST PLAYER WON THE RACE!", normal_font, "red", 800, 600, GAME_SCREEN)

                pygame.display.update()
                pygame.time.wait(1000)

            Settings.enemy_time_list.sort()
            Settings.car_time_list.sort()
            DrawUI.enemy_time_table(Settings.enemy_time_list[0], Settings.enemy_time_list[Settings.max_laps - 1],
                                    Settings.enemy_match_time)

            pygame.display.update()
            pygame.time.wait(5000)

            LoopFunctions.check_new_game()
            reset_map()
