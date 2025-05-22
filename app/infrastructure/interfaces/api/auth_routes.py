from fastapi import APIRouter,Security,Depends,HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
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
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        token = generar_jwt.ejecutar(form_data.username, form_data.password, repo)
        token["token_type"] = "bearer"  # 👈 Esto lo espera Swagger
        return token
    except Exception:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
