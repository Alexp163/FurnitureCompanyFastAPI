from datetime import datetime

from fastapi import APIRouter, status, Depends
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .dependecies import Bank, Customer, Worker, Engineer, Security, Cleaning
from .models import Order
from .schemas import OrderCreateSchema, OrderReadSchema, OrderUpdateSchema
from .utils import increase_wallet


router = APIRouter(tags=["orders"], prefix="/orders")




# fmt: off
@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создать заказ
async def create_order(order: OrderCreateSchema, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = insert(Order).values(
        price=order.price,
        date_order=order.date_order,
        bank_id=order.bank_id,
        customer_id=order.customer_id,
        engineer_id=order.engineer_id,
        worker_id=order.worker_id,
        security_id=order.security_id,
        cleaning_id=order.cleaning_id,
        location_id=order.location_id
    ).returning(Order)
    result = await session.scalar(statement)
    await increase_wallet(Bank, order.price, session, 0.5, order.bank_id)  # перевод денег в банк организации
    await increase_wallet(Customer, order.price, session, 1, order.customer_id)  # снятие денег со счета заказчика
    await increase_wallet(Engineer, order.price, session, 0.2, order.engineer_id)  #  зачисление денег инженеру
    await increase_wallet(Worker, order.price, session, 0.1, order.worker_id)  #  зачисление денег рабочему
    await increase_wallet(Security, order.price, session, 0.1, order.security_id)  # зачисление денег охраннику
    await increase_wallet(Cleaning, order.price, session, 0.1, order.cleaning_id)  # зачисление денег клинингу
    await session.commit()
    return result
# fmt: on


# fmt: off
@router.get("/", status_code=status.HTTP_200_OK)  # 2) получение данных о всех заказах
async def get_orders(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    start_price: float | None = None,
    end_price: float | None = None,
    customer_id: int | None = None,
    engineer_id: int | None = None,
    location_id: int | None = None,
    session=Depends(get_async_session)) -> list[OrderReadSchema]:
    statement = select(Order)
    if start_date is not None:
        statement = statement.where(Order.created_at >= start_date)
    if end_date is not None:
        statement = statement.where(Order.created_at <= end_date)
    if start_price is not None:
        statement = statement.where(Order.price >= start_price)
    if end_price is not None:
        statement = statement.where(Order.price <= end_price)
    if customer_id is not None:
        statement = statement.where(Order.customer_id == customer_id)
    if engineer_id is not None:
        statement = statement.where(Order.engineer_id == engineer_id)
    if location_id is not None:
        statement = statement.where(Order.location_id == location_id)
    result = await session.scalars(statement)
    return list(result)
# fmt: on


@router.get("/{order_id)", status_code=status.HTTP_200_OK)  # 3) получение данных о заказе по id
async def get_order_by_id(order_id: int, session=Depends(get_async_session)) -> OrderReadSchema:
    statement = select(Order).where(Order.id == order_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление заказа по id
async def delete_order_by_id(order_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Order).where(Order.id == order_id)
    await session.execute(statement)
    await session.commit()


# fmt: off
@router.put("/{order_id}", status_code=status.HTTP_200_OK)  # 5) Обновление заказа по id
async def update_order_by_id(order_id: int, order: OrderUpdateSchema,
                             session=Depends(get_async_session)) -> OrderReadSchema:
    statement = update(Order).where(Order.id == order_id).values(
        price=order.price,
        date_order=order.date_order,
        bank_id=order.bank_id,
        customer_id=order.customer_id,
        engineer_id=order.engineer_id,
        worker_id=order.worker_id,
        security_id=order.security_id,
        cleaning_id=order.cleaning_id,
        location_id=order.location_id
    ).returning(Order)
    result = await session.scalar(statement)
    await session.commit()
    return result
# fmt: on
