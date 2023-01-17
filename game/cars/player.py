from game.cars.car import Car
from game.ui.resolution import draw_text
from game.ui.load_image import blue_formula, blue_lambo, width, height, game_screen, small_font, green_formula, \
    yellow_formula, orange_formula, cyan_lambo, red_lambo, pink_lambo, dark_purple_spoiler_car, light_blue_spoiler_car, \
    orange_spoiler_car, pink_spoiler_car, normal_font


class Player(Car):
    x_position = 700
    y_position = 950
    car_image = blue_formula
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    # formula
    def car_blue_formula(self):
        self.car_image = blue_formula

    def car_orange_formula(self):
        self.car_image = orange_formula

    def car_yellow_formula(self):
        self.car_image = yellow_formula

    def car_green_formula(self):
        self.car_image = green_formula

    # lambo
    def car_blue_lambo(self):
        self.car_image = blue_lambo

    def car_cyan_lambo(self):
        self.car_image = cyan_lambo

    def car_red_lambo(self):
        self.car_image = red_lambo

    def car_pink_lambo(self):
        self.car_image = pink_lambo

    def spoiler_car_dark_purple(self):
        self.car_image = dark_purple_spoiler_car

    def spoiler_car_light_blue(self):
        self.car_image = light_blue_spoiler_car

    def spoiler_car_orange(self):
        self.car_image = orange_spoiler_car

    def spoiler_car_pink(self):
        self.car_image = pink_spoiler_car

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
        self.x = 450
        self.y = 850
        self.car_angle = 270

    def out_of_map(self):
        if self.x >= width or self.x <= 0:
            self.respawn_first_map()
        if self.y >= height or self.y <= 0:
            self.respawn_first_map()

    def car_info(self):

        draw_text(f"Y - ( {round(self.y)} )", small_font, "white", 120, 1030, game_screen)
        draw_text(f"X - ( {round(self.x)} )", small_font, "cyan", 30, 1030, game_screen)
        # draw_text(f"MOVEMENT - ( {round(self.movement_speed)} )", small_font, "cyan", 1660, 1020, game_screen)
        draw_text(f"{round(self.car_speed)}", normal_font, "white", 1800, 940, game_screen)
