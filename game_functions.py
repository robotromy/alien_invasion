import sys
import pygame

def check_events(ship):
    # Response to mouse and key imputs"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    # Update images in the screen
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

