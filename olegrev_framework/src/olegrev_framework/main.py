from typing import Literal


class PageNotFound404:
    def __call__(self) -> tuple[Literal["404 WHAT"], Literal["404 PAGE Not Found"]]:
        return "404 WHAT", "404 PAGE Not Found"


class Framework:
    """Класс Framework - основа WSGI-фреймворка"""

    def __init__(self, routes_obj) -> None:
        self.routes_lst = routes_obj

    def __call__(self, environ, start_response):
        # Получение адреса, по которому пользовательвыполнил переход
        path = environ["PATH_INFO"]

        # Добавляем закрывающий слэш
        if not path.endswith("/"):
            path = f"{path}/"

        # Находим нужный контролер
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # Запускаем контролер
        code, body = view()
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
