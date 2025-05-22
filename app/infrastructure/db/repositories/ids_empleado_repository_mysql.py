from app.domain.models.ids_empleado import IdsEmpleado
from app.domain.repositories.id_empleado_repository import IdsEmpleadoRepository
from typing import List
import sqlite3  # O usa el connector adecuado para MySQL

class IdsEmpleadoRepositoryMySQL(IdsEmpleadoRepository):
    def __init__(self, db_conn):
        self.conn = db_conn

    def guardar(self, ids_empleado: IdsEmpleado) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO ids_empleado (id_trabajador, tipo, Fini, Ffin)
            VALUES (?, ?, ?, ?)
            """,
            (ids_empleado.id_trabajador, ids_empleado.tipo, ids_empleado.fini, ids_empleado.ffin)
        )
        self.conn.commit()

    def eliminar(self, id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM ids_empleado WHERE id = ?", (id,))
        self.conn.commit()

    def listar(self) -> List[IdsEmpleado]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, id_trabajador, tipo, Fini, Ffin FROM ids_empleado")
        rows = cursor.fetchall()
        return [IdsEmpleado(*row) for row in rows]

    def obtener_por_id(self, id: int) -> IdsEmpleado | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, id_trabajador, tipo, Fini, Ffin FROM ids_empleado WHERE id = ?", (id,))
        row = cursor.fetchone()
        return IdsEmpleado(*row) if row else None
