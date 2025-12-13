import pygame
import random

#CLASE DE MANZANA
class Manzana:
    
    
    #VARIABLES DE MANZANA
    def __init__(self,tamaño ,ancho_ventana,alto_ventana):
        self.posicion = pygame.Vector2(200, 200)
        self.tamaño = tamaño
        self.ancho_ventana = ancho_ventana
        self.alto_ventana = alto_ventana
        self.color = ("Red")
        self.moverRandom()
        
        
    #DIBUJO DE LA MANZANA 
    def Manzana_Dibujo(self, pantalla):
        manzanas = pygame.Rect(self.posicion.x , self.posicion.y , self.tamaño , self.tamaño)
        pygame.draw.rect(pantalla,self.color,manzanas)
           
           
    #MOVIMIENTO ALEATORIO DE LA MANZANA
    def moverRandom(self):
        self.posicion = pygame.Vector2(     
        random.randint(0,(self.ancho_ventana - self.tamaño) // self.tamaño) * self.tamaño,
        random.randint(0,(self.alto_ventana - self.tamaño) // self.tamaño) * self.tamaño
        )

     
        
        
        
        
        