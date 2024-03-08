import pygame
class ObjectoJuego():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color

    def render(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)
        