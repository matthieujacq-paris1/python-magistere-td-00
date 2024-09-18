import pytest
from main import addition, print_hello

def test_addition():
    assert addition(1, 2) == 3
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(100, 200) == 300

def test_addition_negative_numbers():
    assert addition(-1, -1) == -2
    assert addition(-5, -3) == -8

def test_addition_floats():
    assert addition(1.5, 2.5) == 4.0
    assert addition(-1.1, 1.1) == 0.0

def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"

if __name__ == "__main__":
    pytest.main()
