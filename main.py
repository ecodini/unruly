import random

import niveles
import unruly
import ui

def main():
    nivel = random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)

    print("Juego UNRULY")
    print("Hecho por Enzo Codini para ALG 1, FIUBA 2023")

    while True:
        ui.print_grid(grilla)
        ui.enter_coordinates()

main()