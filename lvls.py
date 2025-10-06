import pygame
from PIL import Image


class lvl_choose(pygame.sprite.Sprite):
    def __init__(self, x, y, filename,nom):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.im = Image.open(filename)
        self.nom=nom


class lvl_act(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, nom, objectsss):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.im = Image.open(filename)
        self.nom = nom
        self.objectsss=objectsss