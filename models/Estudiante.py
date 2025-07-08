# Clase Estudiante (estructura de los datos)
from models.EntidadBase import EntidadBase

class Estudiante(EntidadBase):
    def __init__(self, codigo: int, nombre: str, correo: str, facultad: str, carrera: str):
        """
        Este método será responsable de crear una nueva instancia de estudiante

        Args:
            codigo (int): El código único de identificación del estudiante
            nombre (str): El nombre completo del estudiante
            correo (str): La dirección de correo electrónico del estudiante
            facultad (str): La facultad a la que pertenece el estudiante
            carrera (str): El programa académico o carrera del estudiante
        """
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.facultad = facultad
        self.carrera = carrera

    def get_codigo(self) -> int:
        return self.codigo

    def to_dict(self):
        """
        Este método será responsable de convertir la instancia de estudiante a formato diccionario

        Returns:
            dict: Un diccionario que contiene todos los atributos del estudiante con sus valores correspondientes
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "correo": self.correo,
            "facultad": self.facultad,
            "carrera": self.carrera
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Este método será responsable de crear una instancia de estudiante a partir de un diccionario

        Args:
            data (dict): Un diccionario que contiene los datos del estudiante con las claves: codigo, nombre, correo, facultad, carrera

        Returns:
            Estudiante: Una nueva instancia de estudiante creada a partir de los datos del diccionario
        """
        return Estudiante(
            data["codigo"],
            data["nombre"],
            data["correo"],
            data["facultad"],
            data["carrera"]
        )

    def __str__(self):
        """
        Este método será responsable de proporcionar una representación en cadena del estudiante

        Returns:
            str: Una cadena formateada que contiene toda la información del estudiante
        """
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Correo: {self.correo}, Facultad: {self.facultad}, Carrera: {self.carrera}"
