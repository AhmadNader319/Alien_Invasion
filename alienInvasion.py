import pygame
from ship import Ship
from rocket import Rocket
from settings import Settings
from bullet import Bullet

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
            self._update_objects()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)
    
    def _handle_keydown(self, event):
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        
        self.ship_events += self._handle_movement(event, self.ship, {
            pygame.K_RIGHT: 'moving_right', pygame.K_LEFT: 'moving_left',
            pygame.K_UP: 'moving_up', pygame.K_DOWN: 'moving_down'
        })
        
        self.rocket_events += self._handle_movement(event, self.rocket, {
            pygame.K_d: 'moving_right', pygame.K_a: 'moving_left',
            pygame.K_w: 'moving_up', pygame.K_s: 'moving_down'
        })
    
    def _handle_keyup(self, event):
        self._handle_movement(event, self.ship, {
            pygame.K_RIGHT: 'moving_right', pygame.K_LEFT: 'moving_left',
            pygame.K_UP: 'moving_up', pygame.K_DOWN: 'moving_down'
        }, False)
        
        self._handle_movement(event, self.rocket, {
            pygame.K_d: 'moving_right', pygame.K_a: 'moving_left',
            pygame.K_w: 'moving_up', pygame.K_s: 'moving_down'
        }, False)
    
    def _handle_movement(self, event, obj, key_map, is_keydown=True):
        event_count = 0
        if event.key in key_map:
            setattr(obj, key_map[event.key], is_keydown)
            event_count = 1 if is_keydown else 0
        return event_count
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))
    
    def _update_objects(self):
        self.ship.update()
        self.rocket.update()
        self._update_bullets()
    
    def _update_bullets(self):
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        
        self.ship.blitme()
        self.rocket.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self._display_event_counts()
        pygame.display.flip()
    
    def _display_event_counts(self):
        ship_text = self.font.render(f"Ship Events: {self.ship_events}", True, (0, 0, 0))
        rocket_text = self.font.render(f"Rocket Events: {self.rocket_events}", True, (0, 0, 0))
        
        self.screen.blit(ship_text, (10, 10))
        self.screen.blit(rocket_text, (10, 50))

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
