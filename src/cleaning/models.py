from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Cleaning(Base):  # Модель клининга
    __tablename__ = "cleaning"

    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped[str] = mapped_column()  # профиль уборщика(уборка полов, окон или химчистка)
    experience: Mapped[str] = mapped_column()  # опыт работы
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.profile} {self.experience}"
    