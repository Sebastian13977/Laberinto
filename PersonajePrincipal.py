import pygame
from objectoJuego import ObjectoJuego as Objeto
class PersonajePrincipal(Objeto):
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)
        self.velocidad = 10

        
    def mover(self,aumentarX,aumentarY):
        self.rect.x+= aumentarX*self.velocidad
        self.rect.y+= aumentarY*self.velocidad
    