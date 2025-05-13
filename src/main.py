import uvicorn
from fastapi import FastAPI
from src.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.get("/")
def read_root():
    return {"message": f"{settings.APP_NAME} está corriendo 🎉"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host=settings.HOST, port=settings.PORT, reload=True)
