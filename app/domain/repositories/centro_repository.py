from abc import ABC, abstractmethod
from app.domain.models.centro import Centro

class CentroRepository(ABC):
    @abstractmethod
    def guardar(self, centro: Centro): pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Centro: pass

    @abstractmethod
    def listar(self) -> list[Centro]: pass

    @abstractmethod
    def eliminar(self, id: int): pass
