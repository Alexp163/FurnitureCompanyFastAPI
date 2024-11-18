from fastapi import APIRouter, Depends, status
from sqlalchemy import delete, insert, select, update

from database import get_async_session

from .models import Cleaning
from .schemas import CleaningCreateSchema, CleaningReadSchema, CleaningUpdateSchema

router = APIRouter(tags=["cleaning"], prefix="/cleaning")


# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание клининга
async def create_cleaning(cleaning: CleaningCreateSchema, session=Depends(get_async_session)) -> CleaningReadSchema:
    statement = insert(Cleaning).values(  # "statement" - заявление
        profile=cleaning.profile,
        experience=cleaning.experience,
        wallet=cleaning.wallet
    ).returning(Cleaning)
    result = await session.scalar(statement)  # "await" - ожидать
    await session.commit()
    return result
# fmt: on


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получение данных о всех клинингах
async def get_cleanings(session=Depends(get_async_session)) -> list[CleaningReadSchema]:
    statement = select(Cleaning)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{cleaning_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о клиниге по id
async def get_cleaning_by_id(cleaning_id: int, session=Depends(get_async_session)) -> CleaningReadSchema:
    statement = select(Cleaning).where(Cleaning.id == cleaning_id)  # "where" - где
    result = await session.scalar(statement)
    return result


@router.delete("/{cleaning_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление клининга по id
async def delete_cleaning_by_id(cleaning_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Cleaning).where(Cleaning.id == cleaning_id)
    await session.execute(statement)
    await session.commit()


# fmt: off
@router.put("/{cleaning_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных клининга по id
async def update_cleaning_by_id(cleaning_id: int, cleaning: CleaningUpdateSchema, session=Depends(get_async_session)) -> CleaningReadSchema:
    statement = update(Cleaning).where(Cleaning.id == cleaning_id).values(
        profile=cleaning.profile,
        experience=cleaning.experience,
        wallet=cleaning.wallet
    ).returning(Cleaning)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on
