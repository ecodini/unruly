from random import choice
from niveles import NIVELES
from unruly import crear_grilla, dimensiones, cambiar_a_uno, cambiar_a_cero, grilla_terminada
from ui import print_grid, enter_coordinates
import consts

def main():
    nivel = choice(NIVELES)
    grilla = crear_grilla(nivel)

    col_num, row_num = dimensiones(grilla)

    print("Juego UNRULY")
    print("Hecho por Enzo Codini para ALG 1, FIUBA 2023")

    while True:
        print_grid(grilla)
        col, row, val = enter_coordinates()

        if col < col_num and row < row_num and val in (consts.ONE, consts.ZERO):
            if val == consts.ONE:
                cambiar_a_uno(grilla, col, row)
            else:
                cambiar_a_cero(grilla, col, row)
        
        if grilla_terminada(grilla):
            print('Juego terminado! Habeis ganado, enhorabuena!!!!!')
            quit()

main()