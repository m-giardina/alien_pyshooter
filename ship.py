import pygame

class Ship():

    def __init__(self, screen):
        """Initialize ship and starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        # bmp from https://cdn.dribbble.com/users/35310/screenshots/2494273/icon-a-day-falcon-heavy_1x.png
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom cent of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        self.center = float(self.rect.centerx)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on screen."""
        self.center = self.screen_rect.centerx
