import sys
import pygame

def check_events(tank):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                tank.moving_up=True
            elif event.key==pygame.K_DOWN:
                tank.moving_down=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                tank.moving_up=False
            elif event.key==pygame.K_DOWN:
                tank.moving_down=False



def update_screen(ai_settings,screen,tank):
    """updating the screen  everytime loop runs"""
    screen.fill(ai_settings.bg_color)
    tank.blitme()
    pygame.display.flip()