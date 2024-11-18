from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select, delete, update

from database import get_async_session

from .models import Security
from .schemas import SecurityCreateSchema, SecurityReadSchema, SecurityUpdateSchema

router = APIRouter(tags=["security"], prefix="/security")


# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание охранника
async def create_security(security: SecurityCreateSchema, session=Depends(get_async_session)) -> SecurityReadSchema:
    statement = insert(Security).values(
        name=security.name,
        age=security.age,
        weapon=security.weapon,
        wallet=security.wallet
    ).returning(Security)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on


@router.get("/", status_code=status.HTTP_200_OK)  # 2) получает данные о всех охранниках
async def get_security(session=Depends(get_async_session)) -> list[SecurityReadSchema]:
    statement = select(Security)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{security_id}", status_code=status.HTTP_200_OK)  # 3) Получает данные об охраннике по id
async def get_security_by_id(security_id: int, session=Depends(get_async_session)) -> SecurityReadSchema:
    statement = select(Security).where(Security.id == security_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{security_id}", status_code=status.HTTP_200_OK)  # 4) Удаляет данные об охраннике по id
async def delete_security_by_id(security_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Security).where(Security.id == security_id)
    await session.execute(statement)
    await session.commit()


# fmt: off
@router.put("/{security_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных по id
async def update_security_by_id(security_id: int, security: SecurityUpdateSchema,
                                session=Depends(get_async_session)) -> SecurityReadSchema:
    statement = update(Security).where(Security.id == security_id).values(
        name=security.name,
        age=security.age,
        weapon=security.weapon,
        wallet=security.wallet
    ).returning(Security)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on
