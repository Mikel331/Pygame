import pygame


#CLASE SERPIENTE
class Serpiente:
   
   
   #VARIABLES DE LA CLASE SERPIENTE
    def __init__ (self,tamaño):
       self.tamaño = tamaño
       self.color = ("green")
       self.cuerpo = [pygame.Rect(100, 100,tamaño,tamaño), pygame.Rect(100, 100,tamaño,tamaño)]
       self.direccion = pygame.Vector2(tamaño,0)
       self.crecer = False
       self.velocidad = 3
       
       
     #DIBUJO Y MOVIMIENTO POR SI SOLO
    def Dibujo(self,pantalla):
        for segmento in self.cuerpo:
            serpiente =  pygame.Rect(segmento.x,segmento.y,self.tamaño,self.tamaño)  
            pygame.draw.rect(pantalla,self.color,serpiente)
            
            

    #MOVIMIENTO DE LA SERPIENTE DE ARRIBA, ABAJO , IZQUIERDA ,DERECHA
    def Movimiento_Serpiente(self):
        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and self.cuerpo[0].y > 0:
            self.direccion= pygame.Vector2(0,- self.velocidad) 
        
        elif teclas[pygame.K_DOWN] and self.cuerpo[0].y < 600:
            self.direccion = pygame.Vector2(0,self.velocidad)
            
        elif teclas[pygame.K_LEFT] and self.cuerpo[0].x > 0:
           self.direccion = pygame.Vector2(- self.velocidad, 0)
            
        elif teclas[pygame.K_RIGHT] and self.cuerpo[0].x < 800:
           self.direccion = pygame.Vector2(self.velocidad,0)
           
           
        self.cuerpo[0].x += self.direccion.x
        self.cuerpo[0].y += self.direccion.y
        
        
        for i in range (len(self.cuerpo)-1,0,-1):
            self.cuerpo[i] = self.cuerpo[i-1].copy()
            
    
   
            

        