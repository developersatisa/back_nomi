from fastapi import APIRouter, Depends, HTTPException, Body, Path,Security
from sqlalchemy.orm import Session
from datetime import date

from app.infrastructure.db.session import get_session
from app.infrastructure.security.deps import get_current_user
from app.infrastructure.db.repositories.ids_empleado_repository_mysql import IdsEmpleadoRepositoryMySQL

from app.application.use_cases.ids_empleado.crear import CrearIdsEmpleado
from app.application.use_cases.ids_empleado.obtener import ObtenerIdsEmpleado
from app.application.use_cases.ids_empleado.listar import ListarIdsEmpleado
from app.application.use_cases.ids_empleado.eliminar import EliminarIdsEmpleado

router = APIRouter(prefix="/ids_empleado", tags=["IDs Empleado"])

def get_repo(session: Session = Depends(get_session)):
    return IdsEmpleadoRepositoryMySQL(session)

@router.post("/", summary="Crear ID de empleado")
def crear(
    id_trabajador: int = Body(...),
    tipo: str = Body(...),
    fini: date = Body(...),
    ffin: date = Body(...),
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["write"])
):
    CrearIdsEmpleado(repo).ejecutar(id_trabajador, tipo, fini, ffin)
    return {"mensaje": "ID de empleado creado"}

@router.get("/", summary="Listar IDs de empleado")
def listar(
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["read"])
):
    return ListarIdsEmpleado(repo).ejecutar()

@router.get("/{id}", summary="Obtener ID de empleado")
def obtener(
    id: int = Path(...),
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["write"])
):
    resultado = ObtenerIdsEmpleado(repo).ejecutar(id)
    if not resultado:
        raise HTTPException(404, detail="ID de empleado no encontrado")
    return resultado

@router.delete("/{id}", summary="Eliminar ID de empleado")
def eliminar(
    id: int = Path(...),
    repo = Depends(get_repo),
    user=Security(get_current_user, scopes=["write"])
):
    EliminarIdsEmpleado(repo).ejecutar(id)
    return {"mensaje": "ID de empleado eliminado"}
