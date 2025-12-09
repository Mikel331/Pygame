import pygame 
import time
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((800,600))
running = True


#CREACION DE LOS OBJETOS
jugador1 = pygame.Vector2(20,screen.get_height()/2)
jugador2 = pygame.Vector2(780,screen.get_height()/2)
pelota = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
vel_pelota = pygame.Vector2(4, 4)


#CREACION DE LA ALTURA Y ANCHURA DE LOS DOS JUGADORES Y SU VELOCIDAD
ANCHO_PALA= 20
ALTO_PALA = 120
velocidad = 6

#POSICIONAMIENTO DE LOS OBJETOS
pala1 = pygame.Rect(jugador1.x,jugador1.y, ANCHO_PALA,ALTO_PALA)
pala2 = pygame.Rect(jugador2.x,jugador2.y, ANCHO_PALA, ALTO_PALA)
pygame.draw.circle(screen,(255,255,255),(int(pelota.x), int(pelota.y)),10)

#BUCLE DE FUNCIONAMIENTO
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                    
    screen.fill("black")
    
    #DIBUJO DE LOS OBJETOS
    pygame.draw.rect(screen,"white",pala1)
    pygame.draw.rect(screen,"white", pala2)
    
    
    #MOVIMIENTOS JUGADOR 1
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and pala1.top > 0:
        jugador1.y -= velocidad
    if teclas[pygame.K_DOWN] and pala1.bottom < 600:
            jugador1.y += velocidad
     
    #MOVIMIENTOS JUGADOR 2      
    if pelota.y < jugador2.y and pala2.top > 0:
        jugador2 -=velocidad
    if pelota.y > jugador2.y and pala2.bottom < 600:
        jugador2 += velocidad
     
    #ACTUALIZACION DE JUGADORES       
    pala1.center = jugador1
    pala2.center = jugador2
    
   
    
    pygame.display.flip()
    
    time.sleep(1/60)
    
pygame.quit()
    
