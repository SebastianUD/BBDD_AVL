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
        print("2. Buscar estudiante por campo")
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

    def menu_buscar_estudiante(self):
        """
        Este método permite buscar un estudiante por código, nombre, correo, facultad o carrera.
        Para código, nombre y correo muestra un solo resultado.
        Para facultad y carrera muestra todos los estudiantes coincidentes.
        """
        print("\n--- BUSCAR ESTUDIANTE ---")
        print("1. Buscar por código")
        print("2. Buscar por nombre")
        print("3. Buscar por correo")
        print("4. Buscar por facultad")
        print("5. Buscar por carrera")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            codigo = self.obtener_codigo("Ingrese el código a buscar: ")
            if codigo is not None:
                estudiante = self.gestor.buscar_por_codigo(codigo)
                if estudiante:
                    print(f"\n[ENCONTRADO] {estudiante}")
                else:
                    print(f"\n[NO ENCONTRADO] No existe estudiante con código {codigo}")
            return

        campos_unicos = {'2': 'nombre', '3': 'correo'} #Campos con un unico posible resultado
        campos_multiples = {'4': 'facultad', '5': 'carrera'} #Campos con múltiples posibles resultados

        if opcion in campos_unicos or opcion in campos_multiples:
            campo = campos_unicos.get(opcion) or campos_multiples.get(opcion)
            valor_buscado = input(f"Ingrese el {campo} a buscar: ").strip().lower()

            if not valor_buscado:
                print(f"[ERROR] El {campo} no puede estar vacío.")
                return

            try:
                with open(self.gestor.archivo_json, "r", encoding="utf-8") as archivo:
                    estudiantes = json.load(archivo)

                    if opcion in campos_unicos:
                        for d in estudiantes:
                            if d[campo].strip().lower() == valor_buscado:
                                codigo = d["codigo"]
                                estudiante = self.gestor.buscar_por_codigo(codigo)
                                if estudiante:
                                    print(f"\n[ENCONTRADO] {estudiante}")
                                else:
                                    print(f"\n[ERROR] Estudiante con código {codigo} no encontrado.")
                                return
                        print(f"\n[NO ENCONTRADO] No se encontró ningún estudiante con ese {campo}")

                    else:  # Facultad o carrera (múltiples resultados)
                        encontrados = []
                        for d in estudiantes:
                            if d[campo].strip().lower() == valor_buscado:
                                codigo = d["codigo"]
                                estudiante = self.gestor.buscar_por_codigo(codigo)
                                if estudiante:
                                    encontrados.append(estudiante)

                        if encontrados:
                            print(f"\n[ENCONTRADOS] {len(encontrados)} estudiantes con {campo} = {valor_buscado}:")
                            for e in encontrados:
                                print(f"- {e}")
                        else:
                            print(f"\n[NO ENCONTRADO] No se encontraron estudiantes con {campo} = {valor_buscado}")

            except Exception as e:
                print(f"[ERROR] No se pudo abrir el archivo JSON: {e}")
        else:
            print("\n[ERROR] Opción no válida.")

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
        
        
        print("No se puede actualizar el código del estudiante (es una clave primaria).")
        # Obtener resto de datos con valores por defecto
        nuevo_nombre = input(f"Nombre [{estudiante_actual.nombre}]: ") or estudiante_actual.nombre
        nuevo_correo = input(f"Correo [{estudiante_actual.correo}]: ") or estudiante_actual.correo
        nueva_facultad = input(f"Facultad [{estudiante_actual.facultad}]: ") or estudiante_actual.facultad
        nueva_carrera = input(f"Carrera [{estudiante_actual.carrera}]: ") or estudiante_actual.carrera
        
        nuevo_estudiante = Estudiante(codigo, nuevo_nombre, nuevo_correo, nueva_facultad, nueva_carrera)
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
            '2': self.menu_buscar_estudiante,
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
