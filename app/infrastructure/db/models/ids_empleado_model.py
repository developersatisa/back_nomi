from dataclasses import dataclass
from datetime import date

@dataclass
class IdsEmpleadoModel:
    id: int
    id_trabajador: int
    tipo: str
    fini: date
    ffin: date
