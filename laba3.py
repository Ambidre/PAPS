# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod

class Mediator(ABC):
    def notify(self, sender: object, event: str):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: EnglishCourse, component2: SpanishCourse):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str):
        if event == "A":
            print("Медиатор реагирует на создание учебника по английскому и выполняет следующие операции:")
            self._component2.create_product_a()
        elif event == "D":
            print("Медиатор реагирует на создание видеокурса по испанскому и выполняет следующие операции:")
            self._component1.create_product_b()


class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class Course(ABC, BaseComponent):
    # Курсы
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class EnglishCourse(Course):
    # Курсы английского
    def create_product_a(self):
        print("Учебник по английскому")
        self.mediator.notify(self, "A")

    def create_product_b(self):
        print("Видеокурс по английскому")
        self.mediator.notify(self, "B")


class SpanishCourse(Course):
    # Курсы испанского
    def create_product_a(self):
        print("Учебник по испанскому")
        self.mediator.notify(self, "C")

    def create_product_b(self):
        print("Видеокурс по испанскому")
        self.mediator.notify(self, "D")


class EnglishCourseTextbook(BaseComponent):
    # Курсы английского учебник
    def useful_function_a(self):
        print("Учебник по английскому")


class EnglishCourseVideo(BaseComponent):
    # Курсы английского видео
    def useful_function_b(self):
        print("Видеокурс по английскому")


class SpanishCourseTextbook(BaseComponent):
    # Курсы испанского учебник
    def useful_function_a(self):
        print("Учебник по испанскому")


class SpanishCourseVideo(BaseComponent):
    # Курсы испанского видео
    def useful_function_b(self):
        print("Видеокурс по испанскому")


if __name__ == "__main__":
    # Клиентский код.
    c1 = EnglishCourse()
    c2 = SpanishCourse()
    mediator = ConcreteMediator(c1, c2)

    print("Создаем учебники")
    c1.create_product_a()

    print("\n", end="")

    print("Создаем видеокурсы")
    c2.create_product_b()