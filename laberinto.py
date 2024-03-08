#CONTROL PRINCIPAL DEL CODIGO
import pygame
import sys
from PersonajePrincipal import PersonajePrincipal
pygame.init()

BLANCO = (255,255,255)
VERDE = (0,255,0)
AZUL = (0,0,255)
ROJO = (255,0,0)
NEGRO = (0,0,0)

PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600

screen = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
pygame.display.set_caption("Juego del Laberinto")

def control_juego():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#CREAR PERSONAJE
player = PersonajePrincipal(50,50,30,30,AZUL)
#JUEGO
            
while True:
    screen.fill(VERDE)

    control_juego()
    player.render(screen)

    pygame.display.flip()





