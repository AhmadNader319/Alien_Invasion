import pygame

class CheckEvent:
    def __init__(self):  # No need to pass event here
        pass

    def check_event(self, event):
        check_event = 0  # Initialize inside the method
        if event.type == pygame.QUIT:
            check_event = 0  # or just return directly
            return check_event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                check_event = 1
            elif event.key == pygame.K_LEFT:
                check_event = 2
            elif event.key == pygame.K_UP:
                check_event = 3
            elif event.key == pygame.K_DOWN:
                check_event = 4
            elif event.key == pygame.K_d:
                check_event = 5
            elif event.key == pygame.K_a:
                check_event = 6
            elif event.key == pygame.K_w:
                check_event = 7
            elif event.key == pygame.K_s:
                check_event = 8


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_s:
                check_event = 9
        return check_event

