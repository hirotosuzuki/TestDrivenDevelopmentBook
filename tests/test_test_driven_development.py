from test_driven_development import __version__
from test_driven_development.dollar import Dollar


def test_version():
    assert __version__ == '0.1.0'


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        assert product.amount==10
        product = five.times(3)
        assert product.amount==15
    
    def test_equality(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))