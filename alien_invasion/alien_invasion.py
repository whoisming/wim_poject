import sys
import pygame
from ship import Ship
from setting import Setting
import game_functions as gf

def run_game():
    pygame.init()
    # screen = pygame.display.set_mode((800,180))
    # pygame.display.set_caption("Alien_Invasion")
    # bg_color = (230,230,230)
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")
    ship = Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)
    # while True:
    #     for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()
       
run_game()