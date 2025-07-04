from EntidadBase import EntidadBase

class Materia(EntidadBase):
    def __init__(self, codigo: int, nombre: str, creditos: int, horas_semana: int):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.horas_semana = horas_semana
    
    def get_codigo(self) -> int:
        return self.codigo
    
    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "creditos": self.creditos,
            "horas_semana": self.horas_semana
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["codigo"],
            data["nombre"],
            data["creditos"],
            data["horas_semana"]
        )
    
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Créditos: {self.creditos}, Horas/semana: {self.horas_semana}"
