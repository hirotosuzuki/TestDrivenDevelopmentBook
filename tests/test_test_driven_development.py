from test_driven_development import __version__
from test_driven_development.dollar import Dollar, Franc


def test_version():
    assert __version__ == '0.1.0'


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)
    
    def test_equality(self):
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
        assert Franc(5) == Franc(5)
        assert Franc(5) != Franc(6)
        assert Franc(5) != Dollar(5)
