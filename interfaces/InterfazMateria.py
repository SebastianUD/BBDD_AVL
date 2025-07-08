from typing import Optional
from interfaces.InterfazEntidadBase import InterfazEntidadBase
from models.Materia import Materia

class InterfazMateria(InterfazEntidadBase):
    def __init__(self):
        """
        Inicializa la interfaz específica para gestionar materias
        """
        super().__init__("data/materias.json", Materia, "materia")
    
    def solicitar_datos_entidad(self, codigo_actual: Optional[int] = None) -> Optional[Materia]:
        """
        Este método será responsable de solicitar los datos de una materia con validación

        Args:
            codigo_actual (Optional[int]): El código actual de la materia (para actualizaciones)

        Returns:
            Optional[Materia]: Una instancia de Materia con los datos ingresados o None si hubo error
        """
        # Obtener código
        if codigo_actual is None:
            codigo = self.obtener_codigo()
            if codigo is None:
                return None
                
            # Verificar duplicados al agregar
            if self.gestor.buscar_por_codigo(codigo):
                print(f"[ADVERTENCIA] El código {codigo} ya existe. No se puede agregar una materia duplicada.")
                return None
        else:
            # Para actualización, el código no se puede cambiar
            codigo = codigo_actual
        
        # Solicitar resto de datos
        if codigo_actual is None:
            # Agregando nueva materia
            nombre = input("Nombre de la materia: ")
            
            # Validar créditos
            try:
                creditos = int(input("Número de créditos: "))
                if creditos <= 0:
                    print("[ERROR] Los créditos deben ser un número positivo.")
                    return None
            except ValueError:
                print("[ERROR] Los créditos deben ser un número entero.")
                return None
            
            # Validar horas por semana
            try:
                horas_semana = int(input("Horas por semana: "))
                if horas_semana <= 0:
                    print("[ERROR] Las horas por semana deben ser un número positivo.")
                    return None
            except ValueError:
                print("[ERROR] Las horas por semana deben ser un número entero.")
                return None
        else:
            # Actualizando materia existente
            materia_actual = self.gestor.buscar_por_codigo(codigo)
            nombre = input(f"Nombre [{materia_actual.nombre}]: ") or materia_actual.nombre
            
            # Validar créditos
            creditos_input = input(f"Créditos [{materia_actual.creditos}]: ")
            if creditos_input:
                try:
                    creditos = int(creditos_input)
                    if creditos <= 0:
                        print("[ERROR] Los créditos deben ser un número positivo.")
                        return None
                except ValueError:
                    print("[ERROR] Los créditos deben ser un número entero.")
                    return None
            else:
                creditos = materia_actual.creditos
            
            # Validar horas por semana
            horas_input = input(f"Horas por semana [{materia_actual.horas_semana}]: ")
            if horas_input:
                try:
                    horas_semana = int(horas_input)
                    if horas_semana <= 0:
                        print("[ERROR] Las horas por semana deben ser un número positivo.")
                        return None
                except ValueError:
                    print("[ERROR] Las horas por semana deben ser un número entero.")
                    return None
            else:
                horas_semana = materia_actual.horas_semana
        
        # Validar que todos los campos estén completos
        if not nombre:
            print("[ERROR] El nombre es obligatorio.")
            return None
            
        return Materia(codigo, nombre, creditos, horas_semana)
    
    def get_campos_busqueda(self) -> dict:
        """
        Este método retorna un diccionario con los campos de búsqueda disponibles para materias
        
        Returns:
            dict: Diccionario con formato {opcion: nombre_campo}
        """
        return {
            '1': 'codigo',
            '2': 'nombre',
            '3': 'creditos',
            '4': 'horas_semana'
        }
