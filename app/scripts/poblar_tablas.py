import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.infrastructure.db.session import SessionLocal, engine, Base
from app.infrastructure.db.models.organizacion_model import OrganizacionModel
from app.infrastructure.db.models.empresa_model import EmpresaModel
from app.infrastructure.db.models.centro_model import CentroModel

def crear_tablas():
    print("Creando tablas en la base de datos si no existen...")
    Base.metadata.create_all(bind=engine)     
    print("Tablas creadas.")

def poblar_organizaciones():
    session = SessionLocal()
    datos_falsos = [
        {"nombre": "Grupo ATISA", "alias": "ATISA"},
        {"nombre": "Soluciones Empresariales S.L.", "alias": "SOLUCIONES"},
        {"nombre": "TechLegal Consultores", "alias": "TECHLEGAL"},
        {"nombre": "Distribuciones Ferrer", "alias": "FERRER"},
        {"nombre": "Innovación Educativa", "alias": "EDUCA"}
    ]

    for data in datos_falsos:
        org = OrganizacionModel(nombre=data["nombre"], alias=data["alias"])
        session.add(org)

    session.commit()
    session.close()
    print("Organizaciones insertadas con éxito.")

def poblar_empresas():
    session = SessionLocal()
    organizaciones = session.query(OrganizacionModel).all()
    if not organizaciones:
        raise Exception("No hay organizaciones creadas. Primero pobla la tabla de organizaciones.")

    datos_falsos = [
        {"id_organizacion": organizaciones[0].id, "codigop": "EMP001", "nombre": "Empresa Uno", "cif": "A00000001"},
        {"id_organizacion": organizaciones[1].id, "codigop": "EMP002", "nombre": "Empresa Dos", "cif": "A00000002"},
        {"id_organizacion": organizaciones[0].id, "codigop": "EMP003", "nombre": "Empresa Tres", "cif": "A00000003"},
    ]

    for data in datos_falsos:
        empresa = EmpresaModel(
            id_organizacion=data["id_organizacion"],
            codigop=data["codigop"],
            nombre=data["nombre"],
            cif=data["cif"]
        )
        session.add(empresa)

    session.commit()
    session.close()
    print("Empresas insertadas con éxito.")

def poblar_centros():
    session = SessionLocal()
    empresas = session.query(EmpresaModel).all()
    if not empresas:
        raise Exception("No hay empresas creadas. Primero pobla la tabla de empresas.")

    datos_falsos = [
        {"id_empresa": empresas[0].id, "nombre": "Centro A", "direccion": "Calle Uno 123"},
        {"id_empresa": empresas[0].id, "nombre": "Centro B", "direccion": "Avenida Dos 456"},
        {"id_empresa": empresas[1].id, "nombre": "Centro C", "direccion": "Plaza Tres 789"},
    ]

    for data in datos_falsos:
        centro = CentroModel(
            id_empresa=data["id_empresa"],
            nombre=data["nombre"],
            direccion=data["direccion"]
        )
        session.add(centro)

    session.commit()
    session.close()
    print("Centros insertados con éxito.")

if __name__ == "__main__":
    crear_tablas()
    print("Poblando base de datos...")
    poblar_organizaciones()
    poblar_empresas()
    poblar_centros()
    print("Base de datos poblada.")
