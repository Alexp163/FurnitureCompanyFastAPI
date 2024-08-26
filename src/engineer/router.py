from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Engineer
from .schemas import EngineerCreateSchema, EngineerReadSchema, EngineerUpdateSchema

router = APIRouter(tags=["engineers"], prefix="/engineers")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание инженера
async def create_engineer(engineer: EngineerCreateSchema, session=Depends(get_async_session)) -> EngineerReadSchema:
    statement = insert(Engineer).values(
        name=engineer.name,
        special=engineer.special,
        experience=engineer.experience
    ).returning(Engineer)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получает данные о всех инженерах
async def get_engineer(session=Depends(get_async_session)) -> list[EngineerReadSchema]:  # "Depends" - зависит
    statement = select(Engineer)  # "statement" - заявление
    result = await session.scalars(statement) # "await" -ожидать
    return result


@router.get("/{engineer_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных об инженере по id
async def get_engineer_by_id(engineer_id: int, session=Depends(get_async_session)) -> EngineerReadSchema:
    statement = select(Engineer).where(Engineer.id == engineer_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{engineer_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление инженера из базы по id
async def delete_engineer_by_id(engineer_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Engineer).where(Engineer.id == engineer_id)  # "where" - где
    await session.execute(statement)  # "execute" - выполнять
    await session.commit()


@router.put("/{engineer_id}", status_code=status.HTTP_200_OK)  # 5 обновление инженера по id
async def update_engineer_by_id(engineer_id: int, engineer: EngineerUpdateSchema,
                                session=Depends(get_async_session)) -> EngineerReadSchema:
    statement = update(Engineer).where(Engineer.id == engineer_id).values(
        name=engineer.name,
        special=engineer.special,
        experience=engineer.experience
    ).returning(Engineer)
    result = await session.scalar(statement)
    await session.commit()
    return result






