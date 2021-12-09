# -*- coding: utf-8 -*-

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

# Фасад
class Course():
    def __init__(self, name:str):
        self._textbook = Textbook(name)
        self._video = Video(name)
        self._audio = Audio(name)

    def startCourse(self, name:str):
        self._textbook.create(name)
        self._video.create(name)
        self._audio.create(name)

# Клиентская часть
if __name__ == "__main__":
    facade = Course("English")
    facade.startCourse("English")