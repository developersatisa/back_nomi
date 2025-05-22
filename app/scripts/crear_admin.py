from app.application.use_cases.cliente_api import crear_cliente
from app.infrastructure.db.repositories.cliente_api_repository_mysql import ClienteApiRepositoryMySQL
from app.infrastructure.config import settings

repo = ClienteApiRepositoryMySQL()
password = settings.pass_admin_user

crear_cliente.ejecutar("admin", password, repo)
print("✅ Usuario admin creado correctamente con la contraseña del .env")
