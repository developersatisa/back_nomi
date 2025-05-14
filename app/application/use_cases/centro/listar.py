from app.domain.repositories.centro_repository import CentroRepository

class ListarCentros:
    def __init__(self, repo: CentroRepository):
        self.repo = repo

    def ejecutar(self):
        return self.repo.listar()
