from typing import Optional
from InterfazEntidadBase import InterfazEntidadBase
from Profesor import Profesor

class InterfazProfesor(InterfazEntidadBase):
    def __init__(self):
        """
        Inicializa la interfaz específica para gestionar profesores
        """
        super().__init__("profesores.json", Profesor, "profesor")
    
    def solicitar_datos_entidad(self, codigo_actual: Optional[int] = None) -> Optional[Profesor]:
        """
        Este método será responsable de solicitar los datos de un profesor con validación

        Args:
            codigo_actual (Optional[int]): El código actual del profesor (para actualizaciones)

        Returns:
            Optional[Profesor]: Una instancia de Profesor con los datos ingresados o None si hubo error
        """
        # Obtener código
        if codigo_actual is None:
            codigo = self.obtener_codigo()
            if codigo is None:
                return None
                
            # Verificar duplicados al agregar
            if self.gestor.buscar_por_codigo(codigo):
                print(f"[ADVERTENCIA] El código {codigo} ya existe. No se puede agregar un profesor duplicado.")
                return None
        else:
            # Para actualización, el código no se puede cambiar
            codigo = codigo_actual
        
        # Solicitar resto de datos
        if codigo_actual is None:
            # Agregando nuevo profesor
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")
            print("\nTipos de vinculación disponibles:")
            print("1. Planta")
            print("2. Cátedra")
            print("3. Ocasional")
            print("4. Visitante")
            
            vinculacion_opcion = input("Seleccione el tipo de vinculación (1-4): ")
            vinculaciones = {
                '1': 'Planta',
                '2': 'Cátedra',
                '3': 'Ocasional',
                '4': 'Visitante'
            }
            
            if vinculacion_opcion in vinculaciones:
                vinculacion = vinculaciones[vinculacion_opcion]
            else:
                print("[ERROR] Opción de vinculación no válida.")
                return None
        else:
            # Actualizando profesor existente
            profesor_actual = self.gestor.buscar_por_codigo(codigo)
            nombre = input(f"Nombre [{profesor_actual.nombre}]: ") or profesor_actual.nombre
            correo = input(f"Correo [{profesor_actual.correo}]: ") or profesor_actual.correo
            
            print(f"\nVinculación actual: {profesor_actual.vinculacion}")
            print("Tipos de vinculación disponibles:")
            print("1. Planta")
            print("2. Cátedra")
            print("3. Ocasional")
            print("4. Visitante")
            print("Enter para mantener la actual")
            
            vinculacion_opcion = input("Seleccione el tipo de vinculación (1-4): ")
            if vinculacion_opcion:
                vinculaciones = {
                    '1': 'Planta',
                    '2': 'Cátedra',
                    '3': 'Ocasional',
                    '4': 'Visitante'
                }
                
                if vinculacion_opcion in vinculaciones:
                    vinculacion = vinculaciones[vinculacion_opcion]
                else:
                    print("[ERROR] Opción de vinculación no válida.")
                    return None
            else:
                vinculacion = profesor_actual.vinculacion
        
        # Validar que todos los campos estén completos
        if not all([nombre, correo, vinculacion]):
            print("[ERROR] Todos los campos son obligatorios.")
            return None
        
        # Validar formato de correo básico
        if '@' not in correo or '.' not in correo:
            print("[ERROR] El correo debe tener un formato válido.")
            return None
            
        return Profesor(codigo, nombre, correo, vinculacion)
    
    def get_campos_busqueda(self) -> dict:
        """
        Este método retorna un diccionario con los campos de búsqueda disponibles para profesores
        
        Returns:
            dict: Diccionario con formato {opcion: nombre_campo}
        """
        return {
            '1': 'codigo',
            '2': 'nombre',
            '3': 'correo',
            '4': 'vinculacion'
        }
