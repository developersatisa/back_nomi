from app.domain.models.empresa import Empresa
from app.domain.repositories.empresa_repository import EmpresaRepository

class CrearEmpresa:
    def __init__(self, repo: EmpresaRepository):
        self.repo = repo

    def ejecutar(self, id_organizacion: int, codigop: str, nombre: str, cif: str):
        empresa = Empresa(id=None, id_organizacion=id_organizacion, codigop=codigop, nombre=nombre, cif=cif)
        self.repo.guardar(empresa)
