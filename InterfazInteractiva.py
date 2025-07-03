import os
import json
from typing import Optional, List
from ArbolAVL import ArbolAVL
from Estudiante import Estudiante
from NodoAVL import NodoAVL
from GestorBD import GestorBD

# Interfaz interactiva
class InterfazInteractiva:
    def __init__(self):
        """
        Este método será responsable de inicializar la interfaz interactiva

        """
        self.gestor = GestorBD()

    def limpiar_pantalla(self):
        """
        Este método será responsable de limpiar la pantalla de la consola

        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def pausar(self):
        """
        Este método será responsable de pausar la ejecución hasta que el usuario presione Enter

        """
        input("\nPresione Enter para continuar...")

    def mostrar_menu(self):
        """
        Este método será responsable de mostrar el menú principal del sistema

        """
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
        """
        Este método será responsable de solicitar y validar un código entero

        Args:
            mensaje (str): El mensaje que se muestra al usuario para solicitar el código

        Returns:
            Optional[int]: El código entero válido ingresado por el usuario o None si hubo error
        """
        try:
            return int(input(mensaje))
        except ValueError:
            print("[ERROR] El código debe ser un número entero.")
            return None

    def solicitar_datos_estudiante(self, codigo_actual: Optional[int] = None) -> Optional[Estudiante]:
        """
        Este método será responsable de solicitar los datos de un estudiante con validación

        Args:
            codigo_actual (Optional[int]): El código actual del estudiante (para actualizaciones)

        Returns:
            Optional[Estudiante]: Una instancia de Estudiante con los datos ingresados o None si hubo error
        """
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
        """
        Este método será responsable de manejar el menú para agregar un nuevo estudiante

        """
        print("\n--- AGREGAR ESTUDIANTE ---")
        estudiante = self.solicitar_datos_estudiante()
        if estudiante:
            self.gestor.agregar_estudiante(estudiante)
            print(f"\n[ÉXITO] Estudiante agregado correctamente.")
            self.gestor.mostrar_arbol_visual()

    def menu_buscar_codigo(self):
        """
        Este método será responsable de manejar el menú para buscar un estudiante por código

        """
        print("\n--- BUSCAR POR CÓDIGO ---")
        codigo = self.obtener_codigo("Ingrese el código a buscar: ")
        if codigo is not None:
            estudiante = self.gestor.buscar_por_codigo(codigo)
            if estudiante:
                print(f"\n[ENCONTRADO] {estudiante}")
            else:
                print(f"\n[NO ENCONTRADO] No existe estudiante con código {codigo}")

    def menu_actualizar(self):
        """
        Este método será responsable de manejar el menú para actualizar un estudiante existente

        """
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
        """
        Este método será responsable de manejar el menú para eliminar un estudiante

        """
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
        """
        Este método será responsable de ejecutar el bucle principal del programa

        """
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
