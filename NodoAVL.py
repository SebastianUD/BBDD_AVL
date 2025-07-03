import Estudiante
from typing import Optional

# Nodo del árbol AVL
class NodoAVL:
    def __init__(self, estudiante: Estudiante):
        self.estudiante = estudiante
        self.izquierda: Optional[NodoAVL] = None
        self.derecha: Optional[NodoAVL] = None
        self.altura: int = 1

    def __str__(self):
        return f"[{self.estudiante.codigo}]"