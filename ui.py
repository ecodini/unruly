from typing import Tuple
from unruly import dimensiones, Grilla


def print_grid(grilla: Grilla) -> None:
    col_num, row_num = dimensiones(grilla)
    
    print('# | ', end='')

    for col in range(0, col_num):
        print(str(col) + ' ', end='')

    print('|')

    for row in range(0, row_num):
        print(str(row) + ' | ', end='')
        for col in range(0, col_num):
            if grilla[row][col] == ' ':
                print('_ ', end='')
            else:
                print(grilla[row][col] + ' ', end='')
        
        print()


def enter_coordinates() -> Tuple[int, int, int]:
    print("Comando: (columna fila valor)")
    print("Salir: q")

    while True:
        entry = input('Comando: ')
        
        if(entry == 'q'):
            quit()

        coordinates = entry.split(' ')

        if len(coordinates) == 3 and all(c.isdigit() for c in coordinates):
            return (int(coordinates[0]), int(coordinates[1]), coordinates[2])
