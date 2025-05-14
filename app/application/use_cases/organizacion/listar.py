class ListarOrganizaciones:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self):
        return self.repo.listar()
