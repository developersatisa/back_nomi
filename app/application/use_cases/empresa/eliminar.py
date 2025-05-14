from app.domain.repositories.empresa_repository import EmpresaRepository

class EliminarEmpresa:
    def __init__(self, repo: EmpresaRepository):
        self.repo = repo

    def ejecutar(self, id: int):
        self.repo.eliminar(id)
