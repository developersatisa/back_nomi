from app.domain.repositories.id_empleado_repository import IdsEmpleadoRepository

class EliminarIdsEmpleado:
    def __init__(self, repo: IdsEmpleadoRepository):
        self.repo = repo

    def ejecutar(self, id: int):
        self.repo.eliminar(id)
