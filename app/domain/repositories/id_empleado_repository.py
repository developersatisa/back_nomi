from abc import ABC, abstractmethod
from app.domain.models.ids_empleado import IdsEmpleado
from typing import List

class IdsEmpleadoRepository(ABC):

    @abstractmethod
    def guardar(self, ids_empleado: IdsEmpleado) -> None:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def listar(self) -> List[IdsEmpleado]:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> IdsEmpleado | None:
        pass
