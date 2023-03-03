from racing_game.cars.car import Car
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import LoadingImages


class Player(Car):
    x_position = 700
    y_position = 950

    car_image = LoadingImages.FORMULA[1]["CAR"]
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    @staticmethod
    def player_cars(index):

        car_list = [LoadingImages.FORMULA[1]["CAR"], LoadingImages.FORMULA[3]["CAR"],
                    LoadingImages.FORMULA[4]["CAR"], LoadingImages.FORMULA[5]["CAR"],
                    LoadingImages.SPORTS_CAR_I[1]["CAR"], LoadingImages.SPORTS_CAR_I[2]["CAR"],
                    LoadingImages.SPORTS_CAR_I[3]["CAR"], LoadingImages.SPORTS_CAR_I[4]["CAR"],
                    LoadingImages.SPORTS_CAR_II[1]["CAR"], LoadingImages.SPORTS_CAR_II[2]["CAR"],
                    LoadingImages.SPORTS_CAR_II[3]["CAR"], LoadingImages.SPORTS_CAR_II[4]["CAR"],
                    LoadingImages.CABRIO[1]["CAR"], LoadingImages.CABRIO[2]["CAR"],
                    LoadingImages.CABRIO[3]["CAR"], LoadingImages.CABRIO[4]["CAR"]]

        return car_list[index]

    def respawn_map(self, x, y, car_angle):
        self.x = x
        self.y = y
        self.car_angle = car_angle

    def respawn_first_map(self):
        self.respawn_map(700, 950, 270)

    def respawn_second_map(self):
        self.respawn_map(700, 900, 270)

    def respawn_third_map(self):
        self.respawn_map(600, 950, 270)

    def respawn_fourth_map(self):
        self.respawn_map(700, 900, 270)

    def respawn_fifth_map(self):
        self.respawn_map(680, 950, 270)

    def out_of_map(self):
        if self.x >= LoadingImages.WIDTH or self.x <= 0:
            self.respawn_first_map()
        if self.y >= LoadingImages.HEIGHT or self.y <= 0:
            self.respawn_first_map()

    def car_position(self):
        DrawUI.draw_text(f"Y - ( {round(self.y)} )", LoadingImages.SMALL_FONT, "white", 120, 1030,
                         LoadingImages.GAME_SCREEN)
        DrawUI.draw_text(f"X - ( {round(self.x)} )", LoadingImages.SMALL_FONT, "cyan", 30, 1030,
                         LoadingImages.GAME_SCREEN)

    def car_current_speed(self):
        if self.car_speed < 0:
            DrawUI.draw_text(f"0", LoadingImages.NORMAL_FONT, "red", 1800, 940, LoadingImages.GAME_SCREEN)
        if self.car_speed == 0:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "white", 1800, 940,
                             LoadingImages.GAME_SCREEN)
        if 0 < self.car_speed <= 1:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "green", 1800, 940,
                             LoadingImages.GAME_SCREEN)
        if 1 < self.car_speed <= 2:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "green", 1800, 940,
                             LoadingImages.GAME_SCREEN)
        if 2 < self.car_speed <= 3:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "orange", 1800, 940,
                             LoadingImages.GAME_SCREEN)
        if 3 < self.car_speed <= 20:
            DrawUI.draw_text(f"{round(self.car_speed)}", LoadingImages.NORMAL_FONT, "red", 1800, 940,
                             LoadingImages.GAME_SCREEN)

    def car_current_nitro(self):
        DrawUI.draw_text(f"{round(self.car_nitro)}", LoadingImages.NORMAL_FONT, "cyan", 1800, 740,
                         LoadingImages.GAME_SCREEN)
