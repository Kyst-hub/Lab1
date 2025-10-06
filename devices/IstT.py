import pygame
from PIL import Image


class Istochnik_toka(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.im = Image.open(filename)
        self.U = 60
        self.con1=[]
        self.con2=[]