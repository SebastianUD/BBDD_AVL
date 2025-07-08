from typing import Optional
from interfaces.InterfazEntidadBase import InterfazEntidadBase
from models.Estudiante import Estudiante

class InterfazEstudiante(InterfazEntidadBase):
    def __init__(self):
        """
        Inicializa la interfaz específica para gestionar estudiantes
        """
        super().__init__("data/estudiantes.json", Estudiante, "estudiante")
    
    def solicitar_datos_entidad(self, codigo_actual: Optional[int] = None) -> Optional[Estudiante]:
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
            # Para actualización, el código no se puede cambiar
            codigo = codigo_actual
        
        # Solicitar resto de datos
        if codigo_actual is None:
            # Agregando nuevo estudiante
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")
            facultad = input("Facultad: ")
            carrera = input("Carrera: ")
        else:
            # Actualizando estudiante existente
            estudiante_actual = self.gestor.buscar_por_codigo(codigo)
            nombre = input(f"Nombre [{estudiante_actual.nombre}]: ") or estudiante_actual.nombre
            correo = input(f"Correo [{estudiante_actual.correo}]: ") or estudiante_actual.correo
            facultad = input(f"Facultad [{estudiante_actual.facultad}]: ") or estudiante_actual.facultad
            carrera = input(f"Carrera [{estudiante_actual.carrera}]: ") or estudiante_actual.carrera
        
        # Validar que todos los campos estén completos
        if not all([nombre, correo, facultad, carrera]):
            print("[ERROR] Todos los campos son obligatorios.")
            return None
    
        # Validar formato de correo básico
        if '@' not in correo or '.' not in correo:
            print("[ERROR] El correo debe tener un formato válido.")
            return None
                
        return Estudiante(codigo, nombre, correo, facultad, carrera)
    
    def get_campos_busqueda(self) -> dict:
        """
        Este método retorna un diccionario con los campos de búsqueda disponibles para estudiantes
        
        Returns:
            dict: Diccionario con formato {opcion: nombre_campo}
        """
        return {
            '1': 'codigo',
            '2': 'nombre',
            '3': 'correo',
            '4': 'facultad',
            '5': 'carrera'
        }
