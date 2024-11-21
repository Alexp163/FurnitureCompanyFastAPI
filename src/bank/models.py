from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base

# fmt: off
class Bank(Base):  # счета предприятия для оплаты
    __tablename__ = "bank"

    id: Mapped[int] = mapped_column(primary_key=True)
    payment: Mapped[int] = mapped_column()
    wallet: Mapped[float | None] = mapped_column(server_default="0")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.payment} {self.wallet}"

#fmt: on
