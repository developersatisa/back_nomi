from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.session import Base

class CentroModel(Base):
    __tablename__ = "centros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)

    # Relación opcional para navegar desde infraestructura
    empresa = relationship("EmpresaModel", backref="centros")
