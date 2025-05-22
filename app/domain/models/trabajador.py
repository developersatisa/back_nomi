# app/domain/models/trabajador.py

from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date

class Trabajador:
    def __init__(self, id: int, id_organizacion: int, numeross: str, nombre: str,
                 apellido1: str, apellido2: str, fecha_nacimiento: date):
        self.id = id
        self.id_organizacion = id_organizacion
        self.numeross = numeross
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento

class TrabajadorRepository(ABC):
    @abstractmethod
    def crear(self, trabajador: Trabajador) -> Trabajador:
        pass

    @abstractmethod
    def obtener(self, trabajador_id: int) -> Optional[Trabajador]:
        pass

    @abstractmethod
    def listar(self) -> List[Trabajador]:
        pass

    @abstractmethod
    def eliminar(self, trabajador_id: int) -> None:
        pass
