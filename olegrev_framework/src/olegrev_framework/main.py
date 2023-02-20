from crypt import methods
from typing import Literal
from urllib import request
from framework_requests import GetRequests, PostRequests


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

        request = {}
        # Получаем все данные запроса
        method = environ["REQUEST_METHOD"]
        request["method"] = method

        if method == "POST":
            data = PostRequests().get_request_params(environ)
            request["data"] = data
            print(f"Нам пришёл post-запрос: {Framework.decode_value(data)}")
        if method == "GET":
            request_params = GetRequests().get_request_params(environ)
            request["request_params"] = request_params
            print(f"Нам пришли GET-параметры: {request_params}")

        # Находим нужный контролер
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # Запускаем контролер
        code, body = view()
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
