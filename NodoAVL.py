import Estudiante
from typing import Optional

# Nodo del árbol AVL
class NodoAVL:
    def __init__(self, estudiante: Estudiante):
        """
        Este método será responsable de crear un nuevo nodo del árbol AVL

        Args:
            estudiante (Estudiante): La instancia del estudiante que se almacenará en este nodo
        """
        self.estudiante = estudiante
        self.izquierda: Optional[NodoAVL] = None
        self.derecha: Optional[NodoAVL] = None
        self.altura: int = 1

    def __str__(self):
        """
        Este método proporcionará una representación en cadena del nodo

        Returns:
            str: Una cadena que contiene el código del estudiante entre corchetes
        """
        return f"[{self.estudiante.codigo}]"