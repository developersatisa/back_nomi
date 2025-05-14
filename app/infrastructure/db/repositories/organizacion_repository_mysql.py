from app.domain.models.organizacion import Organizacion
from app.domain.repositories.organizacion_repository import OrganizacionRepository
from app.infrastructure.db.models.organizacion_model import OrganizacionModel

class OrganizacionRepositoryMySQL(OrganizacionRepository):
    def __init__(self, session):
        self.session = session

    def guardar(self, organizacion: Organizacion):
        model = OrganizacionModel(nombre=organizacion.nombre, alias=organizacion.alias)
        self.session.add(model)
        self.session.commit()

    def obtener_por_id(self, id: int):
        model = self.session.query(OrganizacionModel).get(id)
        return Organizacion(model.id, model.nombre, model.alias) if model else None

    def listar(self):
        return [Organizacion(m.id, m.nombre, m.alias) for m in self.session.query(OrganizacionModel).all()]

    def eliminar(self, id: int):
        model = self.session.query(OrganizacionModel).get(id)
        if model:
            self.session.delete(model)
            self.session.commit()
