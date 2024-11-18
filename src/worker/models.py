from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Worker(Base):  # рабочий
    __tablename__ = "worker"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # ФИО
    age: Mapped[str] = mapped_column()  # возраст
    profession: Mapped[str] = mapped_column()  # профессия
    experience: Mapped[str] = mapped_column()  # опыт работы
    wallet: Mapped[float | None] = mapped_column("0")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.name} {self.age} {self.profession} {self.experience} {self.wallet}"
