from fastapi import APIRouter, Depends, status
from sqlalchemy import delete, insert, select, update

from database import get_async_session

from .models import Building
from .schemas import BuildingCreateSchema, BuildingReadSchema, BuildingUpdateSchema

router = APIRouter(tags=["buildings"], prefix="/buildings")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание здания
async def create_building(building: BuildingCreateSchema, session=Depends(get_async_session)) -> BuildingReadSchema:
    statement = (
        insert(Building)
        .values(  # "statement" - заявление
            name=building.name, profile=building.profile, year=building.year, floors=building.floors
        )
        .returning(Building)
    )
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получение данных о всех постройках
async def get_buildings(session=Depends(get_async_session)) -> list[BuildingReadSchema]:
    statement = select(Building)
    result = await session.scalar(statement)
    return list(result)


@router.get("/{building_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о здании по id
async def get_building_by_id(building_id: int, session=Depends(get_async_session)) -> BuildingReadSchema:
    statement = select(Building).where(Building.id == building_id)  # "where" - где
    result = await session.scalar(statement)  # "await" - ожидать
    return result


@router.delete("/{building_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление постройки по id
async def delete_building_by_id(building_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Building).where(Building.id == building_id)  # "statement" - заявление
    await session.execute(statement)
    await session.commit()


@router.put("/{building_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_building_by_id(
    building_id: int, building: BuildingUpdateSchema, session=Depends(get_async_session)
) -> BuildingReadSchema:
    statement = (
        update(Building)
        .where(Building.id == building_id)
        .values(name=building.name, profile=building.profile, year=building.year, floors=building.floors)
        .returning(Building)
    )
    result = await session.scalar(statement)
    await session.commit()
    return result
