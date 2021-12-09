# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Any, Optional


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class AuthorisationCommand(Command):

    def __init__(self, receiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        print("AuthorisationCommand: The receiver will reply", end="")
        return self._receiver.do_something()


class CorrectOrderCommand(Command):

    def __init__(self, receiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        print("CorrectOrderCommand: The receiver will reply", end="")
        return self._receiver.do_something()


class PremiumCommand(Command):

    def __init__(self, receiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        print("PremiumCommand: The receiver will reply", end="")
        return self._receiver.do_something()


class AuthorisationReceiver:

    def do_something(self) -> None:
        return f"AuthorisationReceiver: Пользователь не авторизован"


class CorrectOrderReceiver:

    def do_something(self) -> None:
        return f"CorrectOrderReceiver: Пользователь неправильно заполнил поля при покупки курса"


class PremiumReceiver:

    def do_something(self) -> None:
        return f"PremiumReceiver: Пользователь не имеет премиум"


class Invoker:
    string = ''
    _authorisation = None
    _correct_order = None
    _premium = None

    def set_authorisation(self, command: Command):
        self._authorisation = command

    def set_correct_order(self, command: Command):
        self._correct_order = command

    def set_premium(self, command: Command):
        self._premium = command

    def do_command(self, string) -> None:

        if (string == 'autorisation'):
            return self._authorisation.execute()

        if (string == 'correct_order'):
            return self._correct_order.execute()

        if (string == 'premium'):
            return self._premium.execute()


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def use_command(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    invoker: Invoker
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def use_command(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.use_command(request)
        return None


class AuthorisationHandler(AbstractHandler):
    def use_command(self, request: Any) -> str:
        if request[0] == 0:
            invoker.string = 'authorisation'
            return invoker.do_command(invoker.string)
        else:
            return super().use_command(request)


class CorrectOrderHandler(AbstractHandler):
    def use_command(self, request: Any) -> str:
        if request[1] == 0:
            invoker.string = 'correct_order'
            return invoker.do_command(invoker.string)
        else:
            return super().use_command(request)


class PremiumHandler(AbstractHandler):
    def use_command(self, request: Any) -> str:
        if request[2] == 0:
            invoker.string = 'premium'
            return invoker.do_command(invoker.string)
        else:
            return super().use_command(request)


if __name__ == "__main__":

    auth_receiver = AuthorisationReceiver()
    correct_receiver = CorrectOrderReceiver()
    premium_receiver = PremiumReceiver()

    invoker = Invoker()
    invoker.set_authorisation(AuthorisationCommand(auth_receiver))
    invoker.set_correct_order(CorrectOrderCommand(correct_receiver))
    invoker.set_premium(PremiumCommand(premium_receiver))

    authorisation = AuthorisationHandler()
    correct_order = CorrectOrderHandler()
    premium = PremiumHandler()

    authorisation.invoker = invoker
    correct_order.invoker = invoker
    premium.invoker = invoker

    authorisation.set_next(correct_order).set_next(premium)

    print("Chain: authorisation > correct_order > premium")

    print("Первый запрос")
    user = [1, 1, 1]
    result = authorisation.use_command(user)
    if result:
        print(f"  {result}\n", end="")
    else:
        print("Заказ успешно сформирован\n")

    print("Второй запрос")
    user = [1, 0, 1]
    result = authorisation.use_command(user)
    if result:
        print(f"  {result}\n", end="")
    else:
        print("Заказ успешно сформирован\n")

    print("Третий запрос")
    user = [1, 1, 0]
    result = authorisation.use_command(user)
    if result:
        print(f"\n{result}\n", end="")
    else:
        print("Заказ успешно сформирован")


