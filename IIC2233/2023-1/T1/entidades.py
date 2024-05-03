from abc import ABC, abstractmethod
import random
import parametros

class Item(ABC):
    def __init__(self, nombre: str, tipo: str, descripcion: str):
        self._nombre = nombre
        self._tipo = tipo
        self._descripcion = descripcion

class Consumible(Item):
    def __init__(self, nombre: str, tipo: str, descripcion: str,  energia: int, fuerza: int, suerte: int, felicidad: int):
        super().__init__(nombre, 'consumible', descripcion)
        self.energia = energia
        self.fuerza = fuerza
        self.suerte = suerte
        self.felicidad = felicidad

class Tesoro(Item):
    def __init__(self, nombre: str, tipo: str, descripcion: str, calidad: int, cambio: str):
        super().__init__(nombre, 'tesoro', descripcion)
        self.calidad = calidad
        self.cambio = cambio

class Arena(ABC):
    def __init__(self, nombre: str, tipo: str, rareza: int, humedad: int, dureza: int, estatica: int, items: list):
        self.nombre = nombre
        self.tipo = tipo
        self._rareza = rareza
        self._humedad = humedad
        self._dureza = dureza
        self._estatica = estatica
        self._items = items
        self._dificultad = round((self.rareza + self.humedad + self.dureza + self.estatica) / 40, 2)

    @property
    def rareza(self):
        return self._rareza
    
    @rareza.setter
    def rareza(self, r):
        if r > 10:
            self._rareza = 10
        elif r < 1:
            self._rareza = 1
        else:
            self._rareza = r
    
    @property
    def humedad(self):
        return self._humedad
    
    @humedad.setter
    def humedad(self, h):
        if h > 10: 
            self._humedad = 10
        elif h < 1:
            self._humedad = 1
        else:
            self._humedad = h

    @property
    def dureza(self):
        return self._dureza

    @property
    def estatica(self):
        return self._estatica


class ArenaNormal(Arena):
    def __init__(self, nombre, tipo, rareza, humedad, dureza, estatica, items):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)
        self._dificultad = self._dificultad * parametros.POND_ARENA_NORMAL
        

class ArenaMojada(Arena):
    def __init__(self, nombre: str, tipo: str, rareza: int, humedad: int, dureza: int, estatica: int, items: list):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)

    # SIEMPRE Excavador va a encontrar item
        # este item tiene misma prob de ser tesoro o consumible (0.5)

class ArenaRocosa(Arena):
    def __init__(self, nombre: str, tipo: str, rareza: int, humedad: int, dureza: int, estatica: int, items: list):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)
        self._dificultad = round((self._rareza + self._humedad + 2 * self._dureza + self._estatica) / 50, 2)

class ArenaMagnetica(ArenaMojada, ArenaRocosa):
    def __init__(self, nombre: str, tipo: str, rareza: int, humedad: int, dureza: int, estatica: int, items: list):
        super().__init__(nombre, tipo, rareza, humedad, dureza, estatica, items)

    # Cada vez que se Simular día Torneo => humedad y dureza aleatorios entre 1 y 10 (podría ser con randint, dado el setter)

class Excavador(ABC):
    def __init__(self, nombre: str, edad: int, energia: int, fuerza: int, suerte: int, felicidad: int):
        self.nombre = nombre
        self._edad = edad
        self._energia = energia
        self._fuerza = fuerza
        self._suerte = suerte
        self._felicidad = felicidad
        self._descansando = False
        self.dias_por_descansar = 0

    @property
    def energia(self):
        return self._energia # recordar que este es el getter. Simplemente podría llamar a Excavador.energia y obtener el valor de tal atributo

    @energia.setter
    def energia(self, e: int):
        if e > 100:
            self._energia = 100
        elif e < 0:
            self._energia = 0
            self.descansar()
        else:
            self._energia = e

    @property
    def fuerza(self):
        return self._fuerza
    
    @fuerza.setter
    def fuerza(self, f: int):
        if f > 10:
            self._fuerza = 10
        elif f < 0: 
            self._fuerza = 0
        else:
            self._fuerza = f

    @property
    def suerte(self):
        return self._fuerza
    
    @suerte.setter
    def suerte(self, s: int):
        if s > 10:
            self._suerte = 10
        elif s < 0:
            self._suerte = 0
        else:
            self._suerte = s

    @property
    def felicidad(self):
        return self._felicidad
    
    @felicidad.setter
    def felicidad(self, f: int):
        if f > 10:
            self._felicidad = 10
        elif f < 0:
            self._felicidad = 0
        else: 
            self._felicidad = f

    @property
    def descansando(self):
        return self.dias_por_descansar > 0

    @abstractmethod
    def cavar(self, dificultad_arena: float) -> float:
        metros_cavados = round(((30 / self._edad) + ((self._felicidad + 2 * self._fuerza) / 10)) * (1 / (10 * dificultad_arena)), 2)
        self.gastar_energia()
        return metros_cavados

    @abstractmethod
    def descansar(self) -> None:
        dias_descanso = int(self._edad / 20)
        self.descansando = True
        self.dias_por_descansar = dias_descanso

    @abstractmethod
    def encontrar_item(self):
        prob_item = parametros.PROB_ENCONTRAR_ITEM * (self._suerte / 10)
        if random.random() <= prob_item:
            tesoro_o_consumible = random.choices(['tesoro', 'consumible'], [parametros.PROB_ENCONTRAR_TESORO, parametros.PROB_ENCONTRAR_CONSUMIBLE], k=1)
            return tesoro_o_consumible[0]
        return ''
    
    @abstractmethod
    def gastar_energia(self):
        energia_gastada = int((19 / self._fuerza) + (self._edad / 6))
        self._energia -= energia_gastada

    @abstractmethod
    def consumir(self, consumible: Consumible):
        self.energia += consumible.energia
        self.fuerza += consumible.fuerza
        self.suerte += consumible.suerte
        self.felicidad += consumible.felicidad

