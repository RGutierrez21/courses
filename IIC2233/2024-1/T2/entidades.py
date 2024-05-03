from abc import ABC, abstractmethod
import parametros

class DataManager:
    def __init__(self, data: dict):
        pass

class Ejercito:
    def __init__(self):
        pass

    def combatir(self):
        pass

    def presentarse(self):
        pass

class Combatiente(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def curarse(self):
        pass

    @abstractmethod
    def evolucionar(self):
        pass

    @abstractmethod
    def presentarse(self):
        pass

class CombatienteGuerrero(Combatiente):
    def __init__(self):
        super().__init__()
    
    def atacar(self):
        pass

    def curarse(self):
        pass

    def evolucionar(self):
        pass

    def presentarse(self):
        pass

class CombatienteCaballero(Combatiente):
    def __init__(self):
        super().__init__()
    
    def atacar(self):
        pass

    def curarse(self):
        pass

    def evolucionar(self):
        pass

    def presentarse(self):
        pass

    