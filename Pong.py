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
radio_pelota = 10 


pala1 = pygame.Rect(jugador1.x,jugador1.y, ANCHO_PALA,ALTO_PALA)
pala2 = pygame.Rect(jugador2.x,jugador2.y, ANCHO_PALA, ALTO_PALA)
rect_pelota = pygame.Rect(int(pelota.x - radio_pelota),int(pelota.y - radio_pelota),radio_pelota * 2,radio_pelota * 2)

#REINICIO
def Reinicio():
    global pelota, vel_pelota
    if pelota.x - radio_pelota <= 0 or pelota.x + radio_pelota >= 800:
        
        pelota.x = 400
        pelota.y = 300


#BUCLE DE FUNCIONAMIENTO
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
                    
    screen.fill("black")
    
    #DIBUJO DE LOS OBJETOS
    j1 =  pygame.draw.rect(screen,"blue",pala1)
    j2 = pygame.draw.rect(screen,"yellow", pala2)
    p = pygame.draw.circle(screen,("green"),(int(pelota.x), int(pelota.y)),10)
   
   #MOVIMIMENTO DE LA PELOTA 
        #REBOTE HORIZONTAL
    if pelota.x + radio_pelota == 800 or pelota.x - radio_pelota == 0:
        vel_pelota.x *= -1

        #REBOTE VERTICAL 
    if pelota.y + radio_pelota >= 600 or pelota.y - radio_pelota <= 0:
        vel_pelota.y *= -1

    pelota += vel_pelota
    
    #COLISION DE LA PELOTA CON LAS PAREDES Y JUGADORES
    if p.colliderect(j1) or p.colliderect(j2):
        vel_pelota.x *= -1
        pelota += vel_pelota
        
    if p.colliderect(j1) or p.colliderect(j2):
        vel_pelota.y *= 1
        pelota += vel_pelota
    
    Reinicio()   

    #MOVIMIENTOS JUGADOR 2
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and pala2.top > 0:
        jugador2.y -= velocidad
    if teclas[pygame.K_DOWN] and pala2.bottom < 600:
            jugador2.y += velocidad
     
    #MOVIMIENTOS JUGADOR 1
    if teclas[pygame.K_w] and pala1.top>0:
        jugador1.y -= velocidad
    if teclas[pygame.K_s] and pala1.bottom<600:
        jugador1.y += velocidad
         
     
    #ACTUALIZACION DE JUGADORES       
    pala1.center = jugador1
    pala2.center = jugador2
    
    


    
    pygame.display.flip()
    
    time.sleep(1/60)
    
pygame.quit()
    
