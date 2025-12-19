import pygame
from Tablero import Tablero
from Jugador import Jugador

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tres en Raya")
running = True

tablero = Tablero()


cuadrado = [None] * 9
turno = "X"


ancho_celda = 800 // 3
alto_celda = 600 // 3


def elegir_cuadrado(pos, cuadrado, turno):
    x, y = pos
    columna = x // ancho_celda
    fila = y // alto_celda
    i = fila * 3 + columna

    if cuadrado[i] is None:
        cuadrado[i] = turno
        return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if elegir_cuadrado(event.pos, cuadrado, turno):
                turno = "O" if turno == "X" else "X"

 
    ventana.fill("black")
    tablero.dibujar(ventana)

    for idx, valor in enumerate(cuadrado):
        if valor is not None:
            fila = idx // 3
            columna = idx % 3
          
            pos_x = columna * ancho_celda + ancho_celda // 2
            pos_y = fila * alto_celda + alto_celda // 2

            if valor == "O":
                jugador = Jugador(pygame.Vector2(pos_x, pos_y), "O")
            else:
               
                jugador = Jugador(pygame.Rect(pos_x - 40, pos_y - 40, 80, 80), "X")

            jugador.dibujo_Figuras(ventana)

    pygame.display.flip()

pygame.quit()
