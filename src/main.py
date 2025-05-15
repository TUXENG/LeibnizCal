from fastapi import FastAPI
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import settings
from src.defined.router import router as defined_router
from src.undefined.router import router as undefined_router
from src.history.router import router as history_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

BASE_DIR = Path(__file__).resolve().parent.parent  # apunta a la carpeta raíz LeibnizCal

# Apuntar templates a la carpeta raíz/templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# Montar carpeta static que queda en la raíz
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)



# Incluir routers
app.include_router(defined_router)    # monta en /defined
app.include_router(undefined_router)  # monta en /undefined
app.include_router(history_router)  # monta en /history

@app.get("/")
async def root():
    return {"message": f"{settings.app_name} está corriendo 🎉"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )
