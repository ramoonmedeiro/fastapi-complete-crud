from app.db.base import Base
from sqlalchemy import Column, Integer, String


class Category(Base):

    __tablename__ = "categories"

    id: int = Column("id", Integer, primary_key=True, autoincrement=True)
    name: str = Column("name", String, nullable=False)
    slug: str = Column("slug", String, nullable=False)