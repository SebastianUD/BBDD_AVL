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
