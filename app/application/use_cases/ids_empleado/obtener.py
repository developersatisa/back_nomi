from app.domain.repositories.id_empleado_repository import IdsEmpleadoRepository

class ObtenerIdsEmpleado:
    def __init__(self, repo: IdsEmpleadoRepository):
        self.repo = repo

    def ejecutar(self, id: int):
        return self.repo.obtener_por_id(id)
