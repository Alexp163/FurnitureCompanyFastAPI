from fastapi import APIRouter, Depends, status
from sqlalchemy import delete, insert, select, update
from database import get_async_session
from .schemas import BankCreateSchema, BankReadSchema, BankUpdateSchema
from .models import Bank


router = APIRouter(tags=["banks"], prefix="/banks")

@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание банковского счета
async def create_bank(bank: BankCreateSchema, session=Depends(get_async_session))-> BankReadSchema:
    statement = insert(Bank).values(
        payment=bank.payment,
        wallet=bank.wallet
    ).returning(Bank)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_200_OK)  # 2) получить данные о всех счетах
async def get_bank(session=Depends(get_async_session)) -> list[BankReadSchema]:
    statement = select(Bank)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{bank_id}", status_code=status.HTTP_200_OK)  # 3) получение данных о счете по id
async def get_bank_by_id(bank_id: int, session=Depends(get_async_session)) -> BankReadSchema:
    statement = select(Bank).where(Bank.id == bank_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{bank_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление счета по id
async def delete_bank_by_id(bank_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Bank).where(Bank.id == bank_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{bank_id}", status_code=status.HTTP_200_OK)  # 5) обновление счета по id
async def update_bank_by_id(bank_id: int, bank: BankUpdateSchema, session=Depends(get_async_session)) -> BankReadSchema:
    statement = update(Bank).where(Bank.id == bank_id).values(
        payment=bank.payment,
        wallet=bank.wallet
    ).returning(Bank)
    result = await session.scalar(statement)
    await session.commit()
    return result


