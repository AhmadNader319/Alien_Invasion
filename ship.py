import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('d:\\MyFolders\\Alien_Invasion\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)  # Store as float for precise movement
        self.y = float(self.rect.y)  # Store as float for precise movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0:  # Check for top boundary
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # Check for bottom boundary
            self.y += self.settings.ship_speed

        self.rect.x = self.x  # Important: Update rect.x after changing self.x
        self.rect.y = self.y  # Important: Update rect.y after changing self.y`

    def blitme(self):
        self.screen.blit(self.image, self.rect)