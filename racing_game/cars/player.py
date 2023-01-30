from racing_game.cars.car import Car
from racing_game.ui import loading_images
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import GAME_SCREEN


class Player(Car):
    x_position = 700
    y_position = 950

    # x_position = GAME_SCREEN.get_width() / 2
    # y_position = GAME_SCREEN.get_height() / 2

    car_image = loading_images.FORMULA[1]["CAR"]
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    @staticmethod
    def player_cars(index):

        car_list = [loading_images.FORMULA[1]["CAR"], loading_images.FORMULA[3]["CAR"],
                    loading_images.FORMULA[4]["CAR"], loading_images.FORMULA[5]["CAR"],
                    loading_images.SPORTS_CAR_I[1]["CAR"], loading_images.SPORTS_CAR_I[2]["CAR"],
                    loading_images.SPORTS_CAR_I[3]["CAR"], loading_images.SPORTS_CAR_I[4]["CAR"],
                    loading_images.SPORTS_CAR_II[1]["CAR"], loading_images.SPORTS_CAR_II[2]["CAR"],
                    loading_images.SPORTS_CAR_II[3]["CAR"], loading_images.SPORTS_CAR_II[4]["CAR"],
                    loading_images.CABRIO[1]["CAR"], loading_images.CABRIO[2]["CAR"],
                    loading_images.CABRIO[3]["CAR"], loading_images.CABRIO[4]["CAR"]]

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
        if self.x >= loading_images.WIDTH or self.x <= 0:
            self.respawn_first_map()
        if self.y >= loading_images.HEIGHT or self.y <= 0:
            self.respawn_first_map()

    def car_position(self):
        DrawUI.draw_text(f"Y - ( {round(self.y)} )", loading_images.small_font, "white", 120, 1030, GAME_SCREEN)
        DrawUI.draw_text(f"X - ( {round(self.x)} )", loading_images.small_font, "cyan", 30, 1030, GAME_SCREEN)

    def car_current_speed(self):
        # draw_text(f"MOVEMENT - ( {round(self.movement_speed)} )", small_font, "cyan", 1660, 1020, game_screen)
        if self.car_speed < 0:
            DrawUI.draw_text(f"0", loading_images.normal_font, "red", 1800, 940, GAME_SCREEN)
        if self.car_speed == 0:
            DrawUI.draw_text(f"{round(self.car_speed)}", loading_images.normal_font, "white", 1800, 940, GAME_SCREEN)
        if 0 < self.car_speed <= 1:
            DrawUI.draw_text(f"{round(self.car_speed)}", loading_images.normal_font, "green", 1800, 940, GAME_SCREEN)
        if 1 < self.car_speed <= 2:
            DrawUI.draw_text(f"{round(self.car_speed)}", loading_images.normal_font, "green", 1800, 940, GAME_SCREEN)
        if 2 < self.car_speed <= 3:
            DrawUI.draw_text(f"{round(self.car_speed)}", loading_images.normal_font, "orange", 1800, 940, GAME_SCREEN)
        if 3 < self.car_speed <= 20:
            DrawUI.draw_text(f"{round(self.car_speed)}", loading_images.normal_font, "red", 1800, 940, GAME_SCREEN)

    def car_current_nitro(self):
        DrawUI.draw_text(f"{round(self.car_nitro)}", loading_images.normal_font, "cyan", 1800, 740, GAME_SCREEN)
