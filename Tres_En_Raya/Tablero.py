import pygame 

class Tablero:
    
    def __init__(self, ancho=800,alto=600,filas=3,columnas=3):
        self.ancho = ancho
        self.alto = alto
        self.filas = filas 
        self.columnas = columnas
        self.color = ("white")
        
        self.tam_celda_x = ancho / columnas
        self.tam_celda_y = alto / filas


    def dibujar(self,pantalla) :
         
        for i in range(1, self.columnas):
            x = round(i * self.tam_celda_x)
            pygame.draw.line(
                pantalla,
                self.color,
                (x, 0),
                (x, self.alto),
                5
            )

        for i in range(1, self.filas):
            y = round(i * self.tam_celda_y)
            pygame.draw.line(
                pantalla,
                self.color,
                (0, y),
                (self.ancho, y),
                5
            )
        
        