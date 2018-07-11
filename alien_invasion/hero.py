import pygame

class Hero():
    def __init__(self,screen):
        """ 初始化英雄形象"""
        self.screen = screen
        self.image = pygame.image.load("/Users/zhiming/Documents/mygit/alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)