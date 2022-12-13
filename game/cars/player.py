from game.cars.car import Car
from game.ui.resolution import draw_text
from game.ui.load_image import blue_formula, blue_lambo, width, height, game_screen, small_font, green_formula, \
    yellow_formula, orange_formula, cyan_lambo, red_lambo, pink_lambo


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

    def respawn_first_map(self):
        self.x = 700
        self.y = 950
        self.car_angle = 270

    def respawn_second_map(self):
        self.x = 1000
        self.y = 850
        self.car_angle = 270

    def out_of_map(self):
        if self.x >= width or self.x <= 0:
            self.respawn_first_map()
        if self.y >= height or self.y <= 0:
            self.respawn_first_map()

    def car_info(self):

        draw_text(f"Y - ( {round(self.y)} )", small_font, "white", 1740, 970, game_screen)
        draw_text(f"X - ( {round(self.x)} )", small_font, "cyan", 1740, 940, game_screen)
        draw_text(f"MOVEMENT - ( {round(self.movement_speed)} )", small_font, "cyan", 1590, 970, game_screen)
        draw_text(f"SPEED - ( {round(self.car_speed)} )", small_font, "white", 1620, 940, game_screen)
