import requests

BASE_URL = "http://localhost:8000"

def test_crear_organizaciones():
    print("Creando organizaciones de prueba...")
    datos = [
        {"nombre": "Org Uno", "alias": "UNO"},
        {"nombre": "Org Dos", "alias": "DOS"},
    ]
    for data in datos:
        response = requests.post(f"{BASE_URL}/organizaciones", json=data)
        print("POST /organizaciones", response.status_code, response.json())

def test_listar_organizaciones():
    response = requests.get(f"{BASE_URL}/organizaciones")
    print("GET /organizaciones", response.status_code, response.json())
    return response.json()

def test_crear_empresas(id_organizacion):
    print("Creando empresas para organización:", id_organizacion)
    datos = [
        {"id_organizacion": id_organizacion, "codigop": "EMP001", "nombre": "Empresa Uno", "cif": "CIF001"},
        {"id_organizacion": id_organizacion, "codigop": "EMP002", "nombre": "Empresa Dos", "cif": "CIF002"},
    ]
    for data in datos:
        response = requests.post(f"{BASE_URL}/empresas", json=data)
        print("POST /empresas", response.status_code, response.json())

def test_listar_empresas():
    response = requests.get(f"{BASE_URL}/empresas")
    print("GET /empresas", response.status_code, response.json())

def test_obtener_empresa(id):
    response = requests.get(f"{BASE_URL}/empresas/{id}")
    print(f"GET /empresas/{id}", response.status_code, response.json())

def test_eliminar_empresa(id):
    response = requests.delete(f"{BASE_URL}/empresas/{id}")
    print(f"DELETE /empresas/{id}", response.status_code, response.json())

if __name__ == "__main__":
    test_crear_organizaciones()
    organizaciones = test_listar_organizaciones()
    if organizaciones:
        org_id = organizaciones[0]["id"]
        test_crear_empresas(org_id)
        test_listar_empresas()
        test_obtener_empresa(1)
        test_eliminar_empresa(1)
        test_listar_empresas()
