from app.domain.models.empresa import Empresa
from app.domain.repositories.empresa_repository import EmpresaRepository
from app.infrastructure.db.models.empresa_model import EmpresaModel

class EmpresaRepositoryMySQL(EmpresaRepository):
    def __init__(self, session):
        self.session = session

    def guardar(self, empresa: Empresa):
        model = EmpresaModel(
            id_organizacion=empresa.id_organizacion,
            codigop=empresa.codigop,
            nombre=empresa.nombre,
            cif=empresa.cif
        )
        self.session.add(model)
        self.session.commit()

    def obtener_por_id(self, id: int):
        model = self.session.query(EmpresaModel).get(id)
        if model:
            return Empresa(model.id, model.id_organizacion, model.codigop, model.nombre, model.cif)

    def listar(self):
        return [
            Empresa(m.id, m.id_organizacion, m.codigop, m.nombre, m.cif)
            for m in self.session.query(EmpresaModel).all()
        ]

    def eliminar(self, id: int):
        model = self.session.query(EmpresaModel).get(id)
        if model:
            self.session.delete(model)
            self.session.commit()
