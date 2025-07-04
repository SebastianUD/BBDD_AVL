from EntidadBase import EntidadBase

class Profesor(EntidadBase):
    def __init__(self, codigo: int, nombre: str, correo: str, vinculacion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.vinculacion = vinculacion
    
    def get_codigo(self) -> int:
        return self.codigo
    
    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "correo": self.correo,
            "vinculacion": self.vinculacion
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["codigo"],
            data["nombre"],
            data["correo"],
            data["vinculacion"]
        )
    
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Correo: {self.correo}, Vinculación: {self.vinculacion}"
