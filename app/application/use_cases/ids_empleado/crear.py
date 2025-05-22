from app.domain.models.ids_empleado import IdsEmpleado
from app.domain.repositories.id_empleado_repository import IdsEmpleadoRepository
from datetime import date

class CrearIdsEmpleado:
    def __init__(self, repo: IdsEmpleadoRepository):
        self.repo = repo

    def ejecutar(self, id_trabajador: int, tipo: str, fini: date, ffin: date):
        nuevo_id = IdsEmpleado(id=None, id_trabajador=id_trabajador, tipo=tipo, fini=fini, ffin=ffin)
        self.repo.guardar(nuevo_id)
