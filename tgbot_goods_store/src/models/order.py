# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, Integer, DateTime, ForeignKey

# импортируем модуль для связи таблиц
from sqlalchemy.orm import relationship, backref
from data_base.dbcore import Base

# импортируем модель продуктов для связи моделей
from models.product import Products


class Order(Base):
    """
    Класс для создания таблицы "Заказ",
    основан на декларативном стиле SQLAlchemy
    """

    # название таблицы
    __tablename__ = "orders"

    # поля таблицы
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer)

    # для каскадного удаления данных из таблицы
    products = relationship(
        Products, backref=backref("order", uselist=True, cascade="delete,all")
    )

    def __str__(self):
        return f"{self.quantity} {self.data}"
