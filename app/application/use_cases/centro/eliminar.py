from app.domain.repositories.centro_repository import CentroRepository

class EliminarCentro:
    def __init__(self, repo: CentroRepository):
        self.repo = repo

    def ejecutar(self, id: int):
        self.repo.eliminar(id)
