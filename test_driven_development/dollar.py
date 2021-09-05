from typing import Type


class Money:
    def __init__(self, amount:int):
        # Protected Variable: 子クラスからもアクセスできる
        self._amount = amount
    
    def __eq__(self, money: Type['Money']) -> bool:
        return self._amount==money._amount and self.__class__==money.__class__

class Dollar(Money):
    def __init__(self, amount:int):
        super().__init__(amount)
    
    def times(self, multiplier:int) -> Type['Dollar']:
        return Dollar(self._amount * multiplier)

class Franc(Money):
    def __init__(self, amount:int):
        super().__init__(amount)
    
    def times(self, multiplier:int) -> Type['Franc']:
        return Franc(self._amount * multiplier)