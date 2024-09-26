from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth import router as auth_router
from api.health import router as health_router
from api.recycling import router as recycling_router
from api.recycling_point import router as recycling_point_router
from api.material import router as material_router
from core.config import settings

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs" if settings.DEV else None,
    redoc_url="/redoc" if settings.DEV else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://puretech.javm.tech", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(recycling_router, prefix="/recycling", tags=["recycling"])
app.include_router(recycling_point_router, prefix="/recycling_point", tags=["recycling_point"])
app.include_router(material_router, prefix="/material", tags=["material"])

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open(os.path.join("templates", "access_denied.html"), "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
