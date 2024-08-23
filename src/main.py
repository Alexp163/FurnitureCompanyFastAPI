from fastapi import FastAPI

from admin.panel import register_admin
from building.router import router as building_router
from cleaning.router import router as cleaning_router
from customer.router import router as customer_router
from database import engine

app = FastAPI()
app.include_router(building_router)
app.include_router(cleaning_router)
app.include_router(customer_router)

register_admin(app, engine)
