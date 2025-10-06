import pygame
from PIL import Image


class Key(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.im = Image.open(filename)
        self.imw=filename
        self.I = 0
        self.R=0
        self.U=0
        self.con1=[]
        self.con2=[]
        self.zaamk=False
    def zammmk(self, ot):
        if ot:
            self.zaamk=True
        else:
            self.zaamk=False