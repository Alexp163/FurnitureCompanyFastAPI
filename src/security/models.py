from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Security(Base):
    __tablename__ = "security"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    age: Mapped[str] = mapped_column()
    weapon: Mapped[str] = mapped_column()
    wallet: Mapped[float | None] = mapped_column("0")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),  # "update" при обновлении
    )

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.age}, {self.weapon} {self.wallet}"
