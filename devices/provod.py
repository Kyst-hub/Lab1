import pygame
from PIL import Image

class Node1(pygame.sprite.Sprite):
    def __init__(self,x,y,i,j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/circ.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.im = Image.open('images/circ.png')
        self.con=None
        #self.con2=None
        self.id = i
        self.id2=j
class Node2(pygame.sprite.Sprite):
    def __init__(self,x,y,i,j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/circ.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.im = Image.open('images/circ.png')
        #self.con1=None
        self.con=None
        self.id=i
        self.id2=j