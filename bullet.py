import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        """Create a bullet object at the ship's position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright  # Spawn from the ship's right side

        # Store the bullet's position as a float
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet rightward across the screen."""
        self.x += self.settings.bullet_speed  # Move bullet to the right
        self.rect.x = self.x  # Update rect position

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
