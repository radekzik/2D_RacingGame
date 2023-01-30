



class Button:
    def __init__(self, x_y, button_image, button_text, font, font_color, font_hover_color):
        self.x = x_y[0]
        self.y = x_y[1]
        self.font = font
        self.font_color = font_color
        self.font_hover_color = font_hover_color
        self.button_text = button_text
        self.button_image = button_image

        self.button_rect = self.button_image.get_rect(center=(self.x, self.y))

        self.text_render = self.font.render(self.button_text, True, self.font_color)
        self.text_rect = self.text_render.get_rect(center=(self.x, self.y))

    def on_click(self, mouse_coordinates):
        in_rect = True

        if self.button_rect.left <= mouse_coordinates[0] <= self.button_rect.right:
            if self.button_rect.top <= mouse_coordinates[1] <= self.button_rect.bottom:
                return in_rect

    def on_hover(self, mouse_coordinates):

        if self.button_rect.left <= mouse_coordinates[0] <= self.button_rect.right:
            if self.button_rect.top <= mouse_coordinates[1] <= self.button_rect.bottom:
                self.text_render = self.font.render(self.button_text, True, self.font_hover_color)

        else:
            self.text_render = self.font.render(self.button_text, True, self.font_color)

    def button_render(self, game_screen):
        game_screen.blit(self.button_image, self.button_rect)
        game_screen.blit(self.text_render, self.text_rect)

    @staticmethod
    def button_hover_render(button_name, mouse_coordinates, game_screen):
        button_name.on_hover(mouse_coordinates)
        button_name.button_render(game_screen)

    @staticmethod
    def buttons_render(game_screen, *name):
        name.button_render(game_screen)