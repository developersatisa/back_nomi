from app.domain.repositories.empresa_repository import EmpresaRepository

class ObtenerEmpresa:
    def __init__(self, repo: EmpresaRepository):
        self.repo = repo

    def ejecutar(self, id: int):
        return self.repo.obtener_por_id(id)
