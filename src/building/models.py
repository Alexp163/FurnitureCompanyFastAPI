from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Building(Base):  # здание
    __tablename__ = "building"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # название здания
    profile: Mapped[str] = mapped_column()  # профиль работы
    year: Mapped[str] = mapped_column()  # дата постройки
    floors: Mapped[str] = mapped_column()  # этажность
    cleaning = relationship("Cleaning")
    cleaning_id: Mapped[int | None] = mapped_column(ForeignKey("cleaning.id"))  # специалист клининга
    engineer = relationship("Engineer")
    engineer_id: Mapped[int| None] = mapped_column(ForeignKey("engineer.id"))  # инженер
    location = relationship("Location")
    location_id: Mapped[int | None] = mapped_column(ForeignKey("location.id"))  # город или населенный пункт
    security = relationship("Security")
    security_id: Mapped[int | None] = mapped_column(ForeignKey("security.id"))  # охрана здания
    worker = relationship("Worker")
    worker_id: Mapped[int | None] = mapped_column(ForeignKey("worker.id"))  # рабочий-специалист

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"{self.id} {self.name} {self.profile} {self.year} {self.floors} {self.cleaning.id}"
                f"{self.engineer.id} {self.location.id} {self.security.id} {self.worker.id}")

