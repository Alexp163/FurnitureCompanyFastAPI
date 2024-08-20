from sqladmin import ModelView, Admin
from .dependencies import Building
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine


class BuildingModelView(ModelView, model=Building):
    column_list = [Building.name, Building.profile, Building.year, Building.floors]
    form_excluded_columns = [Building.created_at, Building.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(BuildingModelView)

