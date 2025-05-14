from app.domain.models.centro import Centro
from app.domain.repositories.centro_repository import CentroRepository
from app.infrastructure.db.models.centro_model import CentroModel

class CentroRepositoryMySQL(CentroRepository):
    def __init__(self, session):
        self.session = session

    def guardar(self, centro: Centro):
        model = CentroModel(
            id_empresa=centro.id_empresa,
            nombre=centro.nombre,
            direccion=centro.direccion
        )
        self.session.add(model)
        self.session.commit()

    def obtener_por_id(self, id: int):
        model = self.session.query(CentroModel).get(id)
        if model:
            return Centro(model.id, model.id_empresa, model.nombre, model.direccion)

    def listar(self):
        return [
            Centro(m.id, m.id_empresa, m.nombre, m.direccion)
            for m in self.session.query(CentroModel).all()
        ]

    def eliminar(self, id: int):
        model = self.session.query(CentroModel).get(id)
        if model:
            self.session.delete(model)
            self.session.commit()
