from fastapi import APIRouter, Depends, HTTPException, Body, Path, Security
from sqlalchemy.orm import Session

from app.infrastructure.db.session import get_session
from app.infrastructure.security.deps import get_current_user
from app.infrastructure.db.repositories.centro_repository_mysql import CentroRepositoryMySQL

from app.application.use_cases.centro.crear import CrearCentro
from app.application.use_cases.centro.obtener import ObtenerCentro
from app.application.use_cases.centro.listar import ListarCentros
from app.application.use_cases.centro.eliminar import EliminarCentro

router = APIRouter(prefix="/centros", tags=["Centros"])

def get_repo(session: Session = Depends(get_session)):
    return CentroRepositoryMySQL(session)

@router.post("/", summary="Crear centro")
def crear(
    id_empresa: int = Body(...),
    nombre: str = Body(...),
    direccion: str = Body(...),
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["write"])
):
    CrearCentro(repo).ejecutar(id_empresa, nombre, direccion)
    return {"mensaje": "Centro creado"}

@router.get("/", summary="Listar centros")
def listar(
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["read"])
):
    return ListarCentros(repo).ejecutar()

@router.get("/{id}", summary="Obtener centro por ID")
def obtener(
    id: int = Path(...),
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["read"])
):
    centro = ObtenerCentro(repo).ejecutar(id)
    if not centro:
        raise HTTPException(404, detail="Centro no encontrado")
    return centro

@router.delete("/{id}", summary="Eliminar centro")
def eliminar(
    id: int = Path(...),
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["write"])
):
    EliminarCentro(repo).ejecutar(id)
    return {"mensaje": "Centro eliminado"}
