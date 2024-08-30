# from fastapi import APIRouter, Depends, status
# from sqlalchemy import insert
#
# from database import get_async_session
#
# from .models import Security
# from .schemas import SecurityCreateSchema, SecurityReadSchema
#
# router = APIRouter(tags=["security"], prefix="/security")
#
#
# @router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание охранника
# async def create_security(security: SecurityCreateSchema, session=Depends(get_async_session)) -> SecurityReadSchema:
#     statement = (
#         insert(Security).values(name=security.name, age=security.age, weapon=security.weapon).returning(Security)
#     )
#     result = await session.scalar(statement)
#     await session.commit()
#     return result
#
#
# @router.get("/", status_code=status.HTTP_202_ACCEPTED)
# async def get_security():
#     pass
