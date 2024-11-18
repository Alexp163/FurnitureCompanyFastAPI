from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Location(Base):  # модель локации(города) предприятия
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # название филиала
    city: Mapped[str] = mapped_column()  # город локации филиала
    distance: Mapped[str] = mapped_column()  # расстояние до главного офиса в Москве
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.name} {self.city} {self.distance}"
