from app.domain.repositories.empresa_repository import EmpresaRepository

class ListarEmpresas:
    def __init__(self, repo: EmpresaRepository):
        self.repo = repo

    def ejecutar(self):
        return self.repo.listar()
