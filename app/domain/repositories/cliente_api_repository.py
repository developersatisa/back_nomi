from abc import ABC, abstractmethod
from app.domain.models.cliente_api import ClienteApi

class ClienteApiRepository(ABC):

    @abstractmethod
    def obtener_por_usuario(self, username: str) -> ClienteApi | None:
        pass

    @abstractmethod
    def guardar(self, cliente: ClienteApi) -> None:
        pass
