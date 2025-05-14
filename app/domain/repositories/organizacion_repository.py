from abc import ABC, abstractmethod
from app.domain.models.organizacion import Organizacion

class OrganizacionRepository(ABC):

    @abstractmethod
    def guardar(self, organizacion: Organizacion): pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Organizacion: pass

    @abstractmethod
    def listar(self) -> list[Organizacion]: pass

    @abstractmethod
    def eliminar(self, id: int): pass
