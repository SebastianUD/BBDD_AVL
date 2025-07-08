"""
Módulo para gestionar instancias singleton de los gestores de base de datos.
Esto evita que se recarguen los datos innecesariamente cada vez que se navega entre ventanas.
"""

from database.GestorBDGenerico import GestorBDGenerico
from models.Estudiante import Estudiante
from models.Profesor import Profesor
from models.Materia import Materia

class GestorInstancias:
    """
    Clase singleton para gestionar las instancias únicas de los gestores de base de datos.
    """
    _instancia = None
    _gestores = {}
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def get_gestor_estudiantes(self):
        """
        Obtiene la instancia única del gestor de estudiantes.
        
        Returns:
            GestorBDGenerico: Instancia del gestor de estudiantes
        """
        if 'estudiantes' not in self._gestores:
            print("[INFO] Creando gestor de estudiantes por primera vez...")
            self._gestores['estudiantes'] = GestorBDGenerico(
                "data/estudiantes.json", 
                Estudiante, 
                "estudiante"
            )
        return self._gestores['estudiantes']
    
    def get_gestor_profesores(self):
        """
        Obtiene la instancia única del gestor de profesores.
        
        Returns:
            GestorBDGenerico: Instancia del gestor de profesores
        """
        if 'profesores' not in self._gestores:
            print("[INFO] Creando gestor de profesores por primera vez...")
            self._gestores['profesores'] = GestorBDGenerico(
                "data/profesores.json", 
                Profesor, 
                "profesor"
            )
        return self._gestores['profesores']
    
    def get_gestor_materias(self):
        """
        Obtiene la instancia única del gestor de materias.
        
        Returns:
            GestorBDGenerico: Instancia del gestor de materias
        """
        if 'materias' not in self._gestores:
            print("[INFO] Creando gestor de materias por primera vez...")
            self._gestores['materias'] = GestorBDGenerico(
                "data/materias.json", 
                Materia, 
                "materia"
            )
        return self._gestores['materias']

# Instancia global del gestor de instancias
gestor_instancias = GestorInstancias()

# Funciones de conveniencia para obtener los gestores
def get_gestor_estudiantes():
    """Función de conveniencia para obtener el gestor de estudiantes"""
    return gestor_instancias.get_gestor_estudiantes()

def get_gestor_profesores():
    """Función de conveniencia para obtener el gestor de profesores"""
    return gestor_instancias.get_gestor_profesores()

def get_gestor_materias():
    """Función de conveniencia para obtener el gestor de materias"""
    return gestor_instancias.get_gestor_materias() 