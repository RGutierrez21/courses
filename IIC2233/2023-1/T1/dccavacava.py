# en este archivo se simula todo lo pertinente a las clases previamente definidas
# en este archivo se debe implementar la navegacion entre los menu
import os
import menu
from entidades import ArenaNormal, ArenaMojada, ArenaRocosa, ArenaMagnetica 
from entidades import ExcavadorDocencio, ExcavadorTareo, ExcavadorHibrido
from entidades import Torneo, Tesoro, Consumible, Logs


def main() -> None:
    menu.print_start_menu()
    options = ['1', '2', 'X']
    redirect = [new_game, load_game, main_exit]
    opt = input('\nIndique su opción (1, 2 o X): ')
    handle_input('start', options, redirect, opt)

def handle_input(menu_name: str, options: list, redirect: list, opt: str):
    try:
        index = options.index(opt.upper())
        redirect[index]()
    # list.index(value) arroja ValueError si value no está en list
    except ValueError:
        menu.print_error()
        if menu_name == 'start':
            main_exit()
        else:
            # implementar action_menu
            pass

def new_game() -> None:
    # aleatoriza
    pass

def file_handler(file: str) -> tuple:
    # debe tomar los path necesarios, buscar en los .csv o en el .txt
        # debe guardar una estructura de datos la informacion de cada archivo

    # se implementará sin la librería csv

    # TO-DO:
        # validar si existe el archivo
            # si existe, abrir el archivo
                # checkear si es .txt o .csv, probablemente la implementacion de la lectura sea distinta para ambos
                # leer contenido
                # almacenar contenido en estructura de datos
                # RETORNAR info
            # si no existe, retornar tupla vacia
    pass

def load_game():
    # busca el archivo dccavacava.txt e importa sus datos
    pass

def main_menu(torneo: Torneo):
    menu.print_main_menu(
        torneo.dias_transcurridos, torneo.dias_totales, torneo.arena.tipo
    )
    options = ['1', '2', '3', '4', '5', 'X']
    redirect = [
        day_simulation, tournament_status, see_items, save, back, main_exit
    ]
    opt = input('\nIndique su opción (1, 2, 3, 4, 5 o X)')
    handle_input('start', options, redirect, opt)

def day_simulation(torneo: Torneo):
    # torneo.simular_dia
    # Logs, tienen que funcionar
    pass

def tournament_status(torneo: Torneo):
    pass

def see_items(torneo: Torneo):
    pass

def save(torneo: Torneo):
    pass

def back():
    pass

def main_exit() -> None:
    menu.print_exit()