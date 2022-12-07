from game.cars.car import Car

from game.ui.load_image import red_formula


class EnemyPlayer(Car):
    x_position = 700
    y_position = 920
    car_image = red_formula
    car_angle = 270

    car_width = car_image.get_width()
    car_height = car_image.get_height()

    def first_map_car(self):
        self.car_image = red_formula

    def respawn(self):
        self.x = 700
        self.y = 920
        self.car_angle = 270
