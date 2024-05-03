import parametros

def start_menu(data: list, money: int, round_n: int) -> None:
    print_start_menu(money, round_n)
    option = input('Indique su opción: ')
    options = {
        '0': exit_program,
        '1': store,
        '2': army,
        '3': fight,
        '4': error_message
    }
    n = input_handler(options, option)
    try:
        options[n](money)
    except KeyError:
        error_message(data, money, round_n)

def data_manager(data: list) -> None:
    pass

def error_message(data: list, money: int, round_n: int):
    print('Opción seleccionada no es válida. Redirigiendo al menú de inicio...')
    start_menu(data, money, round_n)

def input_handler(options: dict, option: str) -> int:
    try:
        keys = list(options.keys())
        index = keys.index(option)
        return str(index)
    except ValueError:
        print('El valor ingresado no es válido. Redirigiendo al menú de inicio...')
        return -1

def print_start_menu(money: int, round_n: int) -> None:
    print('\n*** Menú de inicio ***\n')
    print(f'Dinero disponible: {money}')
    print(f'Ronda actual: {round_n}\n')
    menu_options = {
        '1': 'Tienda',
        '2': 'Ejército',
        '3': 'Combatir',
        '0': 'Salir del programa'
    }
    for key, value in menu_options.items():
        if key == '0':
            print(f'\n[{key}] {value}\n')
        else:
            print(f'[{key}] {value}')

def store(money: int) -> None:
    print_store(money)

def print_store(money: int) -> None:
    print('\n*** Tienda ***\n')
    print(f'Dinero disponible: {money}\n')
    options = {
        '1': ('Gato Mago', 10),
        '2': ('Gato Guerrero', 10),
        '3': ('Gato Caballero', 10),
        '4': ('Ítem Armadura', 5),
        '5': ('Ítem Pergamino', 5),
        '6': ('Ítem Lanza', 5),
        '7': ('Curar Ejército', 7),
        '0': 'Volver al Menú de Inicio'
    }
    producto, precio = 'Producto', 'Precio'
    print(f'    {producto:16}{precio:6}')
    for key, value in options.items():
        if key != '0':
            print(f'[{key}] {value[0]:<16}{value[1]:^6}')
        else:
            print(f'\n[{key}] {value}\n')

def army():
    pass

def fight():
    pass

def exit_program(money: int):
    print('Saliendo del programa... \n')