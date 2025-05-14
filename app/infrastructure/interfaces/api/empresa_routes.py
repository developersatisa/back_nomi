from fastapi import APIRouter, Depends, HTTPException, Body, Path
from sqlalchemy.orm import Session

from app.infrastructure.db.session import get_session
from app.infrastructure.db.repositories.empresa_repository_mysql import EmpresaRepositoryMySQL

from app.application.use_cases.empresa.crear import CrearEmpresa
from app.application.use_cases.empresa.obtener import ObtenerEmpresa
from app.application.use_cases.empresa.listar import ListarEmpresas
from app.application.use_cases.empresa.eliminar import EliminarEmpresa

router = APIRouter(prefix="/empresas", tags=["Empresas"])

def get_repo(session: Session = Depends(get_session)):
    return EmpresaRepositoryMySQL(session)

@router.post("/", summary="Crear empresa")
def crear(
    id_organizacion: int = Body(...),
    codigop: str = Body(...),
    nombre: str = Body(...),
    cif: str = Body(...),
    repo = Depends(get_repo)
):
    CrearEmpresa(repo).ejecutar(id_organizacion, codigop, nombre, cif)
    return {"mensaje": "Empresa creada"}

@router.get("/", summary="Listar empresas")
def listar(repo = Depends(get_repo)):
    return ListarEmpresas(repo).ejecutar()

@router.get("/{id}", summary="Obtener empresa por ID")
def obtener(id: int = Path(...), repo = Depends(get_repo)):
    empresa = ObtenerEmpresa(repo).ejecutar(id)
    if not empresa:
        raise HTTPException(404, detail="Empresa no encontrada")
    return empresa

@router.delete("/{id}", summary="Eliminar empresa")
def eliminar(id: int = Path(...), repo = Depends(get_repo)):
    EliminarEmpresa(repo).ejecutar(id)
    return {"mensaje": "Empresa eliminada"}
