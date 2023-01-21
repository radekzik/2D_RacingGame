from racing_game.cars.car import Car
from racing_game.cars.pc import random_car

from racing_game.ui.load_image import red_formula, normal_font, GAME_SCREEN
from racing_game.ui.resolution import draw_text


class EnemyPlayer(Car):
    x_position = 700
    y_position = 900
    car_image = random_car()
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def respawn_first_map(self):
        self.x = 800
        self.y = 900
        self.car_angle = 270

    def car_current_speed(self):
        position_x = 100
        position_y = 940

        if self.car_speed < 0:
            draw_text(f"0", normal_font, "red", position_x, position_y, GAME_SCREEN)
        if self.car_speed == 0:
            draw_text(f"{round(self.car_speed)}", normal_font, "white", position_x, position_y, GAME_SCREEN)
        if 0 < self.car_speed <= 1:
            draw_text(f"{round(self.car_speed)}", normal_font, "green", position_x, position_y, GAME_SCREEN)
        if 1 < self.car_speed <= 2:
            draw_text(f"{round(self.car_speed)}", normal_font, "green", position_x, position_y, GAME_SCREEN)
        if 2 < self.car_speed <= 3:
            draw_text(f"{round(self.car_speed)}", normal_font, "orange", position_x, position_y, GAME_SCREEN)
        if 3 < self.car_speed <= 20:
            draw_text(f"{round(self.car_speed)}", normal_font, "red", position_x, position_y, GAME_SCREEN)

    def car_current_nitro(self):
        draw_text(f"{round(self.car_nitro)}", normal_font, "cyan", 200, 740, GAME_SCREEN)
