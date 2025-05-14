from sqlalchemy import Column, Integer, String
from app.infrastructure.db.session import Base

class OrganizacionModel(Base):
    __tablename__ = "organizaciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    alias = Column(String(255))
