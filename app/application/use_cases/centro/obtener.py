from app.domain.repositories.centro_repository import CentroRepository

class ObtenerCentro:
    def __init__(self, repo: CentroRepository):
        self.repo = repo

    def ejecutar(self, id: int):
        return self.repo.obtener_por_id(id)
