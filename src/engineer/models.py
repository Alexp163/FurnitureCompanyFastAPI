from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Engineer(Base):  # модель инженера
    __tablename__ = "engineer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    special: Mapped[str] = mapped_column()
    experience: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )  # "update"-при обновлении

    def __repr__(self):
        return f"{self.name} {self.scpecial} {self.experience}"
