import pygame
from pygame.sprite import Group

from button import Button
from game_stats import Gamestats
from scoreboard import Scoreboard
from settings import Settings


from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (255, 255, 255)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    explosions = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    play_button = Button(ai_settings, screen, "PLAY")

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
            bullets, explosions)

        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, explosions)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, explosions, play_button)

run_game()
