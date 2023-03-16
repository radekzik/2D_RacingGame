from racing_game.cars.car import Car
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import LoadingImages


class EnemyPlayer(Car):
    x_position = 700
    y_position = 900
    car_image = LoadingImages.FORMULA[5]["CAR"]
    car_angle = 270

    def car_current_speed(self):
        x = 100
        y = 940

        if self.car_speed < 0:
            DrawUI.draw_text(f"0", LoadingImages.NORMAL_FONT, "red", x, y, LoadingImages.GAME_SCREEN)
        if self.car_speed == 0:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "white", x, y,
                             LoadingImages.GAME_SCREEN)
        if 0 < self.car_speed <= 1:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "green", x, y,
                             LoadingImages.GAME_SCREEN)
        if 1 < self.car_speed <= 2:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "green", x, y,
                             LoadingImages.GAME_SCREEN)
        if 2 < self.car_speed <= 3:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "orange", x, y,
                             LoadingImages.GAME_SCREEN)
        if 3 < self.car_speed <= 20:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "red", x, y,
                             LoadingImages.GAME_SCREEN)

    def car_current_nitro(self):
        x = 200
        y = 740
        DrawUI.draw_text(f"{round(self.car_nitro)}", LoadingImages.NORMAL_FONT, "cyan", x, y,
                         LoadingImages.GAME_SCREEN)

    def respawn_first_map(self):
        self.respawn_map(700, 950, 270)

    def respawn_second_map(self):
        self.respawn_map(700, 900, 270)

    def respawn_third_map(self):
        self.respawn_map(670, 880, 270)

    def respawn_fourth_map(self):
        self.respawn_map(700, 900, 270)

    def respawn_fifth_map(self):
        self.respawn_map(680, 950, 270)
