import pytest

@pytest.mark.smoke
def test_add_func():
    a,b = 5,3
    s = a+b

    assert s == 8


def test_sub_func():
    a, b = 5, 3
    s = a - b

    assert s == 2

def test_type3():
    a, b = 5, 3
    s = a + b

    assert s == 8
