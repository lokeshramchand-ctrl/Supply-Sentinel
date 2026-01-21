from fastapi import FastAPI
from api.routes import router
from observability.logger import init_db

app = FastAPI(title="SupplySentinel")

init_db()

app.include_router(router)

@app.get("/")
def health():
    return {"status": "SupplySentinel running"}
