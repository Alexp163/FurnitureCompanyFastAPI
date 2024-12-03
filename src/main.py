from fastapi import FastAPI

from admin.panel import register_admin
from building.router import router as building_router
from cleaning.router import router as cleaning_router
from customer.router import router as customer_router
from database import engine
from engineer.router import router as engineer_router
from location.router import router as location_router
from user.router import router as user_router
from worker.router import router as worker_router
from order.router import router as order_router
from security.router import router as security_router
from bank.router import router as bank_router


app = FastAPI()
app.include_router(building_router)
app.include_router(cleaning_router)
app.include_router(customer_router)
app.include_router(engineer_router)
app.include_router(location_router)
app.include_router(user_router)
app.include_router(worker_router)
app.include_router(order_router)
app.include_router(security_router)
app.include_router(bank_router)

register_admin(app, engine)

