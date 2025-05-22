from fastapi import APIRouter,Security
from pydantic import BaseModel
from app.infrastructure.security.deps import get_current_user
from app.application.use_cases.cliente_api import crear_cliente, generar_jwt
from app.infrastructure.db.repositories.cliente_api_repository_mysql import ClienteApiRepositoryMySQL

router = APIRouter()
repo = ClienteApiRepositoryMySQL()

class AuthRequest(BaseModel):
    username: str
    password: str

@router.post("/auth/registro")
def registrar_cliente(data: AuthRequest, user=Security(get_current_user, scopes=["admin"])):
    return crear_cliente.ejecutar(data.username, data.password, repo)

@router.post("/auth/token")
def login(data: AuthRequest):
    return generar_jwt.ejecutar(data.username, data.password, repo)
