from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from cleaning.models import Cleaning
from database import Base
from security.models import Security


# fmt: off
class Order(Base):  # заказ
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column()  # стоимость заказа
    date_order: Mapped[datetime] = mapped_column()  # дата заказа
    bank: Mapped["Bank"] = relationship("Bank")  # банковские счета предприятия
    bank_id: Mapped[int | None] = mapped_column(ForeignKey("bank.id"))
    customer: Mapped["Customer"] = relationship("Customer")  # заказчик(покупатель)
    customer_id: Mapped[int | None] = mapped_column(ForeignKey("customer.id"))
    engineer: Mapped["Engineer"] = relationship("Engineer")  # инженер-изготовитель заказа
    engineer_id: Mapped[int | None] = mapped_column(ForeignKey("engineer.id"))
    worker: Mapped["Worker"] = relationship("Worker")  # рабочий
    worker_id: Mapped[int | None] = mapped_column(ForeignKey("worker.id"))
    security: Mapped["Security"] = relationship("Security")  # безопасность сделки
    security_id: Mapped[int | None] = mapped_column(ForeignKey("security.id"))
    cleaning: Mapped["Cleaning"] = relationship("Cleaning")  # чистовая обработка и упаковка товара
    cleaning_id: Mapped[int | None] = mapped_column(ForeignKey("cleaning.id"))
    location: Mapped["Location"] = relationship("Location")  # филиал изготовитель
    location_id: Mapped[int | None] = mapped_column(ForeignKey("location.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return (f"{self.price} {self.date_order} {self.bank_id} {self.customer_id} {self.engineer_id} {self.worker_id}"
                f" {self.security_id} {self.location_id}")
# fmt: on

