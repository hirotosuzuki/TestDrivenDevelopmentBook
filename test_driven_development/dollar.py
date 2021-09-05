from typing import Type


class Dollar:
    def __init__(self, amount:int):
        self.__amount = amount
    
    def times(self, multiplier:int) -> Type['Dollar']:
        return Dollar(self.__amount * multiplier)
    
    def __eq__(self, o: Type['Dollar']) -> bool:
        dollar = o
        return self.__amount == dollar.__amount 