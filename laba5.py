# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class StateContext(ABC):
    _state = None

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def switchState(self):
        self._state.switchState()


    def pay(self):
        self._state.pay()

class State(ABC):
    @abstractmethod
    def switchState(self):
        pass

    @abstractmethod
    def pay(self):
        pass


class CreditCardState(State):
    def switchState(self):
        print("Пользователь меняет способ оплаты с CreditCard на PayPal")
        self.context.transition_to(PayPalState())

    def pay(self):
        strategy_context_credit_card = StrategyContext(PayByCreditCard())
        strategy_context_credit_card.do_some_business_logic(3500)


class PayPalState(State):
    def switchState(self):
        print("Пользователь меняет способ оплаты с PayPal на CreditCard ")
        self.context.transition_to(CreditCardState())

    def pay(self):
        strategy_context_paypal = StrategyContext(PayByPayPal())
        strategy_context_paypal.do_some_business_logic(3500)


class StrategyContext():
    def __init__(self, strategy: PayStrategy):
        self._strategy = strategy

    def do_some_business_logic(self,paymentAmount: int):
        result = self._strategy.pay(paymentAmount)


class PayStrategy(ABC):
    @abstractmethod
    def pay(self, data: int):
        pass


class PayByCreditCard(PayStrategy):
    def pay(self, data: int):
        print("Оплата {} через CreditCard.".format(data))


class PayByPayPal(PayStrategy):
    def pay(self, data: int):
        print("Оплата {} через PayPal.".format(data))


if __name__ == "__main__":
    state_context = StateContext(CreditCardState())
    state_context.pay()
    state_context.switchState()
    state_context.pay()