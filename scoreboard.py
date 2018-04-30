import pygame.font

class Scoreboard():
    """A class to report scoring info."""
    def __init__(self, ai_settings, screen, stats):
        """Initialize score attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring info
        self.text_color = (30, 30 , 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the intial score image.
        self.prep_score()
        self.prep_level()

    def prep_level(self):
        """Render level into image."""
        self.level_image = self.font.render(str(self.stats.level), True,
            self.text_color, self.ai_settings.bg_color)

        # position the level below the scoreself.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """Render score image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)

        # display the score at top right screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score on screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
