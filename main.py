import random

import niveles
import unruly
import ui
import consts

def main():
    nivel = random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)

    col_num, row_num = unruly.dimensiones(grilla)

    print("Juego UNRULY")
    print("Hecho por Enzo Codini para ALG 1, FIUBA 2023")

    while True:
        ui.print_grid(grilla)
        col, row, val = ui.enter_coordinates()

        if col < col_num and row < row_num and val in (consts.ONE, consts.ZERO):
            if val == consts.ONE:
                unruly.cambiar_a_uno(grilla, col, row)
            else:
                unruly.cambiar_a_cero(grilla, col, row)
        
        if unruly.grilla_terminada(grilla):
            print('Juego terminado! Habeis ganado, enhorabuena!!!!!')

main()