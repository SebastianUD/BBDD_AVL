from abc import ABC, abstractmethod
from typing import Optional
from Estudiante import Estudiante


class IGestorBD(ABC):
    """Interfaz que define los métodos públicos del Gestor de Base de Datos"""
    
    def __init__(self):
        """
        Este método será responsable de declarar la interfaz para inicializar  el gestor de base de datos
        """
        pass

    def cargar_datos(self):
        """
        Este método será responsable de declarar la interfaz para cargar los datos desde el archivo JSON al árbol AVL
        """
        pass

    def guardar_en_json(self):
        """
        Este método será responsable de declarar la interfaz para guardar todos los datos del árbol AVL en el archivo JSON
        """
        pass

    def _recolectar_datos(self):
        """
        Este método será responsable de declarar la interfaz para recolectar datos del árbol AVL de forma recursiva
        """
        pass

    def agregar_estudiante(self):
        """
        Este método será responsable de declarar la interfaz para agregar un estudiante al árbol y guardarlo en JSON
        """
        pass

    def eliminar_estudiante(self):
        """
        Este método será responsable de declarar la interfaz para eliminar un estudiante del árbol y actualizar el JSON
        """
        pass

    def actualizar_estudiante(self):
        """
        Este método será responsable de declarar la interfaz para actualizar un estudiante en el árbol y guardarlo en JSON
        """
        pass

    def buscar_por_codigo(self):
        """
        Este método será responsable de buscar un estudiante por su código
        """
        pass

    def mostrar_inorden(self):
        """
        Este método será responsable de declarar la interfaz para mostrar todos los estudiantes en orden por código
        """
        pass

    def mostrar_arbol_visual(self):
        """
        Este método será responsable de declarar la interfaz para mostrar la estructura visual del árbol AVL
        """
        pass