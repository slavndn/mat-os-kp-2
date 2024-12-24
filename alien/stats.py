import pygame


class GameStats:
    """Отслеживание статистики для игры 'Инопланетное Вторжение'."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats() 
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit  # Количество оставшихся жизней (кораблей)
        self.score = 0  # Текущий счет
        self.level = 1  # Текущий уровень игры

        # Флаг активации щита и его таймер
        self.shield_active = False
        self.shield_timer = 0  # Время начала действия щита

        # Начальные параметры скорости
        self.ship_speed_factor = self.ai_settings.ship_speed_factor
        self.bullet_speed_factor = self.ai_settings.bullet_speed_factor
        self.alien_speed_factor = self.ai_settings.alien_speed_factor
        self.alien_points = self.ai_settings.alien_points

    def activate_shield(self):
        self.shield_active = True
        self.shield_timer = pygame.time.get_ticks()  # Текущее время в миллисекундах

    def deactivate_shield(self):
        self.shield_active = False
        self.shield_timer = 0  # Сброс времени

    def is_shield_expired(self):
        if self.shield_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.shield_timer > self.ai_settings.shield_duration:
                self.deactivate_shield()
                return True
        return False

    def to_dict(self):
        return {
            "ships_left": self.ships_left,
            "score": self.score,
            "level": self.level,
            "high_score": self.high_score,
            "ship_speed_factor": self.ship_speed_factor,  # Сохраняем скорость корабля
            "bullet_speed_factor": self.bullet_speed_factor,
            "alien_speed_factor": self.alien_speed_factor,
            "alien_points": self.alien_points
        }

    def from_dict(self, data):
        self.ships_left = data["ships_left"]
        self.score = data["score"]
        self.level = data["level"]
        self.high_score = data["high_score"]
        self.ship_speed_factor = data["ship_speed_factor"]  # Восстанавливаем скорость корабля
        self.bullet_speed_factor = data["bullet_speed_factor"]
        self.alien_speed_factor = data["alien_speed_factor"]
        self.alien_points = data["alien_points"]  # Восстанавливаем прирост очков

    def update_from_settings(self):
        self.ship_speed_factor = self.ai_settings.ship_speed_factor
        self.bullet_speed_factor = self.ai_settings.bullet_speed_factor
        self.alien_speed_factor = self.ai_settings.alien_speed_factor
        self.alien_points = self.ai_settings.alien_points
