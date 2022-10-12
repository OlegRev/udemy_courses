"""Модуль, содержащий контроллеры веб-приложения"""
from typing import Literal
from olegrev_framework.templator import render


class Index:
    def __call__(self):
        return "200 OK", render("index.html")


class About:
    def __call__(self) -> tuple[Literal["200 OK"], Literal["about"]]:
        return "200 OK", "about"
