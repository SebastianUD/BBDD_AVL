from abc import ABC, abstractmethod
from typing import Dict, Any

class EntidadBase(ABC):
    @abstractmethod
    def get_codigo(self) -> int:
        """Retorna el código único de la entidad (clave primaria)"""
        pass
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convierte la entidad a diccionario"""
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Crea una instancia desde un diccionario"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Representación en string de la entidad"""
        pass
