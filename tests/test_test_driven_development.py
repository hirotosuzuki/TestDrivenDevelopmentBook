from test_driven_development import __version__
from test_driven_development.dollar import Dollar


def test_version():
    assert __version__ == '0.1.0'


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        assert five.amount==10