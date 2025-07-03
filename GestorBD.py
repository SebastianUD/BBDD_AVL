import os
import json
from typing import Optional, List
from ArbolAVL import ArbolAVL
from Estudiante import Estudiante
from NodoAVL import NodoAVL

# Gestor de base de datos que usa JSON y el árbol AVL
class GestorBD:
    def __init__(self, archivo_json="estudiantes.json"):
        self.directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.archivo_json = os.path.join(self.directorio_actual, archivo_json)
        self.arbol = ArbolAVL()
        self.cargar_datos()

    def cargar_datos(self):
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
        datos = []
        self._recolectar_datos(self.arbol.raiz, datos)
        with open(self.archivo_json, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"[INFO] Datos guardados en {self.archivo_json}")

    def _recolectar_datos(self, nodo: Optional[NodoAVL], datos: List[dict]):
        if nodo:
            self._recolectar_datos(nodo.izquierda, datos)
            datos.append(nodo.estudiante.to_dict())
            self._recolectar_datos(nodo.derecha, datos)

    def agregar_estudiante(self, estudiante: Estudiante):
        self.arbol.agregar_estudiante(estudiante)
        self.guardar_en_json()

    def eliminar_estudiante(self, codigo: int) -> bool:
        if self.arbol.buscar_por_codigo(codigo):
            self.arbol.eliminar_estudiante(codigo)
            self.guardar_en_json()
            return True
        return False

    def actualizar_estudiante(self, codigo: int, nuevo_estudiante: Estudiante):
        self.arbol.actualizar_estudiante(codigo, nuevo_estudiante)
        self.guardar_en_json()

    def buscar_por_codigo(self, codigo: int) -> Optional[Estudiante]:
        return self.arbol.buscar_por_codigo(codigo)

    def mostrar_inorden(self):
        print("\n[LISTADO] Estudiantes en orden por código:")
        if self.arbol.raiz:
            self.arbol.inorden(self.arbol.raiz)
        else:
            print("No hay estudiantes registrados.")

    def mostrar_arbol_visual(self):
        print("\n[ESTRUCTURA] Árbol AVL:")
        if self.arbol.raiz:
            self.arbol.mostrar_arbol_binarytree()
        else:
            print("Árbol vacío")