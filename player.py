from car import Car
from resolution import draw_text
from load_image import blue_formula, blue_lambo, width, height, game_screen, small_font


class Player(Car):
    x_position = 700
    y_position = 950
    car_image = blue_formula
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def first_map_car(self):
        self.car_image = blue_formula

    def second_map_car(self):
        self.car_image = blue_lambo

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
        draw_text(f"X - ( {round(self.x)} )", small_font, "white", 1740, 940, game_screen)
        draw_text(f"MOVEMENT - ( {round(self.movement_speed)} )", small_font, "white", 1590, 970, game_screen)
        draw_text(f"SPEED - ( {round(self.car_speed)} )", small_font, "white", 1620, 940, game_screen)

