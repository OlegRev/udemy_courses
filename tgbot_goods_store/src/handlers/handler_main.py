# импортируем класс HandlerCommands обработка комманд
from handlers.handler_com import HandlerCommands

# импортируем класс HandlerALLText обработка нажатия на кнопки и иные сообщения
from handlers.handler_all_text import HandlerALLText

# импортируем класс HandlerInlineQuery обработка нажатия на кнопки инлайн
from handlers.handler_inline_query import HandlerInlineQuery


class HandlerMain:
    """
    Класс компановщик
    """

    def __init__(self, bot):
        # получаем нашего бота
        self.bot = bot
        # здесь будет инициализация обработчика
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerALLText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self):
        # здесь будет запуск обработчиков
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()
