class ObtenerOrganizacion:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, id):
        return self.repo.obtener_por_id(id)
