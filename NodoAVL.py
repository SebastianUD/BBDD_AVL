from typing import Optional
from EntidadBase import EntidadBase

# Nodo del árbol AVL
class NodoAVL:
    def __init__(self, entidad: EntidadBase):
        """
        Este método será responsable de crear un nuevo nodo del árbol AVL

        Args:
            entidad (EntidadBase): La instancia de la entidad que se almacenará en este nodo
        """
        self.entidad = entidad
        self.izquierda: Optional[NodoAVL] = None
        self.derecha: Optional[NodoAVL] = None
        self.altura = 1

    def __str__(self):
        """
        Este método proporcionará una representación en cadena del nodo

        Returns:
            str: Una cadena que contiene el código de la entidad entre corchetes
        """
        return f"[{self.entidad.get_codigo()}]"