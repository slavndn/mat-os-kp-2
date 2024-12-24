class Settings:
    """Класс для хранения настроек игры 'Инопланетное Вторжение'."""

    def __init__(self):

        # Параметры экрана
        self.screen_width = 1200  # Ширина экрана
        self.screen_height = 800  # Высота экрана
        self.bg_color = (22, 59, 108)  # Цвет фона экрана (темно-синий)

        # Параметры корабля
        self.ship_limit = 3  # Максимальное количество кораблей у игрока

        # Параметры скорости пришельцев и очков
        self.speedup_scale = 1.2  # Коэффициент увеличения скорости пришельцев после каждого уровня
        self.score_scale = 1.1  # Коэффициент увеличения очков за убитых пришельцев

        # Параметры пуль
        self.bullet_width = 3  # Ширина пули
        self.bullet_height = 15  # Высота пули
        self.bullet_color = (100, 50, 200)  # Цвет пули
        self.bullet_allowed = 5  # Максимальное количество пуль на экране

        # Параметры бонусов
        self.bonus_chance = 0.1  # Вероятность появления бонуса
        self.bonus_speed = 1.1  # Скорость падения бонусов
        self.shield_duration = 5000  # Длительность щита (в миллисекундах)

        # Инициализация динамических параметров игры
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Инициализация динамических параметров, изменяющихся в ходе игры.

        Эти параметры могут изменяться во время игры в зависимости от уровня и других факторов:
        - Скорости корабля, пуль и пришельцев.
        - Параметры пришельцев: скорость движения, количество очков за уничтожение.
        - Направление движения флота пришельцев.
        """
        self.ship_speed_factor = 1.01  # Начальная скорость корабля
        self.bullet_speed_factor = 1  # Начальная скорость пуль y
        self.alien_speed_factor = 1  # Начальная скорость пришельцев
        self.fleet_drop_speed = 10  # Скорость падения флота пришельцев
        self.alien_points = 10  # Очки за одного пришельца
        self.fleet_direction = 1  # Направление движения флота (1 - вправо, -1 - влево)

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale  # Увеличение скорости корабля
        self.bullet_speed_factor *= self.speedup_scale  # Увеличение скорости пуль
        self.alien_speed_factor *= self.speedup_scale  # Увеличение скорости пришельцев
        self.alien_points = int(self.alien_points * self.score_scale)  # Увеличение очков за пришельцев
