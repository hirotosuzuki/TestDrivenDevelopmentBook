from test_driven_development import __version__
from test_driven_development.dollar import *


def test_version():
    assert __version__ == '0.1.0'


class TestMoney:
    def test_multiplication(self):
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)
    
    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Franc(5) == Franc(5)
        assert Franc(5) != Franc(6)
        assert Franc(5) != Money.dollar(5)
