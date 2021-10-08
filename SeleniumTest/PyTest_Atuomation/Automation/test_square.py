import math
import pytest


@pytest.mark.Login
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.PaymentAutomatiom
def test_square():
    num = 7
    assert 7 * 7 == 49


@pytest.mark.smoke
def test_equality():
    assert 10 == 10
