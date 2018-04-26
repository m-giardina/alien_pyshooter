class Settings():
    """A class to store all settings for game."""

    def __init__(self):
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (255, 255, 255)

        # Ship Settings
        self.ship_speed_factor = 1.5
