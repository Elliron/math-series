from series_py import __version__
from series_py.fib import fibonacci
from series_py.fib import lucas

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_one_not_two():
    actual = fibonacci(1)
    expected = 2
    assert actual != expected

def test_one_three():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected

def test_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_two_not_two():
    actual = lucas(1)
    expected = 2
    assert actual !=expected

def test_two_three():
    actual = lucas(8)
    expected = 47
    assert actual == expected