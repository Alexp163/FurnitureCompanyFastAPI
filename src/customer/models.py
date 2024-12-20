from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Customer(Base):  # покупатель
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    age: Mapped[str] = mapped_column()
    rating: Mapped[str] = mapped_column()
    wallet: Mapped[float | None] = mapped_column(server_default="0")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.name} {self.age} {self.rating} {self.wallet}"
