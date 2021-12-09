# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    def notify(self, sender: object, event: str):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Course, component2: Course):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str):
        if event == "English for Beginners":
            print("Медиатор реагирует на создание учебника по английскому и выполняет следующие операции:")
            self._component2.startCourse("English for intermediate")
        elif event == "English for intermediate":
            print("Медиатор реагирует на создание видеокурса по испанскому и выполняет следующие операции:")
            self._component1.startCourse(event)


class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


# Сложные части системы


class Textbook():
    def __init__(self, name: str):
        self._name = name

    def create(self, name):
        print(f"Create {self._name} textbook")


class Video():
    def __init__(self, name: str):
        self._name = name

    def create(self, name):
        print(f"Create {self._name} video")


class Audio():
    def __init__(self, name: str):
        self._name = name

    def create(self, name):
        print(f"Create {self._name} audio")


class Subtitles():
    def __init__(self, name: str):
        self._name = name

    def create(self, name):
        print(f"Create {self._name} subtitles")


# Фасад
class Course(BaseComponent):
    def __init__(self, name: str):
        self._textbook = Textbook(name)
        self._video = Video(name)
        self._audio = Audio(name)
        self._subtitles = Subtitles(name)

    def startCourse(self, name: str):
        self._textbook.create(name)
        self._video.create(name)
        self._audio.create(name)
        self.mediator.notify(self, "A")

    def startOnlineCourse(self, name: str):
        self._video.create(name)
        self._subtitles.create(name)
        self._audio.create(name)
        self.mediator.notify(self, "D")


class Mediator(ABC):
    def notify(self, sender: object, event: str):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Course, component2: Course):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str):
        if event == "A":
            print("Медиатор реагирует на создание курса для начинающих и создает курс для продолжающих:")
            self._component2.startOnlineCourse("D")
        elif event == "C":
            print("Медиатор реагирует на создание курса для продолжающих и создает курс для начинающих:")
            self._component1.startCourse("A")


class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


# Клиентская часть
if __name__ == "__main__":
    facade1 = Course("English for Beginners")
    facade2 = Course("English for Intermediate")

    mediator = ConcreteMediator(facade1, facade2)

    print("Создаем учебники для начинающих")
    facade1.startCourse("English for Beginners")

    print("\n", end="")
