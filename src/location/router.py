from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select, update

from database import get_async_session
from .dependencies import Order, OrderReadSchema
from .models import Location
from .schemas import LocationCreateSchema, LocationReadSchema, LocationUpdateSchema

router = APIRouter(tags=["locations"], prefix="/locations")


# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создает новую локацию
async def created_location(location: LocationCreateSchema, session=Depends(get_async_session)) -> LocationReadSchema:
    statement = insert(Location).values(
            name=location.name,
            city=location.city,
            distance=location,
    ).returning(Location)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Возвращает все локации
async def get_location(
    name: str | None = None, city: str | None = None, session=Depends(get_async_session)
) -> list[LocationReadSchema]:
    statement = select(Location)
    if name is not None:
        statement = statement.where(Location.name == name)
    if city is not None:
        statement = statement.where(Location.city == city)
    result = await session.scalars(statement)
    return result


@router.get("/{location_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Возвращает локацию по id
async def get_location_by_id(location_id: int, session=Depends(get_async_session)) -> LocationReadSchema:
    statement = select(Location).where(Location.id == location_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{location_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаляет локацию по id
async def delete_location_by_id(location_id: int, session=Depends(get_async_session)) -> None:
    statement = select(Location).where(Location.id == location_id)
    result = await session.scalar(statement)
    return result


@router.get("/{location_id}/orders", status_code=status.HTTP_200_OK)  # выводит список всех заказов из локации
async def get_location_orders(location_id: int, session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order).where(Order.location_id == location_id)
    result = await session.scalars(statement)
    return result


# fmt: off
@router.put("/{location_id}", status_code=status.HTTP_200_OK)  # 5) Обновляет данные о локации
async def update_location_by_id(location_id: int, location: LocationUpdateSchema,
                                session=Depends(get_async_session)) -> LocationReadSchema:
    statement = update(Location).where(Location.id == location_id).values(
        name=location.name,
        city=location.city,
        distance=location.distance
    ).returning(Location)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on
