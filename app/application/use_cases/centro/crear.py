from app.domain.models.centro import Centro
from app.domain.repositories.centro_repository import CentroRepository

class CrearCentro:
    def __init__(self, repo: CentroRepository):
        self.repo = repo

    def ejecutar(self, id_empresa: int, nombre: str, direccion: str):
        centro = Centro(id=None, id_empresa=id_empresa, nombre=nombre, direccion=direccion)
        self.repo.guardar(centro)
