import pygame
class Tank():
    def __init__(self,screen):
        """initializing the tank and making the rectangle"""
        self.screen=screen
        self.image=pygame.image.load('images/tank.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        """making its start location"""
        self.rect.centery=self.screen_rect.centery
        self.rect.left=self.screen_rect.left

        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_up:
            self.rect.centery-=1
        if self.moving_down:
            self.rect.centery+=1

    def blitme(self):
        """Drawing the tank over bg"""
        self.screen.blit(self.image,self.rect)