class ExcavadorDocencio(Excavador):
    def __init__(self, nombre: str, edad: int, energia: int, fuerza: int, suerte: int, felicidad: int):
        super().__init__(nombre, edad, energia, fuerza, suerte, felicidad)
        
    def cavar(self, dificultad_arena: float) -> float:
        super().cavar(dificultad_arena)
        self._felicidad += parametros.FELICIDAD_ADICIONAL_DOCENCIO
        self._fuerza += parametros.FUERZA_ADICIONAL_DOCENCIO

    def descansar(self) -> None:
        super().descansar()

    def encontrar_item(self):
        super().encontrar_item()

    def gastar_energia(self):
        super().gastar_energia()
        self._energia -= parametros.ENERGIA_PERDIDA_DOCENCIO
    
    def consumir(self, consumible: list):
        super().consumir(consumible)

class ExcavadorTareo(Excavador):
    def __init__(self, nombre: str, edad: int, energia: int, fuerza: int, suerte: int, felicidad: int):
        super().__init__(nombre, edad, energia, fuerza, suerte, felicidad)

    def cavar(self, dificultad_arena: float) -> float:
        super().cavar(dificultad_arena)
    
    def descansar(self) -> None:
        super().descansar()

    def encontrar_item(self):
        super().encontrar_item()

    def gastar_energia(self):
        super().gastar_energia()

    def consumir(self, consumible: Consumible):
        super().consumir(consumible)
        self._energia += parametros.ENERGIA_ADICIONAL_TAREO
        self._suerte += parametros.SUERTE_ADICIONAL_TAREO
        self._edad += parametros.EDAD_ADICIONAL_TAREO
        self._felicidad -= parametros.FELICIDAD_PERDIDA_TAREO

class ExcavadorHibrido(ExcavadorDocencio, ExcavadorTareo):
    def __init__(self, nombre: str, edad: int, energia: int, fuerza: int, suerte: int, felicidad: int):
        super().__init__(nombre, edad, energia, fuerza, suerte, felicidad)

    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, e):
        if e > 100:
            self._energia = 100
        elif e < 20:
            self._energia = 20
        else:
            self._energia = e
    
    def cavar(self, dificultad_arena: float) -> float:
        ExcavadorDocencio.cavar(self, dificultad_arena)
    
    def descansar(self) -> None:
        super().descansar()

    def encontrar_item(self):
        super().encontrar_item()

    def gastar_energia(self):
        ExcavadorDocencio.gastar_energia(self)

    def consumir(self, consumible: Consumible):
        ExcavadorTareo.consumir(self, consumible)

# Logs
class Logs():
    # se inicializa instancia sin parámetros ni argumentos
    def __init__(self):
        self.metros_cavados = []
        self.items_encontrados = []
        self.eventos_ocurridos = []
        self.lvls = ['mts', 'items_dia', 'eventos_dia']

    def add(self, lvl: str, msg: tuple) -> None:
        options = [self.metros_cavados, self.items_encontrados, self.eventos_ocurridos]
        try:
            index = self.lvls.index(lvl)
            options[index].append(msg)
        except ValueError:
            self.items_encontrados.append(msg)

    def mts_dia(self, msg: tuple):
        pass

    def items_dia(self, msg: tuple) -> None:
        # en el print, debe incluir que alguien no encontró nada. Por tanto, debe venir un bool o reconocer un 'Nada' en la tupla.
        pass

    def eventos_dia(self, msg) -> None:
        pass

class Torneo:
    def __init__(self, arena: Arena, equipo: list, eventos: list):
        self.arena = arena
        self.equipo = equipo
        self.eventos = eventos
        self.mochila = []
        self._mts_cavados = 0
        self.meta = parametros.METROS_META
        self.dias_transcurridos = 0
        self.dias_totales = parametros.DIAS_TOTALES_TORNEO
        self.torneo_finalizado = False

    # properties
    
    def simular_dia(self, logs: Logs):
        for excavador in self.equipo:
            if not excavador.descansando:
                mts = excavador.cavar()
                self._mts_cavados += mts
                logs.add('mts', (excavador.nombre, mts))
                encuentra = excavador.encontrar_item()
                # implementar correctamente en Logs el caso en que el excavador no encuentre nada
                logs.add('items_dia', (excavador.nombre, encuentra))
                # falta simulacion de eventos

    def mostrar_estado(self):
        sep = '-------------------------------------------------------------'
        estado = f'''
                                *** Estado Torneo ***                
        {sep}
        Día actual: {self.dias_transcurridos}
        Tipo de arena: {self.arena}
        Metros excavados: {int(self._mts_cavados)} / {self.meta}
        {sep}
        '''
        print(estado)

    def ver_mochila(self):
        pass

    def usar_consumible(self):
        pass

    def abrir_tesoro(self):
        pass

    def iniciar_evento(self):
        # lluvia
        # terremoto
        # derrumbe
        pass
        


        

    
