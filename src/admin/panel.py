from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine

from .dependencies import Building, Cleaning, Customer, Engineer, Location, User, Worker, Order, Security, Bank

# fmt: off
class BuildingModelView(ModelView, model=Building):
    column_list = [Building.name, Building.profile, Building.year, Building.floors, Building.cleaning_id,
        Building.engineer_id, Building.location_id, Building.security_id,]
    form_excluded_columns = [Building.created_at, Building.updated_at]


class CleaningModelView(ModelView, model=Cleaning):
    column_list = [Cleaning.profile, Cleaning.experience, Cleaning.wallet]
    form_excluded_columns = [Cleaning.created_at, Cleaning.updated_at]


class CustomerModelView(ModelView, model=Customer):
    column_list = [Customer.name, Customer.age, Customer.rating, Customer.wallet]
    form_excluded_columns = [Customer.created_at, Customer.updated_at]


class EngineerModelView(ModelView, model=Engineer):
    column_list = [Engineer.name, Engineer.special, Engineer.experience, Engineer.wallet]
    form_excluded_columns = [Engineer.created_at, Engineer.updated_at]


class LocationModelView(ModelView, model=Location):
    column_list = [Location.name, Location.city, Location.distance]
    form_excluded_columns = [Location.created_at, Location.updated_at]


class UserModelView(ModelView, model=User):
    column_list = [User.name, User.age, User.email]
    form_excluded_columns = [User.created_at, User.updated_at]


class WorkerModelView(ModelView, model=Worker):
    column_list = [Worker.name, Worker.age, Worker.profession, Worker.experience, Worker.wallet]
    from_excluded_columns = [Worker.created_at, Worker.updated_at]


class OrderModelView(ModelView, model=Order):
    column_list = [Order.price, Order.date_order, Order.bank_id, Order.customer_id, Order.engineer_id, Order.worker_id,
                   Order.security_id, Order.cleaning_id, Order.location_id]
    form_excluded_columns = [Order.created_at, Order.updated_at]


class SecurityModelView(ModelView, model=Security):
    column_list = [Security.name, Security.age, Security.weapon, Security.wallet]
    form_excluded_columns = [Security.created_at, Security.updated_at]


class BankModelView(ModelView, model=Bank):
    column_list = [Bank.payment, Bank.wallet]
    form_excluded_columns = [Bank.created_at, Bank.updated_at]

def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(BuildingModelView)
    admin.add_view(CleaningModelView)
    admin.add_view(CustomerModelView)
    admin.add_view(EngineerModelView)
    admin.add_view(LocationModelView)
    admin.add_view(UserModelView)
    admin.add_view(WorkerModelView)
    admin.add_view(OrderModelView)
    admin.add_view(SecurityModelView)
    admin.add_view(BankModelView)

# fmt: on