import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Класс для управления пулями, выпущенными кораблём.

    Этот класс управляет пулями, которые корабль выпустил для уничтожения пришельцев.
    Пули движутся вверх по экрану и исчезают, когда выходят за пределы экрана.
    """

    def __init__(self, ai_settings, screen, ship, dx):
        super().__init__()  # Вызов конструктора родительского класса Sprite
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  # Центр пули по горизонтали совпадает с центром корабля
        self.rect.top = ship.rect.top  # Пуля появляется на верхней границе корабля

        # Позиция пули хранится в вещественном формате для более точных вычислений
        self.y = float(self.rect.y)
        self.dx = dx

        self.color = ai_settings.bullet_color  # Цвет пули
        self.speed_factor = ai_settings.bullet_speed_factor  # Скорость движения пули

    def update(self):

        # self.y -= self.speed_factor  # Обновление позиции пули в вещественном формате (движется вверх)
        # self.x += self.dx  # Обновление позиции пули в вещественном формате (движется вверх)
        self.rect.y -= self.speed_factor  # Обновление прямоугольника для отображения пули на экране
        self.rect.x += self.dx  # Обновление прямоугольника для отображения пули на экране

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)  # Рисует прямоугольник пули