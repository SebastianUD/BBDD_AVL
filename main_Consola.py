import os
from interfaces.InterfazEstudiante import InterfazEstudiante
from interfaces.InterfazMateria import InterfazMateria
from interfaces.InterfazProfesor import InterfazProfesor

class MenuPrincipal:
    def __init__(self):
        """
        Inicializa el menú principal con las interfaces de cada entidad
        """
        self.interfaces = {
            '1': InterfazEstudiante(),
            '2': InterfazMateria(),
            '3': InterfazProfesor()
        }
    
    def limpiar_pantalla(self):
        """
        Este método será responsable de limpiar la pantalla de la consola
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_principal(self):
        """
        Este método será responsable de mostrar el menú principal del sistema
        """
        print("\n" + "="*60)
        print("   SISTEMA DE GESTIÓN DE BASE DE DATOS NO RELACIONAL")
        print("="*60)
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Materias")
        print("3. Gestionar Profesores")
        print("4. Salir")
        print("-"*60)
    
    def ejecutar(self):
        """
        Este método será responsable de ejecutar el bucle principal del programa
        """
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu_principal()
            
            opcion = input("\nSeleccione una entidad a gestionar: ")
            
            if opcion == '4':
                print("\n¡Gracias por usar el sistema!")
                print("Saliendo del sistema...")
                break
            elif opcion in self.interfaces:
                # Ejecutar la interfaz seleccionada
                self.interfaces[opcion].ejecutar()
            else:
                print("\n[ERROR] Opción no válida.")
                input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    # Crear y ejecutar el menú principal
    menu = MenuPrincipal()
    menu.ejecutar()