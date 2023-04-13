from typing import Tuple
import unruly


def print_grid(grilla: unruly.Grilla) -> None:
    col_num, row_num = unruly.dimensiones(grilla)
    
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
            return list(map(int, coordinates))
