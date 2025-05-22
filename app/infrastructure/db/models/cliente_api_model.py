from sqlalchemy import Column, String
from app.infrastructure.db.session import Base

class ClienteApiModel(Base):
    __tablename__ = "clientes_api"
    username = Column(String(60), primary_key=True, index=True)
    password_hash = Column(String(255))
