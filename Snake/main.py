#IMPORTACIONES
import pygame
import time
from Manzana import Manzana
from Serpiente import Serpiente

#CREACION DE LA VENTANA Y DE LOS OBJETOS QUE QUIERO UTILIZAR
pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("SNAKE")
running = True
serpiente = Serpiente(tamaño=20)
manzana = Manzana(tamaño=10, ancho_ventana=700, alto_ventana=500)
clock = pygame.time.Clock()
tiempo = 0
velocidad_movimiento = 0.2

#METODO COMER MANZANA

def Comer_Manzana(serpiente, manzana):
    cabeza_serpiente = serpiente.cuerpo[0]  

    manzana_rect = pygame.Rect(
        manzana.posicion.x,
        manzana.posicion.y,
        manzana.tamaño,
        manzana.tamaño
    )

    if cabeza_serpiente.colliderect(manzana_rect):
            serpiente.crecer = True
            manzana.moverRandom()


#BUCLE DE INICIO Y LLAMADAS DE METODOS DE LAS DIFERENTES CLASES 
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if tiempo >= velocidad_movimiento:
        serpiente.Movimiento_Serpiente()
        tiempo=0.2 
    
    ventana.fill("blue")
    serpiente.Dibujo(ventana)
    manzana.Manzana_Dibujo(ventana)
    Comer_Manzana(serpiente,manzana)
   

    
    dt = clock.tick(60)/1000
    tiempo += dt
    pygame.display.flip()
   
pygame.quit()

