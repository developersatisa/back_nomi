from dataclasses import dataclass
from datetime import date

@dataclass
class IdsEmpleado:
    id: int | None
    id_trabajador: int
    tipo: str
    fini: date
    ffin: date
