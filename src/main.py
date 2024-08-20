from fastapi import FastAPI

from admin.panel import register_admin
from building.router import router as building_router
from database import engine

app = FastAPI()
app.include_router(building_router)

register_admin(app, engine)
