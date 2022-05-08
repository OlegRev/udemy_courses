# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# импортируем настройки и утилиты
from settings import config

# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    # инициализация разметки
    def __init__(self):
        self.markup = None
        # инициализация менеджера для работы с БД
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам.

        Parameters
        ----------
        name : str
            DESCRIPTION.
        step : int, optional
            шаг. The default is 0.
        quantity : int, optional
            количество. The default is 0.

        Returns
        -------
        KeyboardButton(config.KEYBOARD[name])

        """
        if name == "AMOUNT_ORDERS":
            config.KEYBOARD["AMOUNT_ORDERS"] = "{} {} {}".format(
                step + 1, "из", str(self.BD.count_rows_order())
            )
        if name == "AMOUNT_PRODUCT":
            config.KEYBOARD["AMOUNT_PRODUCT"] = "{}".format(quantity)

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку.

        Returns
        -------
        self.markup

        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("CHOOSE_GOODS")
        itm_btn_2 = self.set_btn("INFO")
        itm_btn_3 = self.set_btn("SETTINGS")
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        """
        Создает разметку кнопок в меню "О магазине".

        ReturnsDESCRIPTION
        -------
        self.markup

        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("<<")
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню "Настройки".

        Returns
        -------
        self.markup

        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("<<")
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def remove_menu(self):
        """
        Удаляет данные кнопки и возвращает ее.

        Returns
        -------
        ReplyKeyboardRemove()

        """
        return ReplyKeyboardMarkup()

    def category_menu(self):
        """
        Создает разметку кнопок в меню 'Категории товаров'.

        Returns
        -------
        self.markup

        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn("SEMIPRODUCT"))
        self.markup.add(self.set_btn("GROCERY"))
        self.markup.add(self.set_btn("ICE_CREAM"))
        self.markup.row(self.set_btn("<<"), self.set_btn("ORDER"))
        return self.markup

    def set_inline_btn(self, name):
        """
        Создает и возвращает инлайн кнопку по входным параметрам.

        Returns
        -------
        InlineKeyboardButton(str(name))
        """
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_select_category(self, category):
        """
        Создает разметку инлайн кнопок в выборанной категории товара.

        Returns
        -------
        Возвращает расметку.
            self.markup
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        # загружаем в название инлайн кнопок данные
        # с БД в соответствии с категорией товара
        for itm in self.BD.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(itm))

        return self.markup

    def orders_menu(self, step, quantity):
        """
        Создает разметку кнопок в заказе товара и возвращает разметку.

        Parameters
        ----------
        step : TYPE
            DESCRIPTION.
        quantity : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.markup = ReplyKeyboardMarkup(True, True)

        itm_btn_0 = self.set_btn("X", step, quantity)

        itm_btn_1 = self.set_btn("DOUWN", step, quantity)
        itm_btn_2 = self.set_btn("AMOUNT_PRODUCT", step, quantity)
        itm_btn_3 = self.set_btn("UP", step, quantity)

        itm_btn_4 = self.set_btn("BACK_STEP", step, quantity)
        itm_btn_5 = self.set_btn("AMOUNT_ORDERS", step, quantity)
        itm_btn_6 = self.set_btn("NEXT_STEP", step, quantity)

        itm_btn_7 = self.set_btn("<<", step, quantity)
        itm_btn_8 = self.set_btn("APPLAY", step, quantity)
        # расположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3)
        self.markup.row(itm_btn_4, itm_btn_5, itm_btn_6)
        self.markup.row(itm_btn_0, itm_btn_7, itm_btn_8)

        return self.markup
