# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey

# импортируем модуль для связи таблиц
from sqlalchemy.orm import relationship, backref
from data_base.dbcore import Base

# импортируем модель Категория для связи моделей
from models.category import Category


class Products(Base):
    """
    Класс для создания таблицы "Товары",
    основан на декларативном стиле SQLAlchemy
    """

    # название таблицы
    __tablename__ = "products"

    # поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey("category.id"))
    # для каскадного удаления данных из таблицы
    category = relationship(
        Category, backref=backref("products", uselist=True, cascade="delete, all")
    )

    def __str__(self):
        return f"{self.name} {self.title} {self.price}"
