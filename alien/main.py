import pygame
from pygame.sprite import Group

from settings import Settings
from stats import GameStats
from button import Button
from ship import Ship
import functions as gf


def run_game():
    """
    Основная функция запуска игры.
    Инициализирует игровые объекты, обрабатывает события,
    обновляет состояние игры и рисует экран.
    """
    # Инициализация Pygame и настроек
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Инопланетное Вторжение")

    # Создание игровых объектов
    play_button = Button(ai_settings, screen, "Играть")  # Кнопка Play
    stats = GameStats(ai_settings)  # Хранение игровой статистики
    ship = Ship(ai_settings, screen)  # Корабль игрока

    # Создание групп спрайтов
    bullets = Group()  # Группа пуль
    aliens = Group()   # Группа пришельцев
    bonuses = Group()  # Группа бонусов

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Основной игровой цикл
    while True:
        # Обработка событий (ввод с клавиатуры, нажатия кнопок)
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # Обновление игровых объектов
            ship.update()  # Обновление состояния корабля
            gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets, bonuses)  # Обновление пуль
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)  # Обновление пришельцев
            gf.check_bonus_collisions(ai_settings, stats, ship, bonuses)  # Проверка столкновений бонусов
            bonuses.update()  # Обновление положения бонусов

            # Проверка истечения времени действия щита
            stats.is_shield_expired()

        # Обновление экрана
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, bonuses)


# Запуск игры
if __name__ == "__main__":
    run_game()
