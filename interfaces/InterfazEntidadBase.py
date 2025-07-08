import os
from abc import ABC, abstractmethod
from typing import Optional, Type
from models.EntidadBase import EntidadBase
from database.GestorBDGenerico import GestorBDGenerico
import json

class InterfazEntidadBase(ABC):
    def __init__(self, archivo_json: str, clase_entidad: Type[EntidadBase], nombre_entidad: str):
        """
        Este método será responsable de inicializar la interfaz base

        Args:
            archivo_json (str): El nombre del archivo JSON para esta entidad
            clase_entidad (Type[EntidadBase]): La clase de la entidad
            nombre_entidad (str): El nombre de la entidad en singular
        """
        self.gestor = GestorBDGenerico(archivo_json, clase_entidad, nombre_entidad)
        self.nombre_entidad = nombre_entidad
        self.clase_entidad = clase_entidad

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
        print(f"   GESTOR DE {self.nombre_entidad.upper()}S - ÁRBOLES AVL")
        print("="*50)
        print(f"1. Agregar {self.nombre_entidad}")
        print(f"2. Buscar {self.nombre_entidad} por campo")
        print(f"3. Actualizar {self.nombre_entidad}")
        print(f"4. Eliminar {self.nombre_entidad}")
        print(f"5. Mostrar {self.nombre_entidad}s en orden ascendente (Inorden)")
        print("6. Mostrar estructura del árbol AVL")
        print("7. Volver al menú principal")
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

    @abstractmethod
    def solicitar_datos_entidad(self, codigo_actual: Optional[int] = None) -> Optional[EntidadBase]:
        """
        Este método abstracto debe ser implementado por cada interfaz específica
        para solicitar los datos particulares de cada entidad

        Args:
            codigo_actual (Optional[int]): El código actual de la entidad (para actualizaciones)

        Returns:
            Optional[EntidadBase]: Una instancia de la entidad con los datos ingresados o None si hubo error
        """
        pass

    @abstractmethod
    def get_campos_busqueda(self) -> dict:
        """
        Este método abstracto debe retornar un diccionario con los campos de búsqueda disponibles
        
        Returns:
            dict: Diccionario con formato {opcion: nombre_campo}
        """
        pass

    def menu_agregar(self):
        """
        Este método será responsable de manejar el menú para agregar una nueva entidad
        """
        print(f"\n--- AGREGAR {self.nombre_entidad.upper()} ---")
        entidad = self.solicitar_datos_entidad()
        if entidad:
            self.gestor.agregar_entidad(entidad)
            print(f"\n[ÉXITO] {self.nombre_entidad} agregado correctamente.")
            self.gestor.mostrar_arbol_visual()

    def menu_buscar_entidad(self):
        """
        Este método será responsable de manejar el menú para buscar una entidad por diferentes campos
        Permite búsqueda por código o por otros campos específicos de la entidad
        """
        print(f"\n--- BUSCAR {self.nombre_entidad.upper()} ---")
        campos = self.get_campos_busqueda()
        
        print("1. Buscar por código")
        for opcion, campo in campos.items():
            if opcion != '1':  # El código ya está en la opción 1
                print(f"{opcion}. Buscar por {campo}")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            codigo = self.obtener_codigo("Ingrese el código a buscar: ")
            if codigo is not None:
                entidad = self.gestor.buscar_por_codigo(codigo)
                if entidad:
                    print(f"\n[ENCONTRADO] {entidad}")
                else:
                    print(f"\n[NO ENCONTRADO] No existe {self.nombre_entidad} con código {codigo}")
            return

        if opcion in campos and opcion != '1':
            campo = campos[opcion]
            valor_buscado = input(f"Ingrese el {campo} a buscar: ").strip()

            if not valor_buscado:
                print(f"[ERROR] El {campo} no puede estar vacío.")
                return

            try:
                with open(self.gestor.archivo_json, "r", encoding="utf-8") as archivo:
                    entidades = json.load(archivo)
                    encontrados = []
                    
                    # Detectar si el campo es numérico
                    campos_numericos = ["creditos", "horas", "numero_creditos", "numero_horas"]
                    es_numerico = any(num_campo in campo.lower().replace(" ", "_") for num_campo in campos_numericos)
                    
                    for d in entidades:
                        if campo in d:
                            valor_entidad = d[campo]
                            coincide = False
                            
                            if es_numerico:
                                # Para campos numéricos, comparar como números
                                try:
                                    if int(valor_entidad) == int(valor_buscado):
                                        coincide = True
                                except (ValueError, TypeError):
                                    continue
                            else:
                                # Para campos de texto, comparar en minúsculas
                                if str(valor_entidad).strip().lower() == valor_buscado.lower():
                                    coincide = True
                            
                            if coincide:
                                codigo = d["codigo"]
                                entidad = self.gestor.buscar_por_codigo(codigo)
                                if entidad:
                                    encontrados.append(entidad)

                    if encontrados:
                        print(f"\n[ENCONTRADOS] {len(encontrados)} {self.nombre_entidad}(s) con {campo} = {valor_buscado}:")
                        for e in encontrados:
                            print(f"- {e}")
                    else:
                        print(f"\n[NO ENCONTRADO] No se encontraron {self.nombre_entidad}s con {campo} = {valor_buscado}")

            except FileNotFoundError:
                print(f"[ERROR] No se pudo encontrar el archivo JSON: {self.gestor.archivo_json}")
            except json.JSONDecodeError:
                print(f"[ERROR] El archivo JSON está corrupto o mal formateado.")
            except Exception as e:
                print(f"[ERROR] Error inesperado al buscar: {e}")
        else:
            print("\n[ERROR] Opción no válida.")

    def menu_actualizar(self):
        """
        Este método será responsable de manejar el menú para actualizar una entidad existente
        """
        print(f"\n--- ACTUALIZAR {self.nombre_entidad.upper()} ---")
        codigo = self.obtener_codigo(f"Código del {self.nombre_entidad} a actualizar: ")
        if codigo is None:
            return
            
        entidad_actual = self.gestor.buscar_por_codigo(codigo)
        if not entidad_actual:
            print(f"\n[ERROR] No existe {self.nombre_entidad} con código {codigo}")
            return
        
        print(f"\nDatos actuales: {entidad_actual}")
        print("\nIngrese los nuevos datos (Enter para mantener el actual):")
        print(f"No se puede actualizar el código del {self.nombre_entidad} (es una clave primaria).")
        
        nueva_entidad = self.solicitar_datos_entidad(codigo)
        if nueva_entidad:
            self.gestor.actualizar_entidad(codigo, nueva_entidad)
            print(f"\n[ÉXITO] {self.nombre_entidad} actualizado correctamente.")
            self.gestor.mostrar_arbol_visual()

    def menu_eliminar(self):
        """
        Este método será responsable de manejar el menú para eliminar una entidad
        """
        print(f"\n--- ELIMINAR {self.nombre_entidad.upper()} ---")
        codigo = self.obtener_codigo(f"Código del {self.nombre_entidad} a eliminar: ")
        if codigo is None:
            return
            
        entidad = self.gestor.buscar_por_codigo(codigo)
        if not entidad:
            print(f"\n[ERROR] No existe {self.nombre_entidad} con código {codigo}")
            return
            
        print(f"\n{self.nombre_entidad} a eliminar: {entidad}")
        confirmar = input("¿Está seguro? (s/n): ").lower()
        
        if confirmar == 's':
            self.gestor.eliminar_entidad(codigo)
            print(f"\n[ÉXITO] {self.nombre_entidad} eliminado correctamente.")
            self.gestor.mostrar_arbol_visual()
        else:
            print("\n[CANCELADO] Operación cancelada.")

    def ejecutar(self):
        """
        Este método será responsable de ejecutar el bucle principal del programa
        """
        opciones = {
            '1': self.menu_agregar,
            '2': self.menu_buscar_entidad,
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
                    print("\nVolviendo al menú principal...")
                    break
                elif opcion in opciones:
                    opciones[opcion]()
                else:
                    print("\n[ERROR] Opción no válida.")
                
                self.pausar()
                
            except Exception as e:
                print(f"\n[ERROR] Ha ocurrido un error: {e}")
                self.pausar()