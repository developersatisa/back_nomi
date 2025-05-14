from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.session import Base

class EmpresaModel(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_organizacion = Column(Integer, ForeignKey("organizaciones.id"), nullable=False)
    codigop = Column(String(255), nullable=False)
    nombre = Column(String(255), nullable=False)
    cif = Column(String(255), nullable=False, unique=True)

    # RELACIÓN OPCIONAL (si luego quieres navegar desde la infraestructura)
    organizacion = relationship("OrganizacionModel", backref="empresas")
