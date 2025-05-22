import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.infrastructure.db.session import engine, Base
from app.infrastructure.db.models.cliente_api_model import ClienteApiModel

def crear_tablas():
    print("Creando tablas en la base de datos si no existen...")
    Base.metadata.create_all(bind=engine)     
    print("Tablas creadas.")

if __name__ == "__main__":
    crear_tablas()