class Empresa:
    def __init__(self, id: int | None, id_organizacion: int, codigop: str, nombre: str, cif: str):
        self.id = id
        self.id_organizacion = id_organizacion
        self.codigop = codigop
        self.nombre = nombre
        self.cif = cif
