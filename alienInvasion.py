import pygame
from ship import Ship
from rocket import Rocket
from settings import Settings
from bullet import Bullet
from pygame.sprite import Sprite

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.ship_events = 0
        self.rocket_events = 0
        self.font = pygame.font.Font(None, 36)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.rocket.update()
            self._update_bullets() 

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        self.ship_events += self._handle_ship_keydown(event)
        self.rocket_events += self._handle_rocket_keydown(event)

    def _check_keyup_events(self, event):
        self.ship_events += self._handle_ship_keyup(event)
        self.rocket_events += self._handle_rocket_keyup(event)

    def _handle_ship_keydown(self, event):
        event_count = 0
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            event_count = 1
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            event_count = 1
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
            event_count = 1
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            event_count = 1
        return event_count

    def _handle_ship_keyup(self, event):
        event_count = 0
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        return event_count

    def _handle_rocket_keydown(self, event):
        event_count = 0
        if event.key == pygame.K_d:
            self.rocket.moving_right = True
            event_count = 1
        elif event.key == pygame.K_a:
            self.rocket.moving_left = True
            event_count = 1
        elif event.key == pygame.K_w:
            self.rocket.moving_up = True
            event_count = 1
        elif event.key == pygame.K_s:
            self.rocket.moving_down = True
            event_count = 1
        return event_count



    def _handle_rocket_keyup(self, event):
        event_count = 0
        if event.key == pygame.K_d:
            self.rocket.moving_right = False
        elif event.key == pygame.K_a:
            self.rocket.moving_left = False
        elif event.key == pygame.K_w:
            self.rocket.moving_up = False
        elif event.key == pygame.K_s:
            self.rocket.moving_down = False
        return event_count
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.ship.update()
        self.ship.blitme()

        self.rocket.update()
        self.rocket.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        ship_text = self.font.render(f"Ship Events: {self.ship_events}", True, (0, 0, 0))
        rocket_text = self.font.render(f"Rocket Events: {self.rocket_events}", True, (0, 0, 0))

        self.screen.blit(ship_text, (10, 10))
        self.screen.blit(rocket_text, (10, 50))

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()