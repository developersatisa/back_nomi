class CrearOrganizacion:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, organizacion):
        self.repo.guardar(organizacion)

