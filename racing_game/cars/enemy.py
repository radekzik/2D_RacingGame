from racing_game.cars.car import Car
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import LoadingImages


class EnemyPlayer(Car):
    x_position = 700
    y_position = 900
    car_image = LoadingImages.FORMULA[5]["CAR"]
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def car_current_speed(self):
        position_x = 100
        position_y = 940

        if self.car_speed < 0:
            DrawUI.draw_text(f"0", LoadingImages.NORMAL_FONT, "red", position_x, position_y, LoadingImages.GAME_SCREEN)
        if self.car_speed == 0:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "white", position_x, position_y, LoadingImages.GAME_SCREEN)
        if 0 < self.car_speed <= 1:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "green", position_x, position_y, LoadingImages.GAME_SCREEN)
        if 1 < self.car_speed <= 2:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "green", position_x, position_y, LoadingImages.GAME_SCREEN)
        if 2 < self.car_speed <= 3:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "orange", position_x, position_y, LoadingImages.GAME_SCREEN)
        if 3 < self.car_speed <= 20:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "red", position_x, position_y, LoadingImages.GAME_SCREEN)

    def car_current_nitro(self):
        DrawUI.draw_text(f"{round(self.car_nitro)}", LoadingImages.NORMAL_FONT, "cyan", 200, 740, LoadingImages.GAME_SCREEN)

    def respawn_first_map(self):
        self.x = 700
        self.y = 950
        self.car_angle = 270

    def respawn_second_map(self):
        self.x = 700
        self.y = 900
        self.car_angle = 270

    def respawn_third_map(self):
        self.x = 670
        self.y = 880
        self.car_angle = 270

    def respawn_fourth_map(self):
        self.x = 700
        self.y = 900
        self.car_angle = 270

    def respawn_fifth_map(self):
        self.x = 680
        self.y = 950
        self.car_angle = 270
