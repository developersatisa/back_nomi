from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from app.infrastructure.security.jwt_utiles import verificar_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
    scopes={"read": "Leer", "write": "Escribir", "admin": "Admin"}
)

def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")

    if not all(scope in payload.get("scopes", []) for scope in security_scopes.scopes):
        raise HTTPException(status_code=403, detail="No tienes permisos suficientes")

    return payload
