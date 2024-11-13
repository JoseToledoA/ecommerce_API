from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.routers.routes import router


# Inicializa la aplicación FastAPI
app = FastAPI(
    title="API Ecommerce",
    description=" ",
    version="0.0.1",
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)


# Agrega tus routers de FastAPI
app.include_router(router, prefix="/API")

# Montar la carpeta 'assets' para que las imágenes sean accesibles
# La ruta debe ser relativa al directorio donde se ejecuta el servidor
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")


# Inicia la aplicación
if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )  #!cambiar a puerto 7000 y volver a modificar las rutas de importaciones , sacar las app.
