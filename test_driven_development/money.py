from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    _currency: str

    def __init__(self, amount:int):
        # Protected Variable: 子クラスからもアクセスできる
        self._amount = amount
    
    def __eq__(self, money: Money) -> bool:
        return self._amount==money._amount and self.__class__==money.__class__
    
    @classmethod
    def currency(cls) -> str:
        return cls._currency
    
    @staticmethod
    def dollar(amount:int) -> Money:
        return Dollar(amount)
    
    @staticmethod
    def franc(amount: int) -> Money:
        return Franc(amount)
    
    @abstractmethod
    def times(self, multiplier:int) -> Money:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def currency(cls) -> str:
        raise NotImplementedError


class Dollar(Money):
    __currency = "USD"

    def __init__(self, amount:int):
        super().__init__(amount)
    
    def times(self, multiplier:int) -> Money:
        return self.__class__(self._amount * multiplier)
    
    @classmethod
    def currency(cls) -> str:
        return cls.__currency

class Franc(Money):
    __currency = "CHF"

    def __init__(self, amount:int):
        super().__init__(amount)
    
    def times(self, multiplier:int) -> Money:
        return self.__class__(self._amount * multiplier)
    
    @classmethod
    def currency(cls) -> str:
        return cls.__currency