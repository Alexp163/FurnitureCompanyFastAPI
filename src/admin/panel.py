from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine

from .dependencies import Building, Cleaning, Customer, Engineer, Location


class BuildingModelView(ModelView, model=Building):
    column_list = [Building.name, Building.profile, Building.year, Building.floors]
    form_excluded_columns = [Building.created_at, Building.updated_at]


class CleaningModelView(ModelView, model=Cleaning):
    column_list = [Cleaning.profile, Cleaning.experience]
    form_excluded_columns = [Cleaning.created_at, Cleaning.updated_at]


class CustomerModelView(ModelView, model=Customer):
    column_list = [Customer.name, Customer.age, Customer.rating]
    form_excluded_columns = [Customer.created_at, Customer.updated_at]


class EngineerModelView(ModelView, model=Engineer):
    column_list = [Engineer.name, Engineer.special, Engineer.experience]
    form_excluded_columns = [Engineer.created_at, Engineer.updated_at]


class LocationModelView(ModelView, model=Location):
    column_list = [Location.name, Location.city, Location.distance]
    form_excluded_columns = [Location.created_at, Location.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(BuildingModelView)
    admin.add_view(CleaningModelView)
    admin.add_view(CustomerModelView)
    admin.add_view(EngineerModelView)
    admin.add_view(LocationModelView)
