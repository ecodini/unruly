import random

import niveles
import unruly

def main():
    nivel = niveles.NIVELES[0] # random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)

    print("UNRULY TEST")
    print(unruly.grilla_terminada(grilla))

main()