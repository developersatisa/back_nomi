class EliminarOrganizacion:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, id):
        return self.repo.eliminar(id)
