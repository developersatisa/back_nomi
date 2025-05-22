from fastapi import FastAPI
from app.infrastructure.interfaces.api.organizacion_routes import router as organizacion_router
from app.infrastructure.interfaces.api.empresa_routes import router as empresa_router
from app.infrastructure.interfaces.api.centro_routes import router as centro_router
from app.infrastructure.interfaces.api.ids_empleado_routes import router as ids_empleado_router
from app.infrastructure.interfaces.api.auth_routes import router as auth_router


app = FastAPI()
app.include_router(organizacion_router)
app.include_router(empresa_router)
app.include_router(centro_router)
app.include_router(ids_empleado_router)
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"mensaje": "Nomina en marcha"}
