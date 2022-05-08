import os
import tomli
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize


# токен выдается при регистрации бота
TOKEN = "ваш_токен_бота"
# название БД
NAME_DB = "products.db"
# родительская дериктория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join("sqlite:///" + BASE_DIR, NAME_DB)

with open(BASE_DIR+"/../../pyproject.toml", "rb") as f:
    pyproject_dict = tomli.load(f)['tool']['poetry']
# версия приложения
VERSION = pyproject_dict['version']
# автор приложения
AUTHOR = pyproject_dict['authors'][0]

COUNT = 0

# кнопки управления
KEYBOARD = {
    "CHOOSE_GOODS": emojize(":open_file_folder: Выбрать товар"),
    "INFO": emojize(":speech_balloon: О магазине"),
    "SETTINGS": emojize("⚙️ Настройки"),
    "SEMIPRODUCT": emojize(":pizza: Полуфабрикаты"),
    "GROCERY": emojize(":bread: Бакалея"),
    "ICE_CREAM": emojize(":shaved_ice: Мороженное"),
    "<<": emojize("⏪"),
    ">>": emojize("⏩"),
    "BACK_STEP": emojize("◀️"),
    "NEXT_STEP": emojize("▶️"),
    "ORDER": emojize("✅ ЗАКАЗ"),
    "X": emojize("❌"),
    "DOUWN": emojize("🔽"),
    "AMOUNT_PRODUCT": COUNT,
    "AMOUNT_ORDERS": COUNT,
    "UP": emojize("🔼"),
    "APPLAY": "✅ Оформить заказ",
    "COPY": "©️",
}

# id категорий продуктов
CATEGORY = {
    "SEMIPRODUCT": 1,
    "GROCERY": 2,
    "ICE_CREAM": 3,
}

# названия команд
COMMANDS = {
    "START": "start",
    "HELP": "help",
}
