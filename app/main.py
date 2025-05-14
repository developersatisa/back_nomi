from fastapi import FastAPI
from app.infrastructure.interfaces.api.organizacion_routes import router as organizacion_router
from app.infrastructure.interfaces.api.empresa_routes import router as empresa_router

app = FastAPI()
app.include_router(organizacion_router)
app.include_router(empresa_router)

@app.get("/")
def read_root():
    return {"mensaje": "Nomina en marcha"}
