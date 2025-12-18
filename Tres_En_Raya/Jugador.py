import pygame 

class Jugador:
    def __init__(self,posicion,simbolo):
    
        self.posicion = posicion
        self.simbolo = simbolo
        self.puntos = 0


    def dibujo_Figuras(self,pantalla):
         
         if self.simbolo == "O" :    
            pygame.draw.circle(pantalla, "blue", self.posicion,40)
        
         if self.simbolo == "X":
            pygame.draw.line(pantalla, "red", (self.posicion.x, self.posicion.y),
                 (self.posicion.x + self.posicion.width, self.posicion.y + self.posicion.height), 5)
            pygame.draw.line(pantalla, "red", (self.posicion.x + self.posicion.width, self.posicion.y),
                 (self.posicion.x, self.posicion.y + self.posicion.height), 5)

    