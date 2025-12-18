#IMPORTACIONES
import pygame
from Manzana import Manzana
from Serpiente import Serpiente
import random

#CREACION DE LA VENTANA Y DE LOS OBJETOS QUE QUIERO UTILIZAR
pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("SNAKE")
running = True
serpiente = Serpiente(tamaño=10)
manzana = Manzana(tamaño=10, ancho_ventana=700, alto_ventana=500)
clock = pygame.time.Clock()
tiempo = 0
velocidad_movimiento = 0.2
font = pygame.font.Font(None,32)

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
            
            puntos_ganados = random.randint(1,5)
            serpiente.puntos += puntos_ganados
            
 #METODO DEL MARCADOR DE PUNTOS           
def Marcador_Puntos():
    suavizado = True
    color = ("white")
    
    texto_vidas = font.render(f"Puntos : {serpiente.puntos} ", suavizado, color)
    
    texto = texto_vidas.get_rect()
    texto.centerx = 800 // 2
    texto.centery = 20
    
    ventana.blit(texto_vidas, texto)
    
#METODO DE CUANDO TOCA PARED SACA EL TEXTO GAME OVER 
def Perdido():
    suave = True  
    color = ("white")
    texto_perdido = font.render("GAME OVER" , suave,color)
    
    frase = texto_perdido.get_rect()
    frase.centerx = ventana.get_width() // 2
    frase.centery = ventana.get_height() // 2
    
    ventana.blit(texto_perdido,frase)
    

#BUCLE DE INICIO Y LLAMADAS DE METODOS DE LAS DIFERENTES CLASES 

serpiente.corregir_velocidad()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    if serpiente.viva:
        serpiente.Movimiento_Serpiente()
        serpiente.Colision_Pared()
        
       
        
    else:
        Perdido()
        pygame.display.update()
        pygame.time.delay(1000)
        manzana.moverRandom()
        serpiente.Reinicio()
        continue
           
        
    tiempo = 0.2
    ventana.fill("blue")
    serpiente.Dibujo(ventana)
    manzana.Manzana_Dibujo(ventana)
    Comer_Manzana(serpiente,manzana)
    Marcador_Puntos()
    
    
    dt = clock.tick(60)/1000
    tiempo += dt
    pygame.display.flip()
   
pygame.quit()

