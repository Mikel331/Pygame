import pygame
from Tablero import Tablero
from Jugador import Jugador
pygame.init()
ventana = pygame.display.set_mode((800,600))
running= True

jugador1 = Jugador(pygame.Vector2(200,200),"O")
jugador2 = Jugador(pygame.Rect(300,200,80,80), "X")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    ventana.fill("black")
    jugador1.dibujo_Figuras(ventana)
    jugador2.dibujo_Figuras(ventana)
    
    
    
    pygame.display.flip()
    
    
pygame.quit()