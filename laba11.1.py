# coding: utf-8
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class Originator():

    def __init__(self, creator: Creator):
        self._creator = creator
        print(f"Изначальный курс: {self._creator}")

    def do_something(self, name):
        print("Курс обновляется")
        self._creator = name
        print(f"Сейчас у нас добавлены {self._creator}")

    def save(self):
        return ConcreteMemento(self._creator)

    def restore(self, memento: Memento):
        self._creator = memento.get_creator()
        print(f"Курс поменялся {self._creator}")


class Memento(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_name(self):
        return f"({self._state[0:9]}...)"

    def get_date(self):
        return self._date


class Caretaker():
    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Восстанавливаем предыдущий курс {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


class Course:
    textbook = ""
    video = ""
    audio = ""



class Creator:
    def create(self):
        self.course = Course()


class EnglishCourse(Creator):
    def create_textbook(self):
        # print("Adding English textbook")
        self.course.textbook = "English textbook"
        return "English textbook"

    def create_video(self):
        # print("Adding English video")
        self.course.video = "English video"
        return "English video"

    def create_audio(self):
        # print("Adding English au/dio")
        self.course.audio = "English audio"
        return "English audio"


class SpanishCourse(Creator):
    def create_textbook(self):
        # print("Adding Spanish textbook")
        self.course.textbook = "Spanish textbook"
        return "Spanish textbook"

    def create_video(self):
        # print("Adding Spanish video")
        self.course.video = "Spanish video"
        return "Spanish video"

    def create_audio(self):
        # print("Adding Spanish audio")
        self.course.audio = "Spanish audio"
        return "Spanish audio"


class Admin:
    __creator = ''

    def set_course(self, creator):
        self.__creator = creator

    def create_a_course(self):
        self.__creator.create()
        self.__creator.create_textbook()
        self.__creator.create_video()
        self.__creator.create_audio()
        return

    def get_course(self):
        return self.__creator.course

    def get_info(self):
        return self.__creator.create_textbook(), self.__creator.create_video(), self.__creator.create_audio()


english = EnglishCourse()
spanish = SpanishCourse()
admin = Admin()
admin.set_course(english)
admin.create_a_course()
course = admin.get_info()

originator = Originator(course)
caretaker = Caretaker(originator)

admin.set_course(spanish)
admin.create_a_course()
course = admin.get_info()

caretaker.backup()
originator.do_something(course)

caretaker.undo()
