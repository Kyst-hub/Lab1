import pygame
from PIL import Image
#from Tools.demo.spreadsheet import center


class Volt_Metr(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.im = Image.open(filename)
        self.I= None
        self.U = 0
        self.R=0
        self.con1=[]
        self.con2=[]
        self.ot=False
    def inf(self,sc):
        if self.ot:
            f=pygame.font.Font(None,24)
            sc_text= f.render('U='+str(self.U),1,(0,0,0))
            posi= sc_text.get_rect(center=(self.im.size[0]/2+self.rect[0],self.rect[1]-10))
            sc.blit(sc_text,posi)