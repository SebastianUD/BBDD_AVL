from abc import ABC, abstractmethod
from typing import Optional
from Estudiante import Estudiante

class IArbolAVL(ABC):
    @abstractmethod
    def insertar(self):
        pass
    
    @abstractmethod
    def eliminar(self):
        pass
    
    @abstractmethod
    def buscar(self):
        pass
    
    @abstractmethod
    def mostrar_inorden(self):
        pass
    
    @abstractmethod
    def mostrar_estructura(self):
        pass