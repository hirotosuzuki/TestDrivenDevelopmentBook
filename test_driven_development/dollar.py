from typing import Type


class Dollar:
    def __init__(self, amount:int):
        self.amount = amount
    
    def times(self, multiplier:int) -> Type['Dollar']:
        return Dollar(self.amount * multiplier)
    
    def equals(self, o:Type['Dollar']) -> bool:
        dollar = o
        return self.amount == dollar.amount