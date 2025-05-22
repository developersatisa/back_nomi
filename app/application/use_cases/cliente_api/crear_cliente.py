from app.domain.models.cliente_api import ClienteApi
from app.domain.repositories.cliente_api_repository import ClienteApiRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def ejecutar(username: str, password: str, repo: ClienteApiRepository):
    hash = pwd_context.hash(password)
    nuevo_cliente = ClienteApi(username=username, password_hash=hash)
    repo.guardar(nuevo_cliente)
    return {"msg": "Cliente creado"}
