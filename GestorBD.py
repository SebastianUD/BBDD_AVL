import os
import json
from typing import Optional, List
from ArbolAVL import ArbolAVL
from Estudiante import Estudiante
from NodoAVL import NodoAVL
from IGestorBD import IGestorBD

class GestorBD(IGestorBD):
    def __init__(self, archivo_json="estudiantes.json"):
        """
        Este método será responsable de inicializar el gestor de base de datos

        Args:
            archivo_json (str): El nombre del archivo JSON donde se almacenan los datos
        """
        self.directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.archivo_json = os.path.join(self.directorio_actual, archivo_json)
        self.arbol = ArbolAVL()
        self.cargar_datos()

    def cargar_datos(self):
        """
        Este método será responsable de cargar los datos desde el archivo JSON al árbol AVL
        """
        try:
            with open(self.archivo_json, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if datos:
                    print(f"[INFO] Cargando {len(datos)} estudiantes desde el archivo...")
                    for d in datos:
                        estudiante = Estudiante.from_dict(d)
                        self.arbol.raiz = self.arbol.insertar(self.arbol.raiz, estudiante, mostrar_mensajes=False)
        except FileNotFoundError:
            print(f"[INFO] Archivo {self.archivo_json} no encontrado. Creando nuevo archivo vacío...")
            with open(self.archivo_json, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4, ensure_ascii=False)
            print(f"[INFO] Archivo creado exitosamente.")

    def guardar_en_json(self):
        """
        Este método será responsable de guardar todos los datos del árbol AVL en el archivo JSON
        """
        datos = []
        self._recolectar_datos(self.arbol.raiz, datos)
        with open(self.archivo_json, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"[INFO] Datos guardados en {self.archivo_json}")

    def _recolectar_datos(self, nodo: Optional[NodoAVL], datos: List[dict]):
        """
        Este método será responsable de recolectar datos del árbol AVL de forma recursiva

        Args:
            nodo (Optional[NodoAVL]): El nodo actual del cual recolectar datos
            datos (List[dict]): La lista donde se almacenan los datos recolectados
        """
        if nodo:
            self._recolectar_datos(nodo.izquierda, datos)
            datos.append(nodo.estudiante.to_dict())
            self._recolectar_datos(nodo.derecha, datos)

    def agregar_estudiante(self, estudiante: Estudiante):
        """
        Este método será responsable de agregar un estudiante al árbol y guardarlo en JSON

        Args:
            estudiante (Estudiante): El estudiante que se va a agregar
        """
        self.arbol.agregar_estudiante(estudiante)
        self.guardar_en_json()

    def eliminar_estudiante(self, codigo: int) -> bool:
        """
        Este método será responsable de eliminar un estudiante del árbol y actualizar el JSON

        Args:
            codigo (int): El código del estudiante que se va a eliminar

        Returns:
            bool: True si el estudiante fue eliminado exitosamente, False si no existía
        """
        if self.arbol.buscar_por_codigo(codigo):
            self.arbol.eliminar_estudiante(codigo)
            self.guardar_en_json()
            return True
        return False

    def actualizar_estudiante(self, codigo: int, nuevo_estudiante: Estudiante):
        """
        Este método será responsable de actualizar un estudiante en el árbol y guardarlo en JSON

        Args:
            codigo (int): El código del estudiante que se va a actualizar
            nuevo_estudiante (Estudiante): Los nuevos datos del estudiante
        """
        self.arbol.actualizar_estudiante(codigo, nuevo_estudiante)
        self.guardar_en_json()

    def buscar_por_codigo(self, codigo: int) -> Optional[Estudiante]:
        """
        Este método será responsable de buscar un estudiante por su código

        Args:
            codigo (int): El código del estudiante que se busca

        Returns:
            Optional[Estudiante]: El estudiante encontrado o None si no existe
        """
        return self.arbol.buscar_por_codigo(codigo)

    def mostrar_inorden(self):
        """
        Este método será responsable de mostrar todos los estudiantes en orden por código
        """
        print("\n[LISTADO] Estudiantes en orden por código:")
        if self.arbol.raiz:
            self.arbol.inorden(self.arbol.raiz)
        else:
            print("No hay estudiantes registrados.")

    def mostrar_arbol_visual(self):
        """
        Este método será responsable de mostrar la estructura visual del árbol AVL
        """
        print("\n[ESTRUCTURA] Árbol AVL:")
        if self.arbol.raiz:
            self.arbol.mostrar_arbol_binarytree()
        else:
            print("Árbol vacío")