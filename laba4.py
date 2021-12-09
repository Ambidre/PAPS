# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


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
        return "Создан учебник английского для начинающих"


class EnglishCourseTextbookAdvanced(EnglishCourseTextbook):
    # Курсы английского учебник для продолжающих
    def useful_function_a(self):
        return "Создан учебник английского для продолжающих"


class EnglishCourseVideo(ABC):
    # Курсы английского видео
    @abstractmethod
    def useful_function_b(self):
        pass


class EnglishCourseVideoBeginner(EnglishCourseVideo):
    # Курсы английского видео для начинающих
    def useful_function_b(self):
        return "Создан видеокурс по английскому для начинающих"


class EnglishCourseVideoAdvanced(EnglishCourseVideo):
    # Курсы английского видео для продолжающих
    def useful_function_b(self):
        return "Создан видеокурс по английскому для продолжающих"


class SpanishCourseTextbook(ABC):
    # Курсы испанского учебник
    @abstractmethod
    def useful_function_a(self):
        pass


class SpanishCourseTextbookBeginner(SpanishCourseTextbook):
    # Курсы испанского учебник для начинающих
    def useful_function_a(self):
        return "Создан учебник испанского для начинающих"


class SpanishCourseTextbookAdvanced(SpanishCourseTextbook):
    # Курсы испанского учебник для продолжающих
    def useful_function_a(self):
        return "Создан учебник испанского для продолжающих"


class SpanishCourseVideo(ABC):
    # Курсы испанского видео
    @abstractmethod
    def useful_function_b(self):
        pass


class SpanishCourseVideoBeginner(SpanishCourseVideo):
    # Курсы испанского видео для начинающих
    def useful_function_b(self):
        return "Создан видеокурс по испанскому для начинающих"


class SpanishCourseVideoAdvanced(SpanishCourseVideo):
    # Курсы испанского видео для продолжающих
    def useful_function_b(self):
        return "Создан видеокурс по испанскому для продолжающих"


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class EnglishBeginnerHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == "English beginner course":
            return create_beginner(EnglishCourse())
        else:
            return super().handle(request)


class SpanishBeginnerHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == "Spanish beginner course":
            return create_beginner(SpanishCourse())
        else:
            return super().handle(request)


class EnglishAdvancedHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == "English advanced course":
            return create_advanced(EnglishCourse())
        else:
            return super().handle(request)


class SpanishAdvancedHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == "Spanish advanced course":
            return create_advanced(SpanishCourse())
        else:
            return super().handle(request)


def create_beginner(course: Course):
    product1, product2 = course.create_beginner_course()

    print(f"{product1.useful_function_a()}")
    print(f"{product2.useful_function_b()}")


def create_advanced(course: Course):
    product1, product2 = course.create_advanced_course()

    print(f"{product1.useful_function_a()}")
    print(f"{product2.useful_function_b()}")


def client_code(handler: Handler):
    for course in ["English beginner course", "Spanish beginner course", "English advanced course",
                   "hgd"]:
        print(f"\nClient: Надо создать {course}?")
        result = handler.handle(course)
        if result:
            print(f"  {result}", end="")
        # else:
        #     print(f"  {course} не создан.", end="")


if __name__ == "__main__":
    english_beginner = EnglishBeginnerHandler()
    spanish_beginner = SpanishBeginnerHandler()
    english_advanced = EnglishAdvancedHandler()
    spanish_advanced = SpanishAdvancedHandler()

    english_beginner.set_next(spanish_beginner).set_next(english_advanced).set_next(spanish_advanced)

    client_code(english_beginner)
    print("\n")

    client_code(spanish_beginner)
