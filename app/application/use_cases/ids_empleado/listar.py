from app.domain.repositories.id_empleado_repository import IdsEmpleadoRepository

class ListarIdsEmpleado:
    def __init__(self, repo: IdsEmpleadoRepository):
        self.repo = repo

    def ejecutar(self):
        return self.repo.listar()
