class Gamestats():
    """Track stats for game"""
    def __init__(self, ai_settings):
        """Initialize stats."""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start game in active stateself.
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
