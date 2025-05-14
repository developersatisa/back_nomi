from abc import ABC, abstractmethod
from app.domain.models.empresa import Empresa

class EmpresaRepository(ABC):

    @abstractmethod
    def guardar(self, empresa: Empresa): pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Empresa: pass

    @abstractmethod
    def listar(self) -> list[Empresa]: pass

    @abstractmethod
    def eliminar(self, id: int): pass
