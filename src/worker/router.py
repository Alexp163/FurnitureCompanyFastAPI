from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select, delete, update, func

from database import get_async_session

from .models import Worker
from .schemas import WorkerReadSchema, WorkerCreateSchema, WorkerUpdateSchema


router = APIRouter(tags=["workers"], prefix="/workers")


# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание нового рабочего
async def create_worker(worker: WorkerCreateSchema, session=Depends(get_async_session)) -> WorkerReadSchema:
    statement = insert(Worker).values(
        name=worker.name,
        age=worker.age,
        profession=worker.profession,
        experience=worker.experience,
        wallet=worker.wallet
    ).returning(Worker)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on


@router.get("/", status_code=status.HTTP_200_OK)  # 2) Получение данных о всех рабочих
async def get_workers(profession: str | None = None, session=Depends(get_async_session)) -> list[WorkerReadSchema]:
    statement = select(Worker)
    if profession is not None:
        statement = statement.where(Worker.profession == profession)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{worker_id}", status_code=status.HTTP_200_OK)  # 3) Получение данных о рабочем по id
async def get_worker_by_id(worker_id: int, session=Depends(get_async_session)) -> WorkerReadSchema:
    statement = select(Worker).where(Worker.id == worker_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{worker_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление рабочего по id
async def delete_worker_by_id(worker_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Worker).where(Worker.id == worker_id)
    await session.execute(statement)
    await session.commit()


# fmt: off
@router.put("/{worker_id}", status_code=status.HTTP_200_OK)  # 5) обновление данных о рабочем по id
async def update_worker_by_id(worker_id: int, worker: WorkerUpdateSchema,
                              session=Depends(get_async_session)) -> WorkerReadSchema:
    statement = update(Worker).where(Worker.id == worker_id).values(
        name=worker.name,
        age=worker.age,
        profession=worker.profession,
        experience=worker.experience,
        wallet=worker.wallet
    ).returning(Worker)
    result = await session.scalar(statement)
    await session.execute(statement)
    return result
# fmt: on
