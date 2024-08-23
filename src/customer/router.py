from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import Customer
from .schemas import CustomerCreateSchema, CustomerReadSchema, CustomerUpdateSchema

router =APIRouter(tags=["customers"], prefix="/customers")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание покупателя
async def create_customer(customer: CustomerCreateSchema, session=Depends(get_async_session)) -> CustomerReadSchema:
    statement = insert(Customer).values(
        name=customer.name,
        age=customer.age,
        rating=customer.rating
    ).returning(Customer)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получает данные о всех клиентах
async def get_customers(session=Depends(get_async_session)) -> list[CustomerReadSchema]:
    statement = select(Customer)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{customer_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получает данные о клиенте по id
async def get_customer_by_id(customer_id: int, session=Depends(get_async_session)) -> CustomerReadSchema:
    statement = select(Customer).where(Customer.id == customer_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление клиента по id
async def delete_customer_by_id(customer_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Customer).where(Customer.id == customer_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{customer_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных о покупателе по id
async def update_customer_by_id(customer_id: int, customer: CustomerUpdateSchema,
                                session=Depends(get_async_session)) -> CustomerReadSchema:
    statement = update(Customer).where(Customer.id == customer_id).values(
        name=customer.name,
        age=customer.age,
        rating=customer.rating
    ).returning(Customer)
    result = await session.scalar(statement)
    await session.commit()
    return result

