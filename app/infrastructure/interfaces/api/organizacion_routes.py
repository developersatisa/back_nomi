from fastapi import APIRouter, Depends, Body, Path, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.db.session import get_session
from app.domain.models.organizacion import Organizacion
from app.infrastructure.db.repositories.organizacion_repository_mysql import OrganizacionRepositoryMySQL
from app.application.use_cases.organizacion.crear import CrearOrganizacion
from app.application.use_cases.organizacion.listar import ListarOrganizaciones
from app.application.use_cases.organizacion.obtener import ObtenerOrganizacion
from app.application.use_cases.organizacion.eliminar import EliminarOrganizacion

router = APIRouter(prefix="/organizaciones", tags=["Organizaciones"])

@router.post("/organizaciones")
def crear(nombre: str = Body(...), alias: str = Body(...), session: Session = Depends(get_session)):
    repo = OrganizacionRepositoryMySQL(session)
    caso = CrearOrganizacion(repo)
    organizacion = Organizacion(None, nombre, alias)
    caso.ejecutar(organizacion)
    return {"mensaje": "Organización creada"}

@router.get("/organizaciones")
def listar(session: Session = Depends(get_session)):
    repo = OrganizacionRepositoryMySQL(session)
    caso = ListarOrganizaciones(repo)
    return caso.ejecutar()

@router.get("/organizaciones/{id}")
def obtener(id: int = Path(...), session: Session = Depends(get_session)):
    repo = OrganizacionRepositoryMySQL(session)
    caso = ObtenerOrganizacion(repo)
    result = caso.ejecutar(id)
    if not result:
        raise HTTPException(404, "No encontrado")
    return result

@router.delete("/organizaciones/{id}")
def eliminar(id: int = Path(...), session: Session = Depends(get_session)):
    repo = OrganizacionRepositoryMySQL(session)
    caso = EliminarOrganizacion(repo)
    caso.ejecutar(id)
    return {"mensaje": "Organización eliminada"}
