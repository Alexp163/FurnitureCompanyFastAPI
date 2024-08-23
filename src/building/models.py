from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Building(Base):  # здание
    __tablename__ = "building"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # название здания
    profile: Mapped[str] = mapped_column()  # профиль работы
    year: Mapped[str] = mapped_column()  # дата постройки
    floors: Mapped[str] = mapped_column()  # этажность
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.name} {self.profile} {self.year} {self.floors}"
