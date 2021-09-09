from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount:int):
        # Protected Variable: 子クラスからもアクセスできる
        self._amount = amount
    
    def __eq__(self, money: Money) -> bool:
        return self._amount==money._amount and self.__class__==money.__class__
    
    @staticmethod
    def dollar(amount:int) -> Money:
        return Dollar(amount)
    
    @staticmethod
    def franc(amount: int) -> Money:
        return Franc(amount)
    
    @abstractmethod
    def times(self, multiplier:int) -> Money:
        pass


class Dollar(Money):
    def __init__(self, amount:int):
        super().__init__(amount)
    
    def times(self, multiplier:int) -> Money:
        return self.__class__(self._amount * multiplier)

class Franc(Money):
    def __init__(self, amount:int):
        super().__init__(amount)
    
    def times(self, multiplier:int) -> Money:
        return self.__class__(self._amount * multiplier)