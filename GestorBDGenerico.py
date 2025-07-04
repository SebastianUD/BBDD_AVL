import os
import json
from typing import Optional, List, Type
from ArbolAVL import ArbolAVL
from EntidadBase import EntidadBase
from NodoAVL import NodoAVL

class GestorBDGenerico:
    def __init__(self, archivo_json: str, clase_entidad: Type[EntidadBase], nombre_entidad: str):
        """
        Este método será responsable de inicializar el gestor de base de datos genérico

        Args:
            archivo_json (str): El nombre del archivo JSON donde se almacenan los datos
            clase_entidad (Type[EntidadBase]): La clase de la entidad a gestionar
            nombre_entidad (str): El nombre de la entidad en singular (para mensajes)
        """
        self.directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.archivo_json = os.path.join(self.directorio_actual, archivo_json)
        self.clase_entidad = clase_entidad
        self.nombre_entidad = nombre_entidad
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
                    print(f"[INFO] Cargando {len(datos)} {self.nombre_entidad}s desde el archivo...")
                    for d in datos:
                        entidad = self.clase_entidad.from_dict(d)
                        self.arbol.raiz = self.arbol.insertar(self.arbol.raiz, entidad, mostrar_mensajes=False)
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
            datos.append(nodo.entidad.to_dict())
            self._recolectar_datos(nodo.derecha, datos)

    def agregar_entidad(self, entidad: EntidadBase):
        """
        Este método será responsable de agregar una entidad al árbol y guardarlo en JSON

        Args:
            entidad (EntidadBase): La entidad que se va a agregar
        """
        self.arbol.agregar_entidad(entidad)
        self.guardar_en_json()

    def eliminar_entidad(self, codigo: int) -> bool:
        """
        Este método será responsable de eliminar una entidad del árbol y actualizar el JSON

        Args:
            codigo (int): El código de la entidad que se va a eliminar

        Returns:
            bool: True si la entidad fue eliminada exitosamente, False si no existía
        """
        if self.arbol.buscar_por_codigo(codigo):
            self.arbol.eliminar_entidad(codigo)
            self.guardar_en_json()
            return True
        return False

    def actualizar_entidad(self, codigo: int, nueva_entidad: EntidadBase):
        """
        Este método será responsable de actualizar una entidad en el árbol y guardarlo en JSON

        Args:
            codigo (int): El código de la entidad que se va a actualizar
            nueva_entidad (EntidadBase): Los nuevos datos de la entidad
        """
        self.arbol.actualizar_entidad(codigo, nueva_entidad)
        self.guardar_en_json()

    def buscar_por_codigo(self, codigo: int) -> Optional[EntidadBase]:
        """
        Este método será responsable de buscar una entidad por su código

        Args:
            codigo (int): El código de la entidad que se busca

        Returns:
            Optional[EntidadBase]: La entidad encontrada o None si no existe
        """
        return self.arbol.buscar_por_codigo(codigo)

    def mostrar_inorden(self):
        """
        Este método será responsable de mostrar todas las entidades en orden por código
        """
        print(f"\n[LISTADO] {self.nombre_entidad}s en orden por código:")
        if self.arbol.raiz:
            self.arbol.inorden(self.arbol.raiz)
        else:
            print(f"No hay {self.nombre_entidad}s registrados.")

    def mostrar_arbol_visual(self):
        """
        Este método será responsable de mostrar la estructura visual del árbol AVL
        """
        print("\n[ESTRUCTURA] Árbol AVL:")
        if self.arbol.raiz:
            self.arbol.mostrar_arbol_binarytree()
        else:
            print("Árbol vacío")