# cambiar manejo de menu en dccavacava
# manejo de input debe ir ahi, refactor a menu, solo deben hacer print de opciones
# deben poder navegar entre ellos, sin manejar ningun tipo de interaccion con las entidades


def print_start_menu():
    print('\n  *** Menú de Inicio ***  ')
    print('-' * len('  *** Menú de Inicio ***  '))
    options = {
        '1': 'Nueva partida',
        '2': 'Cargar partida',
        'X': 'Salir',
    }
    for key, value in options.items():
        print(f'[{key}] {value}')

def print_error():
    print('\nError. La opción indicada no es válida')

def print_exit():
    print('\nSaliendo del programa...\n')

def print_main_menu(actual_day: int, end_day: int, arena: str):
    arena_upper = arena[0].upper() + arena[1:]
    options = {
        '1': 'Simular día torneo',
        '2': 'Ver estado torneo',
        '3': 'Ver ítems',
        '4': 'Guardar partida',
        'X': 'Salir del programa'
    }
    print('\n   *** Menú Principal ***   ')
    print('-' * len('   *** Menú Principal ***   '))
    print(f'Día torneo DCCavaCava: {actual_day} / {end_day}')
    print(f'Tipo de arena: {arena_upper}\n')
    for key, value in options.items():
        print(f'[{key}] {value}')
