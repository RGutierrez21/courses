import os
import functions
import tablero

def main_menu() -> None:
    print('\n*** Menú de Inicio ***\n')
    file = input('Indique el nombre del archivo que desea abrir: ')
    handle_file(file)
    
def handle_file(file: str) -> None:
    txt = os.path.join('Archivos', f'{file}.txt')
    if not os.path.isfile(txt):
        print('Nombre del archivo incorrecto. Saliendo del programa...')
    else:
        board = functions.cargar_tablero(file)
        print('\nArchivo cargado exitosamente.')
        print('\nRedirigiendo al menú de acciones...')
        action_menu(board)

def action_menu(board: list) -> None:
    print('\n*** Menú de Acciones ***\n')
    # se ocupará un dict con las opciones, key será el dígito que podrá ocupar el usuario
    # el value será la función que será llamada cuando selecciones el key, junto con un string para print en consola
    options = {
        1: (tablero.imprimir_tablero_con_utf8, 'Mostrar tablero'),
        2: (functions.validar_tablero, 'Validar bombas y tortugas'),
        3: (print_solution, 'Revisar solución'),
        4: (functions.solucionar_tablero, 'Solucionar tablero'),
        5: (exit_game, 'Salir del programa')
    }
    for key, value in options.items():
        print(f'[{key}] {value[1]}')
    opt = input('\nIndique su opción (1, 2, 3, 4 ó 5): ')
    handle_action_menu(options, opt, board)

def handle_action_menu(options: dict, chosen: str, board: list) -> None:
    try:
        options[int(chosen)][0](board)
    except (KeyError, ValueError):
        print('\nError. Revise los datos ingresados')
        action_menu(board)

def print_solution(board: list) -> None:
    n = len(board)
    file = f'{n}x{n}_sol.txt'
    sol = solution_handle(file)
    tablero.imprimir_tablero_con_utf8(sol)
    action_menu(board)        

def solution_handle(file_name: str) -> list:
    board = []
    txt = os.path.join('Archivos', f'{file_name}')
    with open(txt, 'rt') as f:
        raw = f.readlines()
        rows = raw[0].strip().split(',')
        fila = []
        for ele in rows[1:]:
            if len(fila) < int(rows[0]):
                fila.append(ele)
            if len(fila) == int(rows[0]):
                board.append(fila)
                fila = []
    return board            

def exit_game(board: list) -> None:
    print('Saliendo del programa...\n')


