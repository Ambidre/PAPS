# coding: utf-8
class Course:
    """
    Абстрактный курс
    """
    textbook = ""
    video = ""
    audio = ""


class Creator:
    """
    Ответственный за создание
    """

    def create(self):
        self.course = Course()


class EnglishCourse(Creator):
    """
    Курс английского
    """

    def create_textbook(self):
        print("Adding English textbook")
        self.course.textbook = "English textbook"

    def create_video(self):
        print("Adding English video")
        self.course.video = "English video"

    def create_audio(self):
        print("Adding English audio")
        self.course.audio = "English audio"


class SpanishCourse(Creator):
    """
    Курс испанского
    """

    def create_textbook(self):
        print("Adding Spanish textbook")
        self.course.textbook = "Spanish textbook"

    def create_video(self):
        print("Adding Spanish video")
        self.course.video = "Spanish video"

    def create_audio(self):
        print("Adding Spanish audio")
        self.course.audio = "Spanish audio"


class Admin:
    """
    Админ
    """
    __creator = ''

    def set_course(self, creator):
        self.__creator = creator

    def create_a_course(self):
        self.__creator.create()
        self.__creator.create_textbook()
        self.__creator.create_video()
        self.__creator.create_audio()

    def get_course(self):
        return self.__creator.course


english = EnglishCourse()
spanish = SpanishCourse()
admin = Admin()
admin.set_course(english)
admin.create_a_course()
course = admin.get_course()

admin.set_course(spanish)
admin.create_a_course()
course = admin.get_course()
