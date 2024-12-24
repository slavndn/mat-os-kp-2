import pygame
from pygame.sprite import Sprite
import functions as gf


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_settings, screen):
        super().__init__()  # Инициализация родительского класса Sprite
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load(gf.resource_path('resources/alienship.bmp'))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца для более точных вычислений
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x