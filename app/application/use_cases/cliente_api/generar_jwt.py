from app.domain.repositories.cliente_api_repository import ClienteApiRepository
from passlib.context import CryptContext
from app.infrastructure.security.jwt_utiles import crear_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def ejecutar(username: str, password: str, repo: ClienteApiRepository):
    cliente = repo.obtener_por_usuario(username)
    
    if not cliente:
        print(f"❌ Usuario '{username}' no encontrado.")
        raise Exception("Credenciales inválidas")

    print(f"🔍 Usuario encontrado: {cliente.username}")
    print(f"🔐 Comparando contraseña '{password}' con hash '{cliente.password_hash}'")

    if not pwd_context.verify(password, cliente.password_hash):
        print("❌ Contraseña incorrecta")
        raise Exception("Credenciales inválidas")

    print("✅ Credenciales válidas. Generando token...")

    scopes = ["read", "write"]
    if username == "admin":
        scopes.append("admin")

    return {
        "access_token": crear_token({"sub": cliente.username, "scopes": scopes})
    }

