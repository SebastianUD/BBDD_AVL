# Gestor de Base de Datos con Árboles AVL
from typing import Optional, List
import json
import os
from binarytree import Node as BinaryTreeNode


# Clase Estudiante (estructura de los datos)
class Estudiante:
    def __init__(self, codigo: int, nombre: str, correo: str, facultad: str, carrera: str):
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.facultad = facultad
        self.carrera = carrera

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "correo": self.correo,
            "facultad": self.facultad,
            "carrera": self.carrera
        }

    @staticmethod
    def from_dict(data: dict):
        return Estudiante(
            data["codigo"],
            data["nombre"],
            data["correo"],
            data["facultad"],
            data["carrera"]
        )

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Correo: {self.correo}, Facultad: {self.facultad}, Carrera: {self.carrera}"


# Nodo del árbol AVL
class NodoAVL:
    def __init__(self, estudiante: Estudiante):
        self.estudiante = estudiante
        self.izquierda: Optional[NodoAVL] = None
        self.derecha: Optional[NodoAVL] = None
        self.altura: int = 1

    def __str__(self):
        return f"[{self.estudiante.codigo}]"


# Árbol AVL completo con todas las operaciones
class ArbolAVL:
    def __init__(self):
        self.raiz: Optional[NodoAVL] = None

    def obtener_altura(self, nodo: Optional[NodoAVL]) -> int:
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo: Optional[NodoAVL]) -> int:
        return self.obtener_altura(nodo.derecha) - self.obtener_altura(nodo.izquierda) if nodo else 0

    def actualizar_altura(self, nodo: NodoAVL):
        """Actualiza la altura de un nodo basándose en sus hijos"""
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

    def rotacion_derecha(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierda
        T2 = x.derecha
        
        # Realizar rotación
        x.derecha = y
        y.izquierda = T2
        
        # Actualizar alturas
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        
        print(f"[BALANCEO] Rotación derecha en nodo {y.estudiante.codigo}")
        return x

    def rotacion_izquierda(self, x: NodoAVL) -> NodoAVL:
        y = x.derecha
        T2 = y.izquierda
        
        # Realizar rotación
        y.izquierda = x
        x.derecha = T2
        
        # Actualizar alturas
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        
        print(f"[BALANCEO] Rotación izquierda en nodo {x.estudiante.codigo}")
        return y

    def balancear_nodo(self, nodo: NodoAVL, codigo: int) -> NodoAVL:
        """Balancea un nodo si es necesario después de inserción/eliminación"""
        balance = self.obtener_balance(nodo)
        
        if abs(balance) > 1:
            print(f"[BALANCE] Nodo {nodo.estudiante.codigo} tiene balance {balance}")
        
        # Caso Izquierda-Izquierda
        if balance < -1 and codigo < nodo.izquierda.estudiante.codigo:
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Derecha
        if balance > 1 and codigo > nodo.derecha.estudiante.codigo:
            return self.rotacion_izquierda(nodo)
        
        # Caso Izquierda-Derecha
        if balance < -1 and codigo > nodo.izquierda.estudiante.codigo:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance > 1 and codigo < nodo.derecha.estudiante.codigo:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)
        
        return nodo

    def insertar(self, nodo: Optional[NodoAVL], estudiante: Estudiante, mostrar_mensajes: bool = True) -> NodoAVL:
        # Inserción normal BST
        if not nodo:
            if mostrar_mensajes:
                print(f"[INSERCIÓN] Nuevo nodo creado con código {estudiante.codigo}")
            return NodoAVL(estudiante)

        if estudiante.codigo < nodo.estudiante.codigo:
            nodo.izquierda = self.insertar(nodo.izquierda, estudiante, mostrar_mensajes)
        elif estudiante.codigo > nodo.estudiante.codigo:
            nodo.derecha = self.insertar(nodo.derecha, estudiante, mostrar_mensajes)
        else:
            if mostrar_mensajes:
                print(f"[ADVERTENCIA] Código {estudiante.codigo} ya existe. No se insertó.")
            return nodo

        # Actualizar altura y balancear
        self.actualizar_altura(nodo)
        return self.balancear_nodo(nodo, estudiante.codigo)

    def obtener_maximo_valor_nodo(self, nodo: NodoAVL) -> NodoAVL:
        """Encuentra el nodo con el valor máximo en el subárbol"""
        while nodo.derecha:
            nodo = nodo.derecha
        return nodo

    def eliminar(self, nodo: Optional[NodoAVL], codigo: int) -> Optional[NodoAVL]:
        if not nodo:
            print(f"[ADVERTENCIA] Código {codigo} no encontrado para eliminar.")
            return nodo

        # Búsqueda del nodo a eliminar
        if codigo < nodo.estudiante.codigo:
            nodo.izquierda = self.eliminar(nodo.izquierda, codigo)
        elif codigo > nodo.estudiante.codigo:
            nodo.derecha = self.eliminar(nodo.derecha, codigo)
        else:
            print(f"[ELIMINACIÓN] Eliminando nodo con código {codigo}")
            
            # Nodo con un hijo o sin hijos
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            
            # Nodo con dos hijos: obtener el predecesor
            temp = self.obtener_maximo_valor_nodo(nodo.izquierda)
            nodo.estudiante = temp.estudiante
            nodo.izquierda = self.eliminar(nodo.izquierda, temp.estudiante.codigo)

        # Actualizar altura
        self.actualizar_altura(nodo)
        
        # Balancear el árbol
        balance = self.obtener_balance(nodo)
        
        if abs(balance) > 1:
            print(f"[BALANCE] Nodo {nodo.estudiante.codigo} tiene balance {balance}")

        # Casos de balanceo
        if balance < -1:
            if self.obtener_balance(nodo.izquierda) <= 0:
                return self.rotacion_derecha(nodo)
            else:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)
        
        if balance > 1:
            if self.obtener_balance(nodo.derecha) >= 0:
                return self.rotacion_izquierda(nodo)
            else:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

        return nodo

    def agregar_estudiante(self, estudiante: Estudiante):
        print(f"\n[OPERACIÓN] Insertando estudiante con código {estudiante.codigo}")
        self.raiz = self.insertar(self.raiz, estudiante)

    def eliminar_estudiante(self, codigo: int):
        print(f"\n[OPERACIÓN] Eliminando estudiante con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)

    def actualizar_estudiante(self, codigo: int, nuevo_estudiante: Estudiante):
        """Actualiza un estudiante eliminando el antiguo e insertando el nuevo"""
        print(f"\n[OPERACIÓN] Actualizando estudiante con código {codigo}")
        self.raiz = self.eliminar(self.raiz, codigo)
        self.raiz = self.insertar(self.raiz, nuevo_estudiante)
        if codigo == nuevo_estudiante.codigo:
            print(f"[ACTUALIZACIÓN] Estudiante con código {codigo} actualizado.")

    def inorden(self, nodo: Optional[NodoAVL]):
        if nodo:
            self.inorden(nodo.izquierda)
            print(f"{nodo.estudiante.codigo} - {nodo.estudiante.nombre}")
            self.inorden(nodo.derecha)

    def buscar_por_codigo(self, codigo: int) -> Optional[Estudiante]:
        """Búsqueda binaria en el árbol AVL"""
        nodo = self.raiz
        while nodo:
            if codigo == nodo.estudiante.codigo:
                return nodo.estudiante
            elif codigo < nodo.estudiante.codigo:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        return None

    def convertir_a_binarytree(self, nodo: Optional[NodoAVL]) -> Optional[BinaryTreeNode]:
        """Convierte el árbol AVL a formato binarytree para visualización"""
        if not nodo:
            return None
        
        bt_node = BinaryTreeNode(nodo.estudiante.codigo)
        bt_node.left = self.convertir_a_binarytree(nodo.izquierda)
        bt_node.right = self.convertir_a_binarytree(nodo.derecha)
        
        return bt_node
    
    def mostrar_arbol_binarytree(self):
        """Muestra el árbol usando la librería binarytree"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        arbol_bt = self.convertir_a_binarytree(self.raiz)
        
        print("\n[VISUALIZACIÓN DEL ÁRBOL AVL]")
        print(arbol_bt)
        
        print(f"\nAltura del árbol: {1 + arbol_bt.height}")
        print(f"Número de nodos: {arbol_bt.size}")
        print(f"Número de hojas: {arbol_bt.leaf_count}")


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


# Interfaz interactiva
class InterfazInteractiva:
    def __init__(self):
        self.gestor = GestorBD()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pausar(self):
        input("\nPresione Enter para continuar...")

    def mostrar_menu(self):
        print("\n" + "="*50)
        print("   GESTOR DE BASE DE DATOS - ÁRBOLES AVL")
        print("="*50)
        print("1. Agregar estudiante")
        print("2. Buscar estudiante por código")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Mostrar todos los estudiantes (Inorden)")
        print("6. Mostrar estructura del árbol AVL")
        print("7. Salir")
        print("-"*50)

    def obtener_codigo(self, mensaje: str = "Código: ") -> Optional[int]:
        """Solicita y valida un código entero"""
        try:
            return int(input(mensaje))
        except ValueError:
            print("[ERROR] El código debe ser un número entero.")
            return None

    def solicitar_datos_estudiante(self, codigo_actual: Optional[int] = None) -> Optional[Estudiante]:
        """Solicita los datos de un estudiante con validación"""
        # Obtener código
        if codigo_actual is None:
            codigo = self.obtener_codigo()
            if codigo is None:
                return None
                
            # Verificar duplicados al agregar
            if self.gestor.buscar_por_codigo(codigo):
                print(f"[ADVERTENCIA] El código {codigo} ya existe. No se puede agregar un estudiante duplicado.")
                return None
        else:
            # Para actualización
            codigo_input = input(f"Código [{codigo_actual}]: ")
            if codigo_input:
                codigo = self.obtener_codigo("")
                if codigo is None:
                    codigo = codigo_actual
                elif codigo != codigo_actual and self.gestor.buscar_por_codigo(codigo):
                    print(f"[ADVERTENCIA] El código {codigo} ya existe. No se puede usar un código duplicado.")
                    return None
            else:
                codigo = codigo_actual
        
        # Solicitar resto de datos
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        facultad = input("Facultad: ")
        carrera = input("Carrera: ")
        
        # Validar que todos los campos estén completos
        if not all([nombre, correo, facultad, carrera]):
            print("[ERROR] Todos los campos son obligatorios.")
            return None
            
        return Estudiante(codigo, nombre, correo, facultad, carrera)

    def menu_agregar(self):
        print("\n--- AGREGAR ESTUDIANTE ---")
        estudiante = self.solicitar_datos_estudiante()
        if estudiante:
            self.gestor.agregar_estudiante(estudiante)
            print(f"\n[ÉXITO] Estudiante agregado correctamente.")
            self.gestor.mostrar_arbol_visual()

    def menu_buscar_codigo(self):
        print("\n--- BUSCAR POR CÓDIGO ---")
        codigo = self.obtener_codigo("Ingrese el código a buscar: ")
        if codigo is not None:
            estudiante = self.gestor.buscar_por_codigo(codigo)
            if estudiante:
                print(f"\n[ENCONTRADO] {estudiante}")
            else:
                print(f"\n[NO ENCONTRADO] No existe estudiante con código {codigo}")

    def menu_actualizar(self):
        print("\n--- ACTUALIZAR ESTUDIANTE ---")
        codigo = self.obtener_codigo("Código del estudiante a actualizar: ")
        if codigo is None:
            return
            
        estudiante_actual = self.gestor.buscar_por_codigo(codigo)
        if not estudiante_actual:
            print(f"\n[ERROR] No existe estudiante con código {codigo}")
            return
        
        print(f"\nDatos actuales: {estudiante_actual}")
        print("\nIngrese los nuevos datos (Enter para mantener el actual):")
        
        # Solicitar nuevos datos
        nuevo_codigo = codigo
        codigo_input = input(f"Nuevo código [{codigo}]: ")
        
        if codigo_input:
            # Validar nuevo código
            while True:
                try:
                    nuevo_codigo = int(codigo_input)
                    if nuevo_codigo != codigo and self.gestor.buscar_por_codigo(nuevo_codigo):
                        print(f"[ADVERTENCIA] El código {nuevo_codigo} ya existe. Intente con otro código.")
                        codigo_input = input("Nuevo código: ")
                        continue
                    break
                except ValueError:
                    print("[ERROR] El código debe ser un número entero.")
                    codigo_input = input("Nuevo código: ")
        
        # Obtener resto de datos con valores por defecto
        nuevo_nombre = input(f"Nombre [{estudiante_actual.nombre}]: ") or estudiante_actual.nombre
        nuevo_correo = input(f"Correo [{estudiante_actual.correo}]: ") or estudiante_actual.correo
        nueva_facultad = input(f"Facultad [{estudiante_actual.facultad}]: ") or estudiante_actual.facultad
        nueva_carrera = input(f"Carrera [{estudiante_actual.carrera}]: ") or estudiante_actual.carrera
        
        nuevo_estudiante = Estudiante(nuevo_codigo, nuevo_nombre, nuevo_correo, nueva_facultad, nueva_carrera)
        self.gestor.actualizar_estudiante(codigo, nuevo_estudiante)
        
        print(f"\n[ÉXITO] Estudiante actualizado correctamente.")
        self.gestor.mostrar_arbol_visual()

    def menu_eliminar(self):
        print("\n--- ELIMINAR ESTUDIANTE ---")
        codigo = self.obtener_codigo("Código del estudiante a eliminar: ")
        if codigo is None:
            return
            
        estudiante = self.gestor.buscar_por_codigo(codigo)
        if not estudiante:
            print(f"\n[ERROR] No existe estudiante con código {codigo}")
            return
            
        print(f"\nEstudiante a eliminar: {estudiante}")
        confirmar = input("¿Está seguro? (s/n): ").lower()
        
        if confirmar == 's':
            self.gestor.eliminar_estudiante(codigo)
            print(f"\n[ÉXITO] Estudiante eliminado correctamente.")
            self.gestor.mostrar_arbol_visual()
        else:
            print("\n[CANCELADO] Operación cancelada.")

    def ejecutar(self):
        """Bucle principal del programa"""
        opciones = {
            '1': self.menu_agregar,
            '2': self.menu_buscar_codigo,
            '3': self.menu_actualizar,
            '4': self.menu_eliminar,
            '5': self.gestor.mostrar_inorden,
            '6': self.gestor.mostrar_arbol_visual
        }
        
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            
            try:
                opcion = input("\nSeleccione una opción: ")
                
                if opcion == '7':
                    print("\nSaliendo del sistema...")
                    break
                elif opcion in opciones:
                    opciones[opcion]()
                else:
                    print("\n[ERROR] Opción no válida.")
                
                self.pausar()
                
            except Exception as e:
                print(f"\n[ERROR] Ha ocurrido un error: {e}")
                self.pausar()


# Programa principal
if __name__ == "__main__":
    interfaz = InterfazInteractiva()
    interfaz.ejecutar()
