from abc import ABC, abstractmethod
from typing import Dict, Any

class Entidades(ABC):
    """Interfaz base para todas las entidades del sistema"""
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convierte la entidad a diccionario para serialización"""
        pass
    
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Entidades':
        """Crea una entidad desde un diccionario"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Proporcionar una representación en cadena de la entidad"""
        pass