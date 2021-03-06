import pygame

class Ship():

    def __init__(self, screen):
        # Initialize the ship and sets its starting position
        self.screen = screen

        # Load the image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start every new ship at the desired location
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # Draw the ship
        self.screen.blit(self.image, self.rect)