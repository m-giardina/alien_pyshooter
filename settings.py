class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (255, 255, 255)

        # Ship settings.
        self.ship_speed_factor = 1.9
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings.
        self.alien_speed_factor = 1.3
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

        # Game speedup
        self.speedup_scale =  1.2

        # Scoring
        self.alien_points = 50
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize setting that change in gameplay."""
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 2.8
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
