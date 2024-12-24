import pygame.font


class Button:

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Размеры кнопки
        self.width, self.height = 200, 50
        # Цвет кнопки и текста
        self.button_color = (30, 100, 50)
        self.text_color = (255, 255, 255)
        # Шрифт для текста
        self.font = pygame.font.SysFont(None, 48)

        # Построение прямоугольника для кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Создание изображения для сообщения кнопки
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)  # Рисует кнопку с заданным цветом
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Рисует текст на кнопке
