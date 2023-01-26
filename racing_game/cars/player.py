from racing_game.cars.car import Car
from racing_game.ui import loading_images
from racing_game.ui.resolution import draw_text
from racing_game.ui.loading_images import blue_formula, WIDTH, HEIGHT, GAME_SCREEN, small_font, normal_font


class Player(Car):
    x_position = 700
    y_position = 950

    # x_position = GAME_SCREEN.get_width() / 2
    # y_position = GAME_SCREEN.get_height() / 2

    car_image = blue_formula
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def player_cars(self, index):

        car_list = [loading_images.blue_formula, loading_images.orange_formula,
                    loading_images.yellow_formula, loading_images.green_formula,
                    loading_images.blue_lambo, loading_images.cyan_lambo,
                    loading_images.red_lambo, loading_images.pink_lambo,
                    loading_images.dark_purple_spoiler_car, loading_images.light_blue_spoiler_car,
                    loading_images.orange_spoiler_car, loading_images.pink_spoiler_car,
                    loading_images.blue_cabrio, loading_images.light_blue_cabrio,
                    loading_images.red_cabrio, loading_images.yellow_cabrio]

        # for x in range(12):
        # x += 1
        # if random_number == x:
        # settings.enemy_car_type = x
        # car_image = car_list[x - 1]

        return car_list[index]

    def respawn_first_map(self):
        self.x = 700
        self.y = 950
        self.car_angle = 270

    def respawn_second_map(self):
        self.x = 700
        self.y = 900
        self.car_angle = 270

    def respawn_third_map(self):
        self.x = 600
        self.y = 950
        self.car_angle = 270

    def respawn_fourth_map(self):
        self.x = 700
        self.y = 900
        self.car_angle = 270

    def respawn_fifth_map(self):
        self.x = 680
        self.y = 950
        self.car_angle = 270

    def optimal_respawn(self):
        self.x = self.x + 100
        self.y = self.y
        self.car_angle = 270

    def out_of_map(self):
        if self.x >= WIDTH or self.x <= 0:
            self.respawn_first_map()
        if self.y >= HEIGHT or self.y <= 0:
            self.respawn_first_map()

    def car_position(self):
        draw_text(f"Y - ( {round(self.y)} )", small_font, "white", 120, 1030, GAME_SCREEN)
        draw_text(f"X - ( {round(self.x)} )", small_font, "cyan", 30, 1030, GAME_SCREEN)

    def car_current_speed(self):
        # draw_text(f"MOVEMENT - ( {round(self.movement_speed)} )", small_font, "cyan", 1660, 1020, game_screen)
        if self.car_speed < 0:
            draw_text(f"0", normal_font, "red", 1800, 940, GAME_SCREEN)
        if self.car_speed == 0:
            draw_text(f"{round(self.car_speed)}", normal_font, "white", 1800, 940, GAME_SCREEN)
        if 0 < self.car_speed <= 1:
            draw_text(f"{round(self.car_speed)}", normal_font, "green", 1800, 940, GAME_SCREEN)
        if 1 < self.car_speed <= 2:
            draw_text(f"{round(self.car_speed)}", normal_font, "green", 1800, 940, GAME_SCREEN)
        if 2 < self.car_speed <= 3:
            draw_text(f"{round(self.car_speed)}", normal_font, "orange", 1800, 940, GAME_SCREEN)
        if 3 < self.car_speed <= 20:
            draw_text(f"{round(self.car_speed)}", normal_font, "red", 1800, 940, GAME_SCREEN)

    def car_current_nitro(self):
        draw_text(f"{round(self.car_nitro)}", normal_font, "cyan", 1800, 740, GAME_SCREEN)
