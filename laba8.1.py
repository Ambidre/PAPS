from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originator():
    _state = None

    def __init__(self, state: int):
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self, name):
        print("Originator: I'm doing something important.")
        self._state = name
        print(f"Originator: and my state has changed to: {self._state}")

    def save(self):
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


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
        return f"{self._date} / ({self._state[0:9]}...)"

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
        # print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):

    def __init__(self, caretaker: Caretaker, originator: Originator, progress: int):
        self._caretaker = caretaker
        self._originator= originator
        self._progress = progress

    def execute(self):
        caretaker.backup()
        originator.do_something(self._progress)


class ComplexCommand(Command):

    def __init__(self, caretaker: Caretaker):
        self._caretaker = caretaker

    def execute(self):
        print("\nClient: Now, let's rollback!\n")
        caretaker.undo()


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):

        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    originator = Originator(100)
    caretaker = Caretaker(originator)

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand(caretaker, originator, 250))
    invoker.set_on_finish(ComplexCommand(caretaker))
    invoker.do_something_important()