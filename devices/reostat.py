import pygame
from PIL import Image
#from Tools.demo.spreadsheet import center



class Reostat1(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.im = Image.open(filename)
        self.I= None
        self.U = None
        self.R=10
        self.con1=[]
        self.con2=[]
    def izmR(self,oot):
        if oot==4:
            self.R=self.R + 0.5
        elif oot==5:
            self.R=self.R - 0.5
