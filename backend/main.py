from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from observability.logger import init_db

app = FastAPI(title="SupplySentinel")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(router)

@app.get("/")
def health():
    return {"status": "SupplySentinel running"}
