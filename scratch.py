import pygame
from game_settings import Settings
from tank import Tank
import game_function as gf

def run_game():
    pygame.init()   #initilizaing pygame
    ai_settings=Settings()  #initializating settings
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Shooting Game')
    tank=Tank(screen) #make a tank

    while True:
        gf.check_events(tank)
        tank.update()
        gf.update_screen(ai_settings,screen,tank)

run_game()