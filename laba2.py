# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod


class Course(ABC):
    # Курсы
    @abstractmethod
    def create_beginner_course(self):
        pass

    @abstractmethod
    def create_advanced_course(self):
        pass


class EnglishCourse(Course):
    # Курсы английского
    def create_beginner_course(self):
        return EnglishCourseBeginner().create_product_a(), EnglishCourseBeginner().create_product_b()

    def create_advanced_course(self):
        return EnglishCourseAdvanced().create_product_a(), EnglishCourseAdvanced().create_product_b()


class SpanishCourse(Course):
    # Курсы испанского
    def create_beginner_course(self):
        return SpanishCourseBeginner().create_product_a(), SpanishCourseBeginner().create_product_b()

    def create_advanced_course(self):
        return SpanishCourseAdvanced().create_product_a(), SpanishCourseAdvanced().create_product_b()


class EnglishCourseBeginner(EnglishCourse):
    # Курсы нач английского
    def create_product_a(self):
        return EnglishCourseTextbookBeginner()

    def create_product_b(self):
        return EnglishCourseVideoBeginner()


class EnglishCourseAdvanced(EnglishCourse):
    # Курсы проф английского
    def create_product_a(self):
        return EnglishCourseTextbookAdvanced()

    def create_product_b(self):
        return EnglishCourseVideoAdvanced()


class SpanishCourseBeginner(SpanishCourse):
    # Курсы нач испанского
    def create_product_a(self):
        return SpanishCourseTextbookBeginner()

    def create_product_b(self):
        return SpanishCourseVideoBeginner()


class SpanishCourseAdvanced(SpanishCourse):
    # Курсы прод испанского
    def create_product_a(self):
        return SpanishCourseTextbookAdvanced()

    def create_product_b(self):
        return SpanishCourseVideoAdvanced()


class EnglishCourseTextbook(ABC):
    # Курсы английского учебник
    @abstractmethod
    def useful_function_a(self):
        pass


class EnglishCourseTextbookBeginner(EnglishCourseTextbook):
    # Курсы английского учебник для начинающих
    def useful_function_a(self):
        return "Учебник английского для начинающих"


class EnglishCourseTextbookAdvanced(EnglishCourseTextbook):
    # Курсы английского учебник для продолжающих
    def useful_function_a(self):
        return "Учебник английского для продолжающих"


class EnglishCourseVideo(ABC):
    # Курсы английского видео
    @abstractmethod
    def useful_function_b(self):
        pass


class EnglishCourseVideoBeginner(EnglishCourseVideo):
    # Курсы английского видео для начинающих
    def useful_function_b(self):
        return "Видеокурс по английскому для начинающих"


class EnglishCourseVideoAdvanced(EnglishCourseVideo):
    # Курсы английского видео для продолжающих
    def useful_function_b(self):
        return "Видеокурс по английскому для продолжающих"


class SpanishCourseTextbook(ABC):
    # Курсы испанского учебник
    @abstractmethod
    def useful_function_a(self):
        pass


class SpanishCourseTextbookBeginner(SpanishCourseTextbook):
    # Курсы испанского учебник для начинающих
    def useful_function_a(self):
        return "Учебник испанского для начинающих"


class SpanishCourseTextbookAdvanced(SpanishCourseTextbook):
    # Курсы испанского учебник для продолжающих
    def useful_function_a(self):
        return "Учебник испанского для продолжающих"


class SpanishCourseVideo(ABC):
    # Курсы испанского видео
    @abstractmethod
    def useful_function_b(self):
        pass


class SpanishCourseVideoBeginner(SpanishCourseVideo):
    # Курсы испанского видео для начинающих
    def useful_function_b(self):
        return "Видеокурс по испанскому для начинающих"


class SpanishCourseVideoAdvanced(SpanishCourseVideo):
    # Курсы испанского видео для продолжающих
    def useful_function_b(self):
        return "Видеокурс по испанскому для продолжающих"


def client_code(course: Course):
    product1, product2 = course.create_beginner_course()

    print(f"{product1.useful_function_a()}")
    print(f"{product2.useful_function_b()}")

    product3, product4 = course.create_advanced_course()
    print(f"{product3.useful_function_a()}")
    print(f"{product4.useful_function_b()}")


if __name__ == "__main__":
    print("App: Создаем курс по английскому")
    client_code(EnglishCourse())
    print("\n")

    print("App: Создаем курс по испанскому")
    client_code(SpanishCourse())
