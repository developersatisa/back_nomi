from app.domain.models.cliente_api import ClienteApi
from app.domain.repositories.cliente_api_repository import ClienteApiRepository
from app.infrastructure.db.models.cliente_api_model import ClienteApiModel
from app.infrastructure.db.session import SessionLocal

class ClienteApiRepositoryMySQL(ClienteApiRepository):

    def __init__(self):
        self.db = SessionLocal()

    def obtener_por_usuario(self, username: str) -> ClienteApi | None:
        modelo = self.db.query(ClienteApiModel).filter_by(username=username).first()
        if modelo:
            return ClienteApi(modelo.username, modelo.password_hash)
        return None

    def guardar(self, cliente: ClienteApi):
        modelo = ClienteApiModel(username=cliente.username, password_hash=cliente.password_hash)
        self.db.add(modelo)
        self.db.commit()
