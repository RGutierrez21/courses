import sys
import os
import menu
import parametros

arg = sys.argv

def arg_handler() -> None:
    dif = ['facil', 'intermedio', 'dificil']
    if len(arg) == 2:
        try:
            index = dif.index(arg[1])
            data = get_data(dif[index])
            menu.start_menu(data, parametros.ORO_INICIAL, 1)
        except ValueError:
            print('\nArgumento inválido. Saliendo del programa...\n')
    else:
        print('Cantidad de argumentos inválida. Saliendo del programa...\n')

def get_data(file_name: str) -> list:
    file = f'{file_name}.txt'
    path = os.path.join('data', file)
    rounds = file_handler(path)
    return rounds

def file_handler(path: str) -> list:
    with open(path, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
        rounds = []
        for line in lines:
            round_n = line.strip().split(';')
            rounds.append(round_n)
        for round_n in rounds:
            for i in range(len(round_n)):
                split_opponent = round_n[i].split(',')
                round_n[i] = split_opponent
    return rounds

if __name__ == '__main__':
    arg_handler